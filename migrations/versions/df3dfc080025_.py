"""empty message

Revision ID: df3dfc080025
Revises: 6ba4e1f913f2
Create Date: 2023-02-22 16:11:23.301151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df3dfc080025'
down_revision = '6ba4e1f913f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('announcements', schema=None) as batch_op:
        batch_op.drop_constraint('announcements_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('attendance', schema=None) as batch_op:
        batch_op.drop_constraint('attendance_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'employee_info', ['employee_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('employment_info', schema=None) as batch_op:
        batch_op.drop_constraint('employment_info_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'employee_info', ['employee_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('leave', schema=None) as batch_op:
        batch_op.drop_constraint('leave_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'employee_info', ['employee_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint('users_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'employee_info', ['employee_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('users_ibfk_1', 'employee_info', ['employee_id'], ['id'])

    with op.batch_alter_table('leave', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('leave_ibfk_1', 'employee_info', ['employee_id'], ['id'])

    with op.batch_alter_table('employment_info', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('employment_info_ibfk_1', 'employee_info', ['employee_id'], ['id'])

    with op.batch_alter_table('attendance', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('attendance_ibfk_1', 'employee_info', ['employee_id'], ['id'])

    with op.batch_alter_table('announcements', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('announcements_ibfk_1', 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###