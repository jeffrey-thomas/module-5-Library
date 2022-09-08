"""empty message

Revision ID: a488d697dbc9
Revises: ec42057dea8e
Create Date: 2022-09-08 11:39:01.729348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a488d697dbc9'
down_revision = 'ec42057dea8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('car', sa.Column('user_token', sa.String(), nullable=False))
    op.create_foreign_key(None, 'car', 'user', ['user_token'], ['token'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'car', type_='foreignkey')
    op.drop_column('car', 'user_token')
    # ### end Alembic commands ###