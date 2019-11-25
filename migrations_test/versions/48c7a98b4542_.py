"""empty message

Revision ID: 48c7a98b4542
Revises: 
Create Date: 2019-11-25 17:35:58.892663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48c7a98b4542'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('players',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=60), nullable=False),
    sa.Column('last_name', sa.String(length=60), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('gender', sa.String(length=50), nullable=False),
    sa.Column('ability', sa.String(length=50), nullable=False),
    sa.Column('dob', sa.Date(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('players')
    # ### end Alembic commands ###
