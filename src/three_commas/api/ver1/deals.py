from py3cw.request import Py3CW
from ...model import *
from ...error import ThreeCommasApiError
from typing import Tuple, List
import logging
from ...sys_utils import logged, with_py3cw, Py3cwClosure


logger = logging.getLogger(__name__)
wrapper: Py3cwClosure = None


@logged
@with_py3cw
def get():
    """
    GET /ver1/deals
    User deals (Permission: BOTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='deals',
        action='',
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def post_convert_to_smart_trade_by_id(deal_id):
    """
    POST /ver1/deals/{deal_id}/convert_to_smart_trade
    Convert to smart trade (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='deals',
        action='convert_to_smart_trade',
        action_id=str(deal_id),
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def post_update_max_safety_orders_by_id(deal_id):
    """
    POST /ver1/deals/{deal_id}/update_max_safety_orders
    Update max safety orders (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='deals',
        action='update_max_safety_orders',
        action_id=str(deal_id),
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def post_panic_sell_by_id(deal_id):
    """
    POST /ver1/deals/{deal_id}/panic_sell
    Panic sell deal (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='deals',
        action='panic_sell',
        action_id=str(deal_id),
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def post_cancel_by_id(deal_id):
    """
    POST /ver1/deals/{deal_id}/cancel
    Cancel deal (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='deals',
        action='cancel',
        action_id=str(deal_id),
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def patch_update_deal_by_id(deal_id):
    """
    PATCH /ver1/deals/{deal_id}/update_deal
    Update deal (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='deals',
        action='update_deal',
        action_id=str(deal_id),
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def post_update_tp_by_id(deal_id):
    """
    POST /ver1/deals/{deal_id}/update_tp
    DEPRECATED, Update take profit condition. Deal status should be bought (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='deals',
        action='update_tp',
        action_id=str(deal_id),
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def get_show_by_id(deal_id):
    """
    GET /ver1/deals/{deal_id}/show
    Info about specific deal (Permission: BOTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='deals',
        action='show',
        action_id=str(deal_id),
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def post_cancel_order_by_id(deal_id):
    """
    POST /ver1/deals/{deal_id}/cancel_order
    Cancel manual safety orders (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='deals',
        action='cancel_order',
        action_id=str(deal_id),
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def get_market_orders_by_id(deal_id):
    """
    GET /ver1/deals/{deal_id}/market_orders
    Deal safety orders (Permission: BOTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='deals',
        action='market_orders',
        action_id=str(deal_id),
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def post_add_funds_by_id(deal_id):
    """
    POST /ver1/deals/{deal_id}/add_funds
    Adding manual safety order (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='deals',
        action='add_funds',
        action_id=str(deal_id),
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def get_data_for_adding_funds_by_id(deal_id):
    """
    GET /ver1/deals/{deal_id}/data_for_adding_funds
    Info required to add funds correctly: available amounts, exchange limitations etc  (Permission: BOTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='deals',
        action='data_for_adding_funds',
        action_id=str(deal_id),
    )
    return ThreeCommasApiError(error), data


