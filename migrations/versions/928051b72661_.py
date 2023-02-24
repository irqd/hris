"""empty message

Revision ID: 928051b72661
Revises: 51f1147cfbd1
Create Date: 2023-02-23 13:39:34.626068

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '928051b72661'
down_revision = '51f1147cfbd1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('salaries', schema=None) as batch_op:
        batch_op.alter_column('daily_rate',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.Float(precision=2, asdecimal=True),
               existing_nullable=False)
        batch_op.alter_column('hourly_rate',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.Float(precision=2, asdecimal=True),
               existing_nullable=False)
        batch_op.alter_column('bir_tax',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.Float(precision=2, asdecimal=True),
               existing_nullable=False)
        batch_op.alter_column('sss_tax',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.Float(precision=2, asdecimal=True),
               existing_nullable=False)
        batch_op.alter_column('phil_health_tax',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.Float(precision=2, asdecimal=True),
               existing_nullable=False)
        batch_op.alter_column('pag_ibig_tax',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.Float(precision=2, asdecimal=True),
               existing_nullable=False)
        batch_op.alter_column('ot_rate',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.Float(precision=2, asdecimal=True),
               existing_nullable=False)
        batch_op.alter_column('allowance',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.Float(precision=2, asdecimal=True),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('salaries', schema=None) as batch_op:
        batch_op.alter_column('allowance',
               existing_type=sa.Float(precision=2, asdecimal=True),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=False)
        batch_op.alter_column('ot_rate',
               existing_type=sa.Float(precision=2, asdecimal=True),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=False)
        batch_op.alter_column('pag_ibig_tax',
               existing_type=sa.Float(precision=2, asdecimal=True),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=False)
        batch_op.alter_column('phil_health_tax',
               existing_type=sa.Float(precision=2, asdecimal=True),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=False)
        batch_op.alter_column('sss_tax',
               existing_type=sa.Float(precision=2, asdecimal=True),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=False)
        batch_op.alter_column('bir_tax',
               existing_type=sa.Float(precision=2, asdecimal=True),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=False)
        batch_op.alter_column('hourly_rate',
               existing_type=sa.Float(precision=2, asdecimal=True),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=False)
        batch_op.alter_column('daily_rate',
               existing_type=sa.Float(precision=2, asdecimal=True),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=False)

    # ### end Alembic commands ###
