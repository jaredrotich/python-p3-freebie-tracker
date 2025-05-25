"""create db

Revision ID: 7a71dbf71c64
Revises: 
Create Date: 2023-03-15 15:05:55.516631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a71dbf71c64'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
   op.create_table(
       'freebies',
       sa.Column('id', sa.Integer(), nullable=False),
       sa.Column('item_name', sa.String(), nullable=True),
       sa.Column('value', sa.Integer(), nullable=True),
       sa.Column('dev_id', sa.Integer(), sa.ForeignKey('devs.id')),
       sa.Column('company_id', sa.Integer(), sa.ForeignKey('companies.id')),
       sa.PrimaryKeyConstraint('id')
   )


def downgrade() -> None:
    op.drop_table('freebies')
