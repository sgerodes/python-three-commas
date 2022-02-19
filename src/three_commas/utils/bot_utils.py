import logging
from ..model import *
from typing import List, Union


logger = logging.getLogger(__name__)


def _get_bot_math_arguments(bot: BotEntity) -> dict:
    return {
        'base_order_volume': bot.get_base_order_volume(),
        'safety_order_volume': bot.get_safety_order_volume(),
        'max_safety_orders': bot.get_max_safety_orders(),
        'martingale_volume_coefficient': bot.get_martingale_volume_coefficient(),
        'max_active_deals': bot.get_max_active_deals(),
    }


def calculate_so_multiplier(max_so: float, martingale: float) -> float:
    return max_so if martingale == 1 else (martingale ** max_so - 1) / (martingale-1)


def get_max_bot_usage(bot: BotEntity) -> float:
    return calculate_max_bot_usage(**_get_bot_math_arguments(bot))


def calculate_max_bot_usage(base_order_volume: float,
                            safety_order_volume: float,
                            max_safety_orders: int,
                            martingale_volume_coefficient: float,
                            max_active_deals: int) -> float:
    return (base_order_volume + safety_order_volume *
            calculate_so_multiplier(max_safety_orders, martingale_volume_coefficient)) * max_active_deals


def calculate_bo(max_bot_usage: float,
                 max_active_deals: int,
                 max_safety_orders: int,
                 martingale_volume_coefficient: float,
                 so: float) -> float:
    return max_bot_usage / max_active_deals - so * \
           calculate_so_multiplier(max_safety_orders, martingale_volume_coefficient)


def calculate_bo_with_so_bo_ratio(max_bot_usage: float,
                                  max_active_deals: int,
                                  max_safety_orders: int,
                                  martingale_volume_coefficient: float,
                                  so_bo_ratio: float) -> float:
    return max_bot_usage / max_active_deals /\
           (1 + so_bo_ratio * calculate_so_multiplier(max_safety_orders, martingale_volume_coefficient))


def calculate_max_active_deals(max_bot_usage: float,
                               max_safety_orders: int,
                               martingale_volume_coefficient: float,
                               base_order_volume: float,
                               safety_order_volume: float) -> float:
    return max_bot_usage / (base_order_volume + safety_order_volume *
                            calculate_so_multiplier(max_safety_orders, martingale_volume_coefficient))


def get_bot_quote(bot: BotEntity) -> Union[str, None]:
    pairs = bot.get_pairs()
    if not pairs:
        return None
    return pairs[0].split('_')[0].upper()


def get_bot_base(bot: BotEntity) -> Union[str, None]:
    pairs = bot.get_pairs()
    if not pairs:
        return None
    return pairs[0].split('_')[1].upper()


def bot_has_pair(bot: BotEntity, pair: str) -> bool:
    return bot.get_pairs() and pair in bot.get_pairs()


def filter_list_bot_having_pair(bot_list: List[BotEntity], pair: str) -> List[BotEntity]:
    return [bot for bot in bot_list if bot_has_pair(bot, pair)]
