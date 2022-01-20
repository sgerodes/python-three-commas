

INDENT = '\t'


class EnumProperties:
    def __init__(self, name, values):
        self.name = name
        self.values = values


enums_list = [
    EnumProperties('DealStatus',
                   values=['active', 'finished', 'completed', 'cancelled', 'failed']),
    EnumProperties('BotScope',
                   values=['enabled', 'disabled']),
    EnumProperties('Mode',
                   values=['paper', 'real']),
    EnumProperties('MarketCode',
                   values=['paper_trading', 'binance', 'bitfinex', 'bitstamp', 'bittrex', 'gdax', 'gemini',
                           'huobi', 'kucoin', 'okex', 'poloniex', 'bitmex', 'kraken', 'gate_io', 'binance_margin',
                           'bybit', 'binance_us', 'binance_futures', 'deribit', 'ftx', 'ftx_us', 'bybit_usdt_perpetual',
                           'binance_futures_coin', 'bybit_spot', 'gate_io_usdt_perpetual', 'gate_io_btc_perpetual',
                           'ethereumwallet', 'trx']
)

]


def generate_enums():
    with open('../src/three_commas/model/generated_enums.py', 'w') as f:
        file_buffer = list()
        # imports
        file_buffer.append('from .enums import AbstractStringEnum')

        for ep in enums_list:
            file_buffer.append('')
            file_buffer.append('')
            file_buffer.append(f'class {ep.name}(AbstractStringEnum):')
            for value in ep.values:
                file_buffer.append(f"{INDENT}{value.upper()} = '{value}'")
            file_buffer.extend(create_enum_functions(ep))

        file_buffer.append('')

        generated_code = '\n'.join(file_buffer)
        f.write(generated_code)


def create_enum_functions(ep: EnumProperties):
    file_buffer = list()

    for value in ep.values:
        file_buffer.append('')
        file_buffer.append(f"{INDENT}def is_{value}(self) -> bool:")
        file_buffer.append(f"{INDENT*2}return self == {ep.name}.{value.upper()}")

    return file_buffer


if __name__ == '__main__':
    generate_enums()
