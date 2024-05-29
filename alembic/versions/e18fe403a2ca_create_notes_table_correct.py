"""create_notes_table_correct

Revision ID: e18fe403a2ca
Revises: 9750ea042f2b
Create Date: 2024-05-29 11:00:06.782385

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e18fe403a2ca'
down_revision: Union[str, None] = '9750ea042f2b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
