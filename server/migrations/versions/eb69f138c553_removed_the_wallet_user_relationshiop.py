"""removed the wallet user relationshiop 

Revision ID: eb69f138c553
Revises: c79bbbea5138
Create Date: 2023-10-27 13:21:28.865527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb69f138c553'
down_revision = 'c79bbbea5138'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wallets', schema=None) as batch_op:
        batch_op.drop_constraint('fk_wallets_user_id_users', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wallets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_wallets_user_id_users', 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###
