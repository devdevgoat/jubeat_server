"""Add userid/arcadeid columns to audit logs for PASELI audits.

Revision ID: 45438cc39f6d
Revises: 04f3eab9ae7a
Create Date: 2017-04-12 18:08:47.521622

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45438cc39f6d'
down_revision = '04f3eab9ae7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('audit', sa.Column('arcadeid', sa.Integer(), nullable=True))
    op.add_column('audit', sa.Column('userid', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_audit_arcadeid'), 'audit', ['arcadeid'], unique=False)
    op.create_index(op.f('ix_audit_userid'), 'audit', ['userid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_audit_userid'), table_name='audit')
    op.drop_index(op.f('ix_audit_arcadeid'), table_name='audit')
    op.drop_column('audit', 'userid')
    op.drop_column('audit', 'arcadeid')
    # ### end Alembic commands ###
