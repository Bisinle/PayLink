"""added  the balance col and changed it's data type to float in wallet

Revision ID: 9acc0de97545
Revises: ded3156f40a6
Create Date: 2023-11-01 20:05:00.818335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9acc0de97545'
down_revision = 'ded3156f40a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wallets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('balance', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wallets', schema=None) as batch_op:
        batch_op.drop_column('balance')

    # ### end Alembic commands ###
