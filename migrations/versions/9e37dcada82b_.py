"""empty message

Revision ID: 9e37dcada82b
Revises: 9632f63052e5
Create Date: 2023-02-23 08:54:28.857099

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9e37dcada82b'
down_revision = '9632f63052e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('leave', schema=None) as batch_op:
        batch_op.add_column(sa.Column('processed_date', sa.Date(), nullable=True))
        batch_op.add_column(sa.Column('processed_by', sa.String(length=50), nullable=True))
        batch_op.drop_column('approved_date')
        batch_op.drop_column('approved_by')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('leave', schema=None) as batch_op:
        batch_op.add_column(sa.Column('approved_by', mysql.VARCHAR(length=50), nullable=True))
        batch_op.add_column(sa.Column('approved_date', sa.DATE(), nullable=True))
        batch_op.drop_column('processed_by')
        batch_op.drop_column('processed_date')

    # ### end Alembic commands ###
