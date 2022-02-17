from py3cw.request import Py3CW
from ...model import *
from ...error import ThreeCommasError
from typing import Tuple


wrapper = Py3CW('', '')


''' This endpoint was not present in the py3cw module
def post_create_simple_sell():
    """
    /ver1/smart_trades/create_simple_sell
    Create SimpleSell (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_create_simple_buy():
    """
    /ver1/smart_trades/create_simple_buy
    Create SimpleBuy (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_create_smart_sell():
    """
    /ver1/smart_trades/create_smart_sell
    Create SmartSale (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_create_smart_cover():
    """
    /ver1/smart_trades/create_smart_cover
    Create SmartCover (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_create_smart_trade():
    """
    /ver1/smart_trades/create_smart_trade
    Create SmartTrade (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def get():
    """
    /ver1/smart_trades
    Get SmartTrade history (Permission: SMART_TRADE_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_cancel_order_by_id(smart_trade_id):
    """
    /ver1/smart_trades/{smart_trade_id}/cancel_order
    Manual cancel order (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_add_funds_by_id(smart_trade_id):
    """
    /ver1/smart_trades/{smart_trade_id}/add_funds
    Smart Trade add funds (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_step_panic_sell_by_id(smart_trade_id):
    """
    /ver1/smart_trades/{smart_trade_id}/step_panic_sell
    Step panic sell (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def patch_update_by_id(smart_trade_id):
    """
    /ver1/smart_trades/{smart_trade_id}/update
    Edit SmartTrade/SmartSale/SmartCover (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_cancel_by_id(smart_trade_id):
    """
    /ver1/smart_trades/{smart_trade_id}/cancel
    Cancel SmartTrade (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_panic_sell_by_id(smart_trade_id):
    """
    /ver1/smart_trades/{smart_trade_id}/panic_sell
    Sell currency immediately (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_force_start_by_id(smart_trade_id):
    """
    /ver1/smart_trades/{smart_trade_id}/force_start
    Process BuyStep immediately  (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_force_process_by_id(smart_trade_id):
    """
    /ver1/smart_trades/{smart_trade_id}/force_process
    Refresh SmartTrade state (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def get_show_by_id(smart_trade_id):
    """
    /ver1/smart_trades/{smart_trade_id}/show
    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasError(error), data
'''


