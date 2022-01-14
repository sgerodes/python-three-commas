import three_commas.api
import three_commas.site
from cachetools import cached, TTLCache
from three_commas.model import BotShow, Account, DealMarketOrder, DealShow, PieChartDataElement
from typing import List, Union


@cached(cache=TTLCache(maxsize=1024, ttl=60))
def get_deals(*args, **kwargs) -> List[DealShow]:
    return three_commas.api.get_deals(*args, **kwargs)


@cached(cache=TTLCache(maxsize=1024, ttl=60))
def get_all_deals(*args, **kwargs) -> List[DealShow]:
    return three_commas.api.get_all_deals(*args, **kwargs)


@cached(cache=TTLCache(maxsize=1024, ttl=60*3))
def get_market_pairs(*args, **kwargs) -> List[str]:
    return three_commas.api.get_market_pairs(*args, **kwargs)


@cached(cache=TTLCache(maxsize=1024, ttl=60*3))
def get_account(*args, **kwargs) -> Account:
    return three_commas.api.get_account(*args, **kwargs)


@cached(cache=TTLCache(maxsize=1024, ttl=60*15))
def get_url_secret(bot_id: int) -> str:
    bot_model: BotShow = three_commas.api.get_bot(bot_id=bot_id)
    return bot_model.get_url_secret()


@cached(cache=TTLCache(maxsize=1024, ttl=60*60*24))
def get_bot_account_id(bot_id: int) -> int:
    bot_model: BotShow = three_commas.api.get_bot(bot_id=bot_id)
    return bot_model.get_account_id()


@cached(cache=TTLCache(maxsize=1024, ttl=60*3))
def get_bot_profit_line_chart_data(*args, **kwargs):
    return three_commas.site.get_bot_profit_line_chart_data(*args, **kwargs)


@cached(cache=TTLCache(maxsize=1024, ttl=60))
def get_pie_chart_data(*args, **kwargs) -> List[PieChartDataElement]:
    return three_commas.api.get_pie_chart_data(*args, **kwargs)
