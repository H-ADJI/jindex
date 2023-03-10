"""create tables

Revision ID: 9d744b9db63d
Revises: bbe22431c036
Create Date: 2023-02-01 18:31:32.376436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d744b9db63d'
down_revision = 'bbe22431c036'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('keywords',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('keyword', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('keyword')
    )
    op.create_index(op.f('ix_keywords_id'), 'keywords', ['id'], unique=False)
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('location')
    )
    op.create_index(op.f('ix_locations_id'), 'locations', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('linkedin_id', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('company', sa.String(), nullable=True),
    sa.Column('company_url', sa.String(), nullable=True),
    sa.Column('search_keyword_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['search_keyword_id'], ['keywords.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_jobs_id'), 'jobs', ['id'], unique=False)
    op.create_index(op.f('ix_jobs_linkedin_id'), 'jobs', ['linkedin_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_jobs_linkedin_id'), table_name='jobs')
    op.drop_index(op.f('ix_jobs_id'), table_name='jobs')
    op.drop_table('jobs')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_locations_id'), table_name='locations')
    op.drop_table('locations')
    op.drop_index(op.f('ix_keywords_id'), table_name='keywords')
    op.drop_table('keywords')
    # ### end Alembic commands ###
