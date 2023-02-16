"""initial market data schema

Revision ID: 52d25047cded
Revises: 
Create Date: 2023-02-16 08:58:06.578865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52d25047cded'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stock_tickers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ticker_symbol', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('options_tickers',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('underlying_ticker_id', sa.Integer(), nullable=False),
    sa.Column('option_ticker', sa.String(), nullable=False),
    sa.Column('exp_date', sa.Date(), nullable=False),
    sa.Column('strike_price', sa.DECIMAL(precision=19, scale=4), nullable=False),
    sa.Column('option_type', sa.Enum('call', 'put', name='optiontype'), nullable=False),
    sa.ForeignKeyConstraint(['underlying_ticker_id'], ['stock_tickers.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('option_prices',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('options_ticker_id', sa.BigInteger(), nullable=False),
    sa.Column('price_date', sa.Date(), nullable=False),
    sa.Column('as_of_date', sa.DateTime(), nullable=False),
    sa.Column('close_price', sa.DECIMAL(precision=19, scale=4), nullable=False),
    sa.Column('open_price', sa.DECIMAL(precision=19, scale=4), nullable=False),
    sa.Column('high_price', sa.DECIMAL(precision=19, scale=4), nullable=False),
    sa.Column('low_price', sa.DECIMAL(precision=19, scale=4), nullable=False),
    sa.Column('volume_weight_price', sa.DECIMAL(precision=19, scale=4), nullable=False),
    sa.Column('volumn', sa.Integer(), nullable=False),
    sa.Column('number_of_trades', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('is_overwritten', sa.Boolean(), server_default=sa.text('false'), nullable=True),
    sa.ForeignKeyConstraint(['options_ticker_id'], ['options_tickers.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('options_ticker_id', 'price_date', 'as_of_date', name='uq_current_price')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('option_prices')
    op.drop_table('options_tickers')
    op.drop_table('stock_tickers')
    # ### end Alembic commands ###