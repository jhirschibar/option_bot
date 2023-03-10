"""letting_type_be_null

Revision ID: 45ad99804ee9
Revises: cea0cb8a78f5
Create Date: 2023-02-21 08:21:13.928385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45ad99804ee9'
down_revision = 'cea0cb8a78f5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('stock_tickers', 'type',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('stock_tickers', 'type',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
