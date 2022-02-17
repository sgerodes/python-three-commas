from py3cw.request import Py3CW
from models import *


wrapper = Py3CW('', '')


def post():
    """
    /v2/smart_trades
    Create smart trade v2 (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    :param account_id: REQUIRED, integer, id from GET /ver1/accounts
    :param pair: REQUIRED, string
    :param leverage[enabled]: REQUIRED, boolean
    :param position[type]: REQUIRED, string, values: ['buy', 'sell']
    :param position[order_type]: REQUIRED, string, values: ['market', 'limit', 'conditional']
    :param position[units][value]: REQUIRED, number, Amount of units to buy
    :param position[price][value]: REQUIRED, number, Price for limit order
    :param position[conditional][price][value]: REQUIRED, number, Conditional trigger price
    :param position[conditional][order_type]: REQUIRED, string, values: ['market', 'limit']
    :param position[conditional][trailing][enabled]: REQUIRED, boolean
    :param position[conditional][trailing][percent]: REQUIRED, number, Should be 100% in the sum of all steps
    :param take_profit[enabled]: REQUIRED, boolean
    :param take_profit[steps][][order_type]: REQUIRED, array, market, limit
    :param take_profit[steps][][volume]: REQUIRED, array
    :param take_profit[steps][][price][type]: REQUIRED, array, bid, ask, last
    :param take_profit[steps][][trailing][enabled]: REQUIRED, array
    :param take_profit[steps][][trailing][percent]: REQUIRED, array
    :param stop_loss[enabled]: REQUIRED, boolean
    :param stop_loss[order_type]: REQUIRED, string, values: ['market', 'limit']
    :param stop_loss[price][value]: REQUIRED, number, Price for limit order
    :param stop_loss[conditional][price][type]: REQUIRED, string, values: ['bid', 'ask', 'last']
    :param stop_loss[conditional][trailing][enabled]: REQUIRED, boolean
    :param stop_loss[timeout][enabled]: REQUIRED, boolean
    :param stop_loss[timeout][value]: REQUIRED, integer
    :param instant: boolean, true for Simple Buy and Simple Sell
    :param skip_enter_step: boolean, true only for Smart Sell
    :param note: string
    :param leverage[type]: string, values: ['custom', 'cross', 'isolated']
    :param leverage[value]: integer, Cross leverage value
    :param position[conditional][price][type]: string, values: ['bid', 'ask', 'last'], By default ask for long, bid for short
    :param take_profit[steps][][price][value]: array, only if position has no trailing or position trailing is finished
    :param take_profit[steps][][price][percent]: array, only if position has trailing and position trailing is not finished
    :param stop_loss[breakeven]: boolean
    :param stop_loss[conditional][price][value]: number, if position has no trailing or position trailing is finished
    :param stop_loss[conditional][price][percent]: number, only if position has trailing and position trailing is not finished
    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='new',
    )
    return ThreeCommasError(error), data


def patch_by_id(id):
    """
    /v2/smart_trades/{id}
    Update smart trade v2 (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    :param leverage[enabled]: REQUIRED, boolean
    :param position[units][value]: REQUIRED, number, Amount of units to buy
    :param position[price][value]: REQUIRED, number, Price for limit order
    :param position[conditional][price][value]: REQUIRED, number, Conditional trigger price
    :param position[conditional][order_type]: REQUIRED, string, values: ['market', 'limit']
    :param position[conditional][trailing][enabled]: REQUIRED, boolean
    :param position[conditional][trailing][percent]: REQUIRED, number
    :param take_profit[enabled]: REQUIRED, boolean
    :param take_profit[steps][][order_type]: REQUIRED, array
    :param take_profit[steps][][volume]: REQUIRED, array
    :param take_profit[steps][][price][type]: REQUIRED, array
    :param take_profit[steps][][trailing][enabled]: REQUIRED, array
    :param take_profit[steps][][trailing][percent]: REQUIRED, array
    :param stop_loss[enabled]: REQUIRED, boolean
    :param stop_loss[order_type]: REQUIRED, string, values: ['market', 'limit']
    :param stop_loss[price][value]: REQUIRED, number, Price for limit order
    :param stop_loss[conditional][price][type]: REQUIRED, string, values: ['bid', 'ask', 'last']
    :param stop_loss[conditional][trailing][enabled]: REQUIRED, boolean
    :param stop_loss[timeout][enabled]: REQUIRED, boolean
    :param stop_loss[timeout][value]: REQUIRED, integer
    :param id: REQUIRED, integer
    :param leverage[type]: string, values: ['custom', 'cross', 'isolated']
    :param leverage[value]: integer, Cross leverage value
    :param position[conditional][price][type]: string, values: ['bid', 'ask', 'last'], By default ask for long, bid for short
    :param take_profit[steps][][price][value]: array
    :param take_profit[steps][][price][percent]: array
    :param stop_loss[breakeven]: boolean
    :param stop_loss[conditional][price][value]: number, Trigger price
    :param stop_loss[conditional][price][percent]: number
    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='update',
        action_id=str(id),
    )
    return ThreeCommasError(error), data


''' This endpoint was not present in the py3cw module
def post_reduce_funds_by_id(id):
    """
    /v2/smart_trades/{id}/reduce_funds
    Reduce funds for smart trade v2 (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    :param order_type: REQUIRED, string, values: ['market', 'limit']
    :param units[value]: REQUIRED, number, Amount of units to buy
    :param price[value]: REQUIRED, number, Price for limit order
    :param id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='<py3cw_action>',
        action_id=str(id),
    )
    return ThreeCommasError(error), data
'''


def post_add_funds_by_id(id):
    """
    /v2/smart_trades/{id}/add_funds
    Average for smart trade v2 (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    :param order_type: REQUIRED, string, values: ['market', 'limit']
    :param units[value]: REQUIRED, number, Amount of units to buy
    :param price[value]: REQUIRED, number, Price for limit order
    :param id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='add_funds',
        action_id=str(id),
    )
    return ThreeCommasError(error), data


def post_close_by_market_by_id(id):
    """
    /v2/smart_trades/{id}/close_by_market
    Close by market smart trade v2 (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    :param id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='close_by_market',
        action_id=str(id),
    )
    return ThreeCommasError(error), data


def post_force_start_by_id(id):
    """
    /v2/smart_trades/{id}/force_start
    Force start smart trade v2 (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    :param id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='force_start',
        action_id=str(id),
    )
    return ThreeCommasError(error), data


def post_force_process_by_id(id):
    """
    /v2/smart_trades/{id}/force_process
    Process smart trade v2 (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    :param id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='force_process',
        action_id=str(id),
    )
    return ThreeCommasError(error), data


def post_set_note_by_id(id):
    """
    /v2/smart_trades/{id}/set_note
    Set note to smart trade v2 (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    :param note: REQUIRED, string
    :param id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='set_note',
        action_id=str(id),
    )
    return ThreeCommasError(error), data


''' This endpoint was not present in the py3cw module
def get_trades_by_smart_trade_id(smart_trade_id):
    """
    /v2/smart_trades/{smart_trade_id}/trades
    Get smart trade v2 trades (Permission: SMART_TRADE_READ, Security: SIGNED)

    :param smart_trade_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_trades_close_by_market_by_smart_trade_id(smart_trade_id, id):
    """
    /v2/smart_trades/{smart_trade_id}/trades/{id}/close_by_market
    Panic close trade by market (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    :param smart_trade_id: REQUIRED, integer
    :param id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
        action_sub_id=str(id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def delete_trades_by_smart_trade_id(smart_trade_id, id):
    """
    /v2/smart_trades/{smart_trade_id}/trades/{id}
    Cancel trade (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    :param smart_trade_id: REQUIRED, integer
    :param id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
        action_sub_id=str(id),
    )
    return ThreeCommasError(error), data
'''


