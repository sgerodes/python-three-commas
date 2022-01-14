from src.three_commas.api import get_bot
from .model import *
import requests
import logging
from logging_configuration import logged
import json


logger = logging.getLogger(__name__)


BASE_URL = 'https://3commas.io'


@logged
def get_bot_profit_line_chart_data(bot_id: int):
    bot_model: BotShow = get_bot(bot_id=bot_id)
    url_secret = bot_model.get_url_secret()
    parameters = {
        'secret': url_secret,
    }
    url = f'{BASE_URL}/bots/{bot_id}/profit_line_chart_data'
    response = requests.get(url=url,params=parameters)
    if not response.status_code == 200:
        return None
    obj = json.loads(response.text)
    return obj


def get_bot_deals_history(bot_id: int):
    # not working
    bot_model: BotShow = get_bot(bot_id=bot_id)
    url_secret = bot_model.get_url_secret()
    parameters = {
        'secret': url_secret,
        'history': 'true',
        'start_at_from': '',
        'start_at_to': '',
        'closed_at_from': '',
        'closed_at_to': '',
        'account_ids': '',
        'bot_ids': f'{bot_id}',
        'order_column': 'closed_at',
        'order_direction': 'desc',
        'page': 1,
        'per_page': 10,
    }
    url = f'{BASE_URL}/deals/history'
    response = requests.get(url=url, params=parameters)
    if not response.status_code == 200:
        return None
    obj = json.loads(response.text)
    return obj
