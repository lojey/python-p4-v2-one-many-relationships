"""add foreign key to Review

Revision ID: 9ee308f2cc48
Revises: 4096dbda5946
Create Date: 2024-12-09 12:33:30.695891

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ee308f2cc48'
down_revision = '4096dbda5946'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employees', sa.Column('employee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_employees_employee_id_employees'), 'employees', 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_employees_employee_id_employees'), 'employees', type_='foreignkey')
    op.drop_column('employees', 'employee_id')
    # ### end Alembic commands ###
