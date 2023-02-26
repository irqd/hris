"""empty message

Revision ID: 80a647648311
Revises: a92580957106
Create Date: 2023-02-26 16:44:11.260069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80a647648311'
down_revision = 'a92580957106'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee_info', schema=None) as batch_op:
        batch_op.drop_index('email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee_info', schema=None) as batch_op:
        batch_op.create_index('email', ['email'], unique=False)

    # ### end Alembic commands ###
