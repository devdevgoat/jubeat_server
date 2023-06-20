"""Add user link table.

Revision ID: 21c19a671b3b
Revises: f1fe9fce9ace
Create Date: 2017-02-09 20:28:01.361801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21c19a671b3b'
down_revision = 'f1fe9fce9ace'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('link',
    sa.Column('game', sa.String(length=32), nullable=False),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=64), nullable=False),
    sa.Column('other_userid', sa.Integer(), nullable=False),
    sa.Column('data', sa.JSON(), nullable=False),
    sa.UniqueConstraint('game', 'version', 'userid', 'type', 'other_userid', name='game_version_userid_type_other_uuserid'),
    mysql_charset='utf8mb4'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('link')
    # ### end Alembic commands ###
