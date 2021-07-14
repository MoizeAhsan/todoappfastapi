"""empty message

Revision ID: 055ea9490d76
Revises: 50e81d43f7aa
Create Date: 2021-07-14 19:13:37.405316

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from app.models.todo import PriorityEnum


# revision identifiers, used by Alembic.
revision = '055ea9490d76'
down_revision = '50e81d43f7aa'
branch_labels = None
depends_on = None


def upgrade():
    pe = postgresql.ENUM(PriorityEnum, name='priorityenum')
    pe.create(op.get_bind(), checkfirst= True)
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('is_completed', sa.Boolean(), nullable=False))
    op.add_column('todo', sa.Column('due_date', sa.Date(), nullable=True))
    op.add_column('todo', sa.Column('priority', pe, server_default='NONE', nullable=False))
    # ### end Alembic commands ###


def downgrade():

    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo', 'priority')
    op.drop_column('todo', 'due_date')
    op.drop_column('todo', 'is_completed')
    # ### end Alembic commands ###
    pe= postgresql.ENUM(PriorityEnum, name='priorityenum')
    pe.drop(op.get_bind())