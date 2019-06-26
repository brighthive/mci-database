"""empty message

Revision ID: a50481349c3c
Revises: 3b012868551d
Create Date: 2019-06-26 12:10:20.384880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a50481349c3c'
down_revision = '3b012868551d'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('individual', 'first_name', nullable=True)
    op.alter_column('individual', 'date_of_birth', nullable=True)


def downgrade():
    op.alter_column('individual', 'first_name', nullable=False)
    op.alter_column('individual', 'date_of_birth', nullable=False)
