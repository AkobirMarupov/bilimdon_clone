"""nullables changed

Revision ID: 08220d19f09b
Revises: c864be807025
Create Date: 2025-04-10 20:00:19.749031

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08220d19f09b'
down_revision: Union[str, None] = 'c864be807025'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'first_name',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    op.alter_column('users', 'last_name',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'last_name',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    op.alter_column('users', 'first_name',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    # ### end Alembic commands ###
