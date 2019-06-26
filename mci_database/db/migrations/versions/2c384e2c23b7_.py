"""empty message

Revision ID: 2c384e2c23b7
Revises: a50481349c3c
Create Date: 2019-06-26 12:24:53.477059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c384e2c23b7'
down_revision = 'a50481349c3c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('individual_pii_removal',
                    sa.Column('removal_timestamp', sa.DateTime(),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('comment', sa.String(length=100), nullable=True),
                    sa.Column('individual_id', sa.String(length=40), nullable=False),
                    sa.ForeignKeyConstraint(['individual_id'], ['individual.mci_id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('individual_id')
                    )


def downgrade():
    op.drop_table('individual_pii_removal')
