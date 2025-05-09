"""empty message

Revision ID: 75c96964810d
Revises: c227f622f10b
Create Date: 2025-04-18 18:30:11.527431

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75c96964810d'
down_revision: Union[str, None] = 'c227f622f10b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('voters', sa.Column('full_name', sa.String(), nullable=False))
    op.add_column('voters', sa.Column('user_id', sa.Integer(), autoincrement=True, primary_key=True))
    op.add_column('voters', sa.Column('password', sa.String(), nullable=False))
    op.drop_column('voters', 'fullName')
    op.drop_column('voters', 'userId')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('voters', sa.Column('userId', sa.INTEGER(), autoincrement=True, nullable=False))
    op.add_column('voters', sa.Column('fullName', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('voters', 'password')
    op.drop_column('voters', 'user_id')
    op.drop_column('voters', 'full_name')
    # ### end Alembic commands ###
