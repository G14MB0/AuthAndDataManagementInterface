from app import schemas, utils
from app.database import get_db
from app import oauth2
from app import models

from sqlalchemy.orm import Session

#fastAPI things
from fastapi import status, HTTPException, APIRouter, Depends
from sqlalchemy.exc import IntegrityError

#pydantic things
from typing import  List #list is used to define a response model that return a list


router = APIRouter(
    prefix="/note",
    tags=['Note']
)

@router.get("/", response_model=List[schemas.NoteResponse])
def get_note(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), title: str = ""):
    """Get all the note for that user (users table rows) or filtered by a title

    Returns:
        list[dict]: all the user's inventories
    """    
    if title == "":
        note = db.query(models.Note).filter(models.Note.owner_id == current_user.id).all()
        return note
    else:
        note = db.query(models.Note).filter(models.Note.owner_id == current_user.id, models.Note.title == title).first()
        if not note:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No note titled: {title}')
        return [note] # return a list to match the response_model even if it's only one



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.NoteResponse)
def create_note(data: schemas.NoteCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    try:
        # If note does not exist, create a new record
        new_note = models.Note(title=data.title, content=data.content, owner_id=current_user.id)
        db.add(new_note)
        db.commit()
        db.refresh(new_note)
        return new_note
    
    except IntegrityError as e:
        db.rollback()  # Rollback the session to a clean state
        # Check if the exception is due to a unique constraint violation
        if "unique" in str(e.orig) or "duplicat" in str(e.orig):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Duplicate note title")
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
    except Exception as e:
        db.rollback()  # Ensure the session is rolled back in case of any other exceptions
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")


@router.delete("/{id}")
def delete_note(title: str, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    if title != "":
        data = db.query(models.Note).filter(models.Note.owner_id == current_user.id, models.Note.id == id).first()
        if data is None:
            raise HTTPException(status_code=404, detail="Note not found")
        else:
            # If note exists, delete it
            db.delete(data)
            db.commit()
    else:
        raise HTTPException(status_code=404, detail="No note title has been passed")
    
    return {"message": f"note with title {title} correctly deleted"}


