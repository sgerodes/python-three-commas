from enum import Enum


class AbstractThreeCommasEnum(Enum):
    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == other
        else:
            return super.__eq__(self, other)

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

    def __str__(self):
        return self.value


class BotScope(AbstractThreeCommasEnum):
    ENABLED = 'enabled'
    DISABLED = 'disabled'


class DealStatus(AbstractThreeCommasEnum):
    ACTIVE = 'active'
    FINISHED = 'finished'
    COMPLETED = 'completed'
    CANCELED = 'cancelled'
    FAILED = 'failed'


class ForcedMode(AbstractThreeCommasEnum):
    PAPER = 'paper'
    REAL = 'real'


class MarketCode(AbstractThreeCommasEnum):
    PAPER_TRADING = 'paper_trading'
    BINANCE = 'binance'
    BITFINEX = 'bitfinex'
    BITSTAMP = 'bitstamp'
    BITTREX = 'bittrex'
    GDAX = 'gdax'
    GEMINI = 'gemini'
    HUOBI = 'huobi'
    KUCOIN = 'kucoin'
    OKEX = 'okex'
    POLONIEX = 'poloniex'
    BITMEX = 'bitmex'
    KRAKEN = 'kraken'
    GATE_IO = 'gate_io'
    BINANCE_MARGIN = 'binance_margin'
    BYBIT = 'bybit'
    BINANCE_US = 'binance_us'
    BINANCE_FUTURES = 'binance_futures'
    DERIBIT = 'deribit'
    FTX = 'ftx'
    FTX_US = 'ftx_us'
    BYBIT_USDT_PERPETUAL = 'bybit_usdt_perpetual'
    BINANCE_FUTURES_COIN = 'binance_futures_coin'
    BYBIT_SPOT = 'bybit_spot'
    GATE_IO_USDT_PERPETUAL = 'gate_io_usdt_perpetual'
    GATE_IO_BTC_PERPETUAL = 'gate_io_btc_perpetual'
    ETHEREUMWALLET = 'ethereumwallet'
    TRX = 'trx'
