"""create tables

Revision ID: e8b2456dfd23
Revises: 9d744b9db63d
Create Date: 2023-02-01 18:36:24.616331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8b2456dfd23'
down_revision = '9d744b9db63d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jobs', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'jobs', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'jobs', type_='foreignkey')
    op.drop_column('jobs', 'user_id')
    # ### end Alembic commands ###
