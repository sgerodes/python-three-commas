import logging
from src.three_commas.model import Bot
from typing import List


logger = logging.getLogger(__name__)


def get_base_from_3c_pair(tc_pair: str, account_market_code: str) -> str:
    if account_market_code in {'ftx', 'binance', 'paper_trading'}:
        return tc_pair.split('_')[1].upper()
    elif account_market_code in {'ftx_futures'}:
        return tc_pair.split('_')[1].split('-')[0]
    else:
        raise RuntimeError(f'Not known market code {account_market_code} in get_base_from_3c_pair')


def filter_market_pairs_with_quote(market_pairs: List[str], quote: str):
    return [pair for pair in market_pairs if pair.upper().startswith(quote.upper())]


def get_quote_from_3c_pair(tc_pair: str) -> str:
    return tc_pair.split('_')[0].upper()


def pair_is_quote(tc_pair: str, quote: str) -> bool:
    return get_quote_from_3c_pair(tc_pair).upper() == quote.upper()


def map_spot_tc_pairs_to_bases(tc_pairs: list, account_market_code: str) -> list:
    return list(map(lambda pair: get_base_from_3c_pair(tc_pair=pair, account_market_code=account_market_code), tc_pairs))


def filter_tc_pairs_by_quote(pairs: list, quote: str) -> list:
    return list(filter(lambda pair: pair_is_quote(tc_pair=pair, quote=quote), pairs))


def construct_pair_from_quote_and_base(quote: str, base: str) -> str:
    return f"{quote.upper()}_{base.upper()}"


def construct_futures_pair_from_base(base: str, account_market_code: str) -> str:
    if account_market_code in {'ftx_futures'}:
        return f'USD_{base.upper()}-PERP'
    else:
        raise RuntimeError(f'Not known market code {account_market_code} in construct_futures_pair_from_quote_and_base')






