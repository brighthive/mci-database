"""empty message

Revision ID: 08dad05889a9
Revises: 05c4d470cd9c
Create Date: 2020-07-22 13:07:06.139549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08dad05889a9'
down_revision = '05c4d470cd9c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('individual', sa.Column(
        'vendor_creation_date', sa.DateTime(), nullable=True))


def downgrade():
    op.drop_column('individual', 'vendor_creation_date')
