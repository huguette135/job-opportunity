"""Initial Migration

Revision ID: ace6fa25b2ce
Revises: 
Create Date: 2020-12-08 11:46:09.280823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ace6fa25b2ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=225), nullable=False),
    sa.Column('fullname', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('bio', sa.String(length=255), nullable=True),
    sa.Column('image', sa.String(length=225), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('facebook', sa.String(), nullable=True),
    sa.Column('twitter', sa.String(), nullable=True),
    sa.Column('github', sa.String(), nullable=True),
    sa.Column('linkedin', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('posted_date', sa.DateTime(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('image', sa.String(length=225), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=255), nullable=True),
    sa.Column('comment', sa.Text(), nullable=False),
    sa.Column('posted_date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    op.drop_table('post')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
