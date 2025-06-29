"""create pdfs table

Revision ID: b28ab3bb8307
Revises: 
Create Date: 2025-06-29 14:25:59.028900

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b28ab3bb8307'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'pdfs',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('name', sa.Text, nullable=False),
        sa.Column('file', sa.Text, nullable=False),
        sa.Column('selected', sa.Boolean, nullable=False, default=False)
    )

def downgrade():
    op.drop_table('pdfs')
