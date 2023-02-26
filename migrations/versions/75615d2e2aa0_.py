"""empty message

Revision ID: 75615d2e2aa0
Revises: fdb272058877
Create Date: 2023-02-24 16:11:37.688990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75615d2e2aa0'
down_revision = 'fdb272058877'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payslips', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.String(length=500), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payslips', schema=None) as batch_op:
        batch_op.drop_column('status')

    # ### end Alembic commands ###