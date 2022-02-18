from py3cw.request import Py3CW
from ...model import *
from ...error import ThreeCommasApiError
from typing import Tuple, List
import logging
from ...sys_utils import logged, with_py3cw, Py3cwClosure


logger = logging.getLogger(__name__)
wrapper: Py3cwClosure = None


''' This endpoint was not present in the py3cw module
@logged
@with_py3cw
def post_create_simple_sell():
    """
    POST /ver1/smart_trades/create_simple_sell
    Create SimpleSell (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
    )
    return ThreeCommasApiError(error), data
'''


''' This endpoint was not present in the py3cw module
@logged
@with_py3cw
def post_create_simple_buy():
    """
    POST /ver1/smart_trades/create_simple_buy
    Create SimpleBuy (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
    )
    return ThreeCommasApiError(error), data
'''


''' This endpoint was not present in the py3cw module
@logged
@with_py3cw
def post_create_smart_sell():
    """
    POST /ver1/smart_trades/create_smart_sell
    Create SmartSale (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
    )
    return ThreeCommasApiError(error), data
'''


''' This endpoint was not present in the py3cw module
@logged
@with_py3cw
def post_create_smart_cover():
    """
    POST /ver1/smart_trades/create_smart_cover
    Create SmartCover (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
    )
    return ThreeCommasApiError(error), data
'''


''' This endpoint was not present in the py3cw module
@logged
@with_py3cw
def post_create_smart_trade():
    """
    POST /ver1/smart_trades/create_smart_trade
    Create SmartTrade (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
    )
    return ThreeCommasApiError(error), data
'''


''' This endpoint was not present in the py3cw module
@logged
@with_py3cw
def get():
    """
    GET /ver1/smart_trades
    Get SmartTrade history (Permission: SMART_TRADE_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
    )
    return ThreeCommasApiError(error), data
'''


''' This endpoint was not present in the py3cw module
@logged
@with_py3cw
def post_cancel_order_by_id(smart_trade_id):
    """
    POST /ver1/smart_trades/{smart_trade_id}/cancel_order
    Manual cancel order (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasApiError(error), data
'''


''' This endpoint was not present in the py3cw module
@logged
@with_py3cw
def post_add_funds_by_id(smart_trade_id):
    """
    POST /ver1/smart_trades/{smart_trade_id}/add_funds
    Smart Trade add funds (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasApiError(error), data
'''


''' This endpoint was not present in the py3cw module
@logged
@with_py3cw
def post_step_panic_sell_by_id(smart_trade_id):
    """
    POST /ver1/smart_trades/{smart_trade_id}/step_panic_sell
    Step panic sell (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasApiError(error), data
'''


''' This endpoint was not present in the py3cw module
@logged
@with_py3cw
def patch_update_by_id(smart_trade_id):
    """
    PATCH /ver1/smart_trades/{smart_trade_id}/update
    Edit SmartTrade/SmartSale/SmartCover (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasApiError(error), data
'''


''' This endpoint was not present in the py3cw module
@logged
@with_py3cw
def post_cancel_by_id(smart_trade_id):
    """
    POST /ver1/smart_trades/{smart_trade_id}/cancel
    Cancel SmartTrade (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasApiError(error), data
'''


''' This endpoint was not present in the py3cw module
@logged
@with_py3cw
def post_panic_sell_by_id(smart_trade_id):
    """
    POST /ver1/smart_trades/{smart_trade_id}/panic_sell
    Sell currency immediately (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasApiError(error), data
'''


''' This endpoint was not present in the py3cw module
@logged
@with_py3cw
def post_force_start_by_id(smart_trade_id):
    """
    POST /ver1/smart_trades/{smart_trade_id}/force_start
    Process BuyStep immediately  (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasApiError(error), data
'''


''' This endpoint was not present in the py3cw module
@logged
@with_py3cw
def post_force_process_by_id(smart_trade_id):
    """
    POST /ver1/smart_trades/{smart_trade_id}/force_process
    Refresh SmartTrade state (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasApiError(error), data
'''


''' This endpoint was not present in the py3cw module
@logged
@with_py3cw
def get_show_by_id(smart_trade_id):
    """
    GET /ver1/smart_trades/{smart_trade_id}/show
    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasApiError(error), data
'''


