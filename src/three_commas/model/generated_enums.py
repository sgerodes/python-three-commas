from .other_enums import AbstractStringEnum


class DealStatus(AbstractStringEnum):
    ACTIVE = 'active'
    FINISHED = 'finished'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'
    FAILED = 'failed'

    def is_active(self) -> bool:
        return self == DealStatus.ACTIVE

    def is_finished(self) -> bool:
        return self == DealStatus.FINISHED

    def is_completed(self) -> bool:
        return self == DealStatus.COMPLETED

    def is_cancelled(self) -> bool:
        return self == DealStatus.CANCELLED

    def is_failed(self) -> bool:
        return self == DealStatus.FAILED


class BotScope(AbstractStringEnum):
    ENABLED = 'enabled'
    DISABLED = 'disabled'

    def is_enabled(self) -> bool:
        return self == BotScope.ENABLED

    def is_disabled(self) -> bool:
        return self == BotScope.DISABLED


class Mode(AbstractStringEnum):
    PAPER = 'paper'
    REAL = 'real'

    def is_paper(self) -> bool:
        return self == Mode.PAPER

    def is_real(self) -> bool:
        return self == Mode.REAL


class AccountMarketCode(AbstractStringEnum):
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

    def is_paper_trading(self) -> bool:
        return self == AccountMarketCode.PAPER_TRADING

    def is_binance(self) -> bool:
        return self == AccountMarketCode.BINANCE

    def is_bitfinex(self) -> bool:
        return self == AccountMarketCode.BITFINEX

    def is_bitstamp(self) -> bool:
        return self == AccountMarketCode.BITSTAMP

    def is_bittrex(self) -> bool:
        return self == AccountMarketCode.BITTREX

    def is_gdax(self) -> bool:
        return self == AccountMarketCode.GDAX

    def is_gemini(self) -> bool:
        return self == AccountMarketCode.GEMINI

    def is_huobi(self) -> bool:
        return self == AccountMarketCode.HUOBI

    def is_kucoin(self) -> bool:
        return self == AccountMarketCode.KUCOIN

    def is_okex(self) -> bool:
        return self == AccountMarketCode.OKEX

    def is_poloniex(self) -> bool:
        return self == AccountMarketCode.POLONIEX

    def is_bitmex(self) -> bool:
        return self == AccountMarketCode.BITMEX

    def is_kraken(self) -> bool:
        return self == AccountMarketCode.KRAKEN

    def is_gate_io(self) -> bool:
        return self == AccountMarketCode.GATE_IO

    def is_binance_margin(self) -> bool:
        return self == AccountMarketCode.BINANCE_MARGIN

    def is_bybit(self) -> bool:
        return self == AccountMarketCode.BYBIT

    def is_binance_us(self) -> bool:
        return self == AccountMarketCode.BINANCE_US

    def is_binance_futures(self) -> bool:
        return self == AccountMarketCode.BINANCE_FUTURES

    def is_deribit(self) -> bool:
        return self == AccountMarketCode.DERIBIT

    def is_ftx(self) -> bool:
        return self == AccountMarketCode.FTX

    def is_ftx_us(self) -> bool:
        return self == AccountMarketCode.FTX_US

    def is_bybit_usdt_perpetual(self) -> bool:
        return self == AccountMarketCode.BYBIT_USDT_PERPETUAL

    def is_binance_futures_coin(self) -> bool:
        return self == AccountMarketCode.BINANCE_FUTURES_COIN

    def is_bybit_spot(self) -> bool:
        return self == AccountMarketCode.BYBIT_SPOT

    def is_gate_io_usdt_perpetual(self) -> bool:
        return self == AccountMarketCode.GATE_IO_USDT_PERPETUAL

    def is_gate_io_btc_perpetual(self) -> bool:
        return self == AccountMarketCode.GATE_IO_BTC_PERPETUAL

    def is_ethereumwallet(self) -> bool:
        return self == AccountMarketCode.ETHEREUMWALLET

    def is_trx(self) -> bool:
        return self == AccountMarketCode.TRX
