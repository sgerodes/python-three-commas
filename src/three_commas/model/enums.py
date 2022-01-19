from enum import Enum
from typing import List
from aenum import extend_enum
import logging


logger = logging.getLogger(__name__)


class AbstractStringEnum(Enum):
    @classmethod
    def _missing_(cls, value):
        logger.warning(f"Enum value='{value}' for {cls} is not known. Will extend the Enum. Allowed values were {cls.list_values()}")
        extend_enum(cls, value.upper(), value)
        return cls(value)

    @classmethod
    def list_values(cls) -> List[str]:
        return list(cls._value2member_map_.keys())
        # return list(map(lambda c: c.value, cls))

    @classmethod
    def list_members(cls) -> List[str]:
        return list(cls._value2member_map_.values())
        # return list(map(lambda c: c, cls))

    @classmethod
    def has_value(cls, value: str):
        return value in cls._value2member_map_

    @classmethod
    def has_member(cls, member: str):
        return member in cls._member_names_

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == other
        else:
            return super.__eq__(self, other)

    def __str__(self):
        return self.value


class BotScope(AbstractStringEnum):
    ENABLED = 'enabled'
    DISABLED = 'disabled'

    def is_enabled(self) -> bool:
        return self == BotScope.ENABLED

    def is_disabled(self) -> bool:
        return self == BotScope.DISABLED


class DealStatus(AbstractStringEnum):
    ACTIVE = 'active'
    FINISHED = 'finished'
    COMPLETED = 'completed'
    CANCELED = 'cancelled'
    FAILED = 'failed'

    def is_active(self) -> bool:
        return self == DealStatus.ACTIVE

    def is_completed(self) -> bool:
        return self == DealStatus.COMPLETED


class ForcedMode(AbstractStringEnum):
    PAPER = 'paper'
    REAL = 'real'


class MarketCode(AbstractStringEnum):
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
