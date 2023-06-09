"""Inicializacao das tabelas.

Revision ID: 90d7a0e554b5
Revises: 
Create Date: 2023-04-24 16:24:05.512308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90d7a0e554b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pessoa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pessoa')
    # ### end Alembic commands ###
