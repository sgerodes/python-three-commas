from typing import List
import logging
from ...sys_utils import logged, with_py3cw
from ... import utils
from ...model import Deal as DealShow, DealMarketOrder


logger = logging.getLogger(__name__)


@logged
@with_py3cw
def get_deals(py3cw,
              bot_id: int = None,
              account_id: int = None,
              limit: int = None,
              scope: str = None,
              offset: int = None) -> List[DealShow]:
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
    error, data = py3cw.request(
        entity='deals',
        action='',
        payload=payload
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
@with_py3cw
def get_deal_market_orders(py3cw, deal_id: int):
    error, data = py3cw.request(
        entity='deals',
        action='market_orders',
        action_id=str(deal_id)
    )
    utils.verify_no_error(error=error, data=data)
    return DealMarketOrder.of_list(data)
