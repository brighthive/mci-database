"""empty message

Revision ID: 05c4d470cd9c
Revises: 2c384e2c23b7
Create Date: 2019-06-28 14:12:08.782826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05c4d470cd9c'
down_revision = '2c384e2c23b7'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('address', 'address', nullable=True)
    op.alter_column('address', 'city', nullable=True)
    op.alter_column('address', 'state', nullable=True)
    op.alter_column('address', 'postal_code', nullable=True)
    op.alter_column('address', 'country', nullable=True)


def downgrade():
    op.alter_column('address', 'address', nullable=False)
    op.alter_column('address', 'city', nullable=False)
    op.alter_column('address', 'state', nullable=False)
    op.alter_column('address', 'postal_code', nullable=False)
    op.alter_column('address', 'country', nullable=False)
