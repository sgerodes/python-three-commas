from py3cw.request import Py3CW
import os
import logging
from .logging_configuration import logged
from . import utils
from .model import BotShow, Account, DealMarketOrder, DealShow, PieChartDataElement
from typing import List

logger = logging.getLogger(__name__)


def get_p3cw() -> Py3CW:
    api_key = os.getenv("THREE_COMMAS_API_KEY")
    api_secret = os.getenv("THREE_COMMAS_API_SECRET")
    if api_key is None or api_secret is None:
        raise RuntimeError("Please configure 'THREE_COMMAS_API_KEY' and 'THREE_COMMAS_API_SECRET' in your environment variables")
    return Py3CW(key=api_key, secret=api_secret)


# Bots

@logged
def get_pairs_black_list() -> List[str]:
    error, data = get_p3cw().request(
        entity='bots',
        action='pairs_black_list'
    )
    utils.verify_no_error(error=error, data=data)
    return data


@logged
def disable_bot(bot_id: int):
    error, data = get_p3cw().request(
        entity='bots',
        action='disable',
        action_id=str(bot_id)
    )
    utils.verify_no_error(error=error, data=data)
    return data


@logged(log_return=True)
def copy_and_create(bot_id: int, new_bot_name: str,  old_bot_url_secret: str):
    """
    POST /ver1/bots/{bot_id}/copy_and_create
    """
    error, data = get_p3cw().request(
        entity='bots',
        action='copy_and_create',
        action_id=str(bot_id),
        payload={
            'name': new_bot_name,
            'secret': old_bot_url_secret
        }
    )
    utils.verify_no_error(error=error, data=data)
    return data


@logged(reduce_long_arguments=True)
def update_bot(bot_id: int, new_bot_show: dict) -> BotShow:
    error, data = get_p3cw().request(
        entity='bots',
        action='update',
        action_id=str(bot_id),
        payload=new_bot_show
    )
    utils.verify_no_error(error=error, data=data)
    return BotShow.of(data)


@logged
def get_bots(enabled: bool = None, limit: int = None) -> List[BotShow]:
    payload = {}
    if enabled is not None:
        payload['scope'] = 'enabled' if enabled else 'disabled'
    if limit is not None:
        payload['limit'] = limit
    error, data = get_p3cw().request(
        entity='bots',
        action='',
        payload=payload
    )
    utils.verify_no_error(error=error, data=data)
    return BotShow.of_list(data)


@logged
def get_bot(bot_id: int, include_events: bool = None) -> BotShow:
    """
    /ver1/bots/:bot_id/show
    """
    payload = {}
    if include_events is not None:
        payload['include_events'] = 'true' if include_events else 'false'
    error, data = get_p3cw().request(
        entity='bots',
        action='show',
        action_id=str(bot_id),
        payload=payload
    )
    utils.verify_no_error(error=error, data=data)
    return BotShow.of(data)


@logged
def enable_bot(bot_id: int):
    error, data = get_p3cw().request(
        entity='bots',
        action='enable',
        action_id=str(bot_id)
    )
    utils.verify_no_error(error=error, data=data)
    return data


@logged
def create_bot(bot_model: BotShow) -> BotShow:
    error, data = get_p3cw().request(
        entity='bots',
        action='create_bot',
        payload=bot_model
    )
    utils.verify_no_error(error=error, data=data)
    return BotShow.of(data)


# Accounts

@logged
def get_pie_chart_data(account_id: int) -> List[PieChartDataElement]:
    error, data = get_p3cw().request(
        entity='accounts',
        action='pie_chart_data',
        action_id=str(account_id)
    )
    utils.verify_no_error(error=error, data=data)
    return PieChartDataElement.of_list(data)


@logged
def get_account_balance_chart_data(account_id: int, date_from: str, date_to: str = None):
    """
    :param account_id:
    :param date_from: format YYYY-MM-DD
    :param date_to: format YYYY-MM-DD
    :return:
    """
    payload = {
        'date_from': date_from,
    }
    if date_to is not None:
        payload['date_to'] = date_to

    error, data = get_p3cw().request(
        entity='accounts',
        action='balance_chart_data',
        action_id=str(account_id),
        payload=payload
    )
    utils.verify_no_error(error=error, data=data)
    return data


@logged
def get_market_pairs(market_code: str) -> List[str]:
    error, data = get_p3cw().request(
        entity='accounts',
        action='market_pairs',
        payload={'market_code': market_code}
    )
    utils.verify_no_error(error=error, data=data)
    return data


@logged
def get_accounts() -> List[Account]:
    """
    /ver1/accounts
    :return:
    """
    error, data = get_p3cw().request(
        entity='accounts'
    )
    utils.verify_no_error(error=error, data=data)
    return Account.of_list(data)


@logged
def get_account(account_id: int) -> Account:
    """
    /ver1/accounts/:account_id
    :param account_id:
    :return:
    """
    error, data = get_p3cw().request(
        entity='accounts',
        action='account_info',
        action_id=str(account_id)
    )
    utils.verify_no_error(error=error, data=data)
    return Account.of(data)


# Deals

@logged
def get_deals(bot_id: int = None,
              account_id: int = None,
              limit: int = None,
              scope: str = None,
              offset: int = None,
              forced_mode: str = None) -> List[DealShow]:
    """
    :param bot_id: defaults to all if not specified
    :param account_id: defaults to all if not specified
    :param limit: defaults to 50, max is 1000
    :param scope: should be in [active, finished, completed, cancelled, failed], other defaults to all
    :param offset:
    :param forced_mode: add forced mode real == True, paper == False, no forced mode == None
    :return:
    """
    payload = {}
    if bot_id is not None:
        payload['bot_id'] = str(bot_id)
    if account_id is not None:
        payload['account_id'] = account_id
    if limit is not None:
        payload['limit'] = limit
    if scope is not None:
        payload['scope'] = scope
    if offset is not None:
        payload['offset'] = offset

    additional_headers = {}
    if forced_mode is not None:
        if forced_mode.lower() == 'real':
            additional_headers = get_real_headers()
        elif forced_mode.lower() == 'paper':
            additional_headers = get_paper_headers()
        else:
            logger.warning(f'{forced_mode=} is not known')

    error, data = get_p3cw().request(
        entity='deals',
        action='',
        payload=payload,
        additional_headers=additional_headers
    )
    utils.verify_no_error(error=error, data=data)
    return DealShow.of_list(data)


@logged
def get_all_deals(*args, **kwargs) -> List[DealShow]:
    all_deals = list()
    max_limit = 1000
    kwargs['limit'] = max_limit
    offset = 0
    while True:
        new_deals = get_deals(*args, **kwargs)
        if len(new_deals) == 0:
            return all_deals
        all_deals.extend(new_deals)
        offset += max_limit
        kwargs['offset'] = offset


@logged
def get_deal_market_orders(deal_id: int):
    error, data = get_p3cw().request(
        entity='deals',
        action='market_orders',
        action_id=str(deal_id)
    )
    utils.verify_no_error(error=error, data=data)
    return DealMarketOrder.of_list(data)


def get_paper_headers():
    return {'Forced-Mode': 'paper'}


def get_real_headers():
    return {'Forced-Mode': 'real'}
