"""empty message

Revision ID: f45036e316fe
Revises: 80303bcabc81
Create Date: 2019-12-02 18:31:49.369869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f45036e316fe'
down_revision = '80303bcabc81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('players', sa.Column('bio', sa.String(length=200), nullable=True))
    op.add_column('players', sa.Column('sport', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('players', 'sport')
    op.drop_column('players', 'bio')
    # ### end Alembic commands ###
