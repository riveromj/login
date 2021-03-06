"""empty message

Revision ID: 290122aa2398
Revises: dcdd6c68909d
Create Date: 2021-09-26 11:19:34.128876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '290122aa2398'
down_revision = 'dcdd6c68909d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('name', sa.String(length=120), nullable=False))
    op.add_column('user', sa.Column('surname', sa.String(length=120), nullable=False))
    op.create_unique_constraint(None, 'user', ['surname'])
    op.create_unique_constraint(None, 'user', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'surname')
    op.drop_column('user', 'name')
    # ### end Alembic commands ###
