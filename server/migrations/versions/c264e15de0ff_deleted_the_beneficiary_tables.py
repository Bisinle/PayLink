"""deleted the beneficiary tables

Revision ID: c264e15de0ff
Revises: bedaa0e2bece
Create Date: 2023-11-01 12:46:26.801052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c264e15de0ff'
down_revision = 'bedaa0e2bece'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('beneficiaries')
    op.drop_table('user_beneficiaries')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_beneficiaries',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('beneficiary_id', sa.INTEGER(), nullable=True),
    sa.Column('sender_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['beneficiary_id'], ['beneficiaries.id'], name='fk_user_beneficiaries_beneficiary_id_beneficiaries'),
    sa.ForeignKeyConstraint(['sender_id'], ['users_profile.id'], name='fk_user_beneficiaries_sender_id_users_profile'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('beneficiaries',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_profile_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_profile_id'], ['users_profile.id'], name='fk_beneficiaries_user_profile_id_users_profile'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
