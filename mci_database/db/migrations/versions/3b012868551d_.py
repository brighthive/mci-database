"""empty message

Revision ID: 3b012868551d
Revises: 3187a44ef222
Create Date: 2019-06-20 21:56:27.664585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b012868551d'
down_revision = '3187a44ef222'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('individual', sa.Column(
        'telephone_2', sa.String(length=20), nullable=True))
    op.add_column('individual', sa.Column(
        'telephone_3', sa.String(length=20), nullable=True))

def downgrade():
    op.drop_column('individual', 'telephone_2')
    op.drop_column('individual', 'telephone_3')
