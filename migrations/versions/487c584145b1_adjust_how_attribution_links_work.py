"""Adjust how attribution links work

Revision ID: 487c584145b1
Revises: e4ee0183e767
Create Date: 2022-11-20 17:28:08.031650

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '487c584145b1'
down_revision = 'e4ee0183e767'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('attribution_links')
    op.create_table('attribution_person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('link', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('attribution', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sticker_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('person_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('attribution_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'attribution_person', ['person_id'], ['id'])
        batch_op.create_foreign_key(None, 'sticker', ['sticker_id'], ['id'])
        batch_op.drop_column('link')
        batch_op.drop_column('name')
        batch_op.drop_column('user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('attribution', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('link', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('attribution_user_id_fkey', 'user', ['user_id'], ['id'])
        batch_op.drop_column('person_id')
        batch_op.drop_column('sticker_id')

    op.drop_table('attribution_person')
    # ### end Alembic commands ###
