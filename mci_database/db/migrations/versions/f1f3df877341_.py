"""Add county field to Address.

Revision ID: f1f3df877341
Revises: 08dad05889a9
Create Date: 2020-11-09 09:52:20.889107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1f3df877341'
down_revision = '08dad05889a9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('address', sa.Column(
        'county', sa.String(length=125), nullable=True))


def downgrade():
    op.drop_column('address', 'county')
