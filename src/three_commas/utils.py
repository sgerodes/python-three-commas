import logging

from src.three_commas.error import ThreeCommasError
from src.three_commas.model import BotShow
from typing import List
from sys_utils import get_parent_function_name

logger = logging.getLogger(__name__)


class BotMath:
    # Legend: mabu is max amount bot usage
    def __init__(self, bot_show: BotShow):
        self.bot_show = bot_show

    def get_max_bot_usage(self) -> float:
        bo = self.bot_show.get_base_order_volume()
        so = self.bot_show.get_safety_order_volume()
        max_so = self.bot_show.get_max_safety_orders()
        martingale = self.bot_show.get_martingale_volume_coefficient()
        mad = self.bot_show.get_max_active_deals()
        return BotMath.calculate_max_bot_usage(bo=bo, so=so, max_so=max_so, martingale=martingale, mad=mad)

    @staticmethod
    def calculate_max_bot_usage(bo: float, so: float, max_so: int, martingale: float, mad: int) -> float:
        return (bo + so * BotMath.calculate_so_multiplicator(max_so, martingale)) * mad

    @staticmethod
    def calculate_so_multiplicator(max_so: float, martingale: float) -> float:
        return max_so if martingale == 1 else (martingale ** max_so - 1) / (martingale-1)

    @staticmethod
    def calculate_bo(mabu: float, mad: int, max_so: int, martingale: float, so: float) -> float:
        return mabu / mad - so * BotMath.calculate_so_multiplicator(max_so, martingale)

    @staticmethod
    def calculate_bo_with_so_bo_ratio(mabu: float, mad: int, max_so: int, martingale: float, so_bo_ratio: float) -> float:
        return mabu / mad / (1 + so_bo_ratio * BotMath.calculate_so_multiplicator(max_so, martingale))

    @staticmethod
    def calculate_mad(mabu: float, max_so: int, martingale: float, bo: float, so: float):
        return mabu / (bo + so * BotMath.calculate_so_multiplicator(max_so, martingale))


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


def filter_list_bot_show_having_pair(list_bot_show: List[BotShow], pair: str) -> List[BotShow]:
    return [bot_model for bot_model in list_bot_show if bot_model.has_pair(pair)]


def verify_no_error(error, data):
    calling_function_name = get_parent_function_name()
    if error:
        error['function_name'] = calling_function_name
        logger.error(error)
        raise ThreeCommasError(error=error)
    if data is None:
        logger.warning(f'No data was received for function {calling_function_name}')
        raise ThreeCommasError(error={'msg': 'Data is None', 'function_name': calling_function_name})



