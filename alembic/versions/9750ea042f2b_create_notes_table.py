"""create_notes_table

Revision ID: 9750ea042f2b
Revises: 829320c1b51d
Create Date: 2024-05-29 10:53:27.910368

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9750ea042f2b'
down_revision: Union[str, None] = '829320c1b51d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
