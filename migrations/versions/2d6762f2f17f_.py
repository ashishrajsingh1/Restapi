"""empty message

Revision ID: 2d6762f2f17f
Revises: 1653a609f3fc
Create Date: 2023-11-16 15:27:04.913735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d6762f2f17f'
down_revision = '1653a609f3fc'
branch_labels = None
depends_on = None


def upgrade():

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(), nullable=True))
        batch_op.create_unique_constraint("mail", ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('email')

    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###
