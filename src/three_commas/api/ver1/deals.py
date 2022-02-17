from py3cw.request import Py3CW
from models import *


wrapper = Py3CW('', '')


def get():
    """
    /ver1/deals
    User deals (Permission: BOTS_READ, Security: SIGNED)

    :param limit: integer, Limit records. Max: 1_000
    :param offset: integer, Offset records
    :param from: string, Param for a filter by created date
    :param account_id: integer, Account to show bots on. Return all if not specified. Gather this from GET /ver1/accounts
    :param bot_id: integer, Bot show deals on. Return all if not specified
    :param scope: string, active - active deals, finished - finished deals, completed - successfully completed, cancelled - cancelled deals, failed - failed deals, any other value or null (default) - all deals
    :param order: string, values: ['created_at', 'updated_at', 'closed_at', 'profit', 'profit_percentage']
    :param order_direction: string, values: ['asc', 'desc']
    :param base: string, Base currency
    :param quote: string, Quote currency
    """
    error, data = wrapper.request(
        entity='deals',
        action='',
    )
    return ThreeCommasError(error), data


''' This endpoint was not present in the py3cw module
def post_convert_to_smart_trade_by_deal_id(deal_id):
    """
    /ver1/deals/{deal_id}/convert_to_smart_trade
    Convert to smart trade (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    :param deal_id: REQUIRED, integer
    :param stop_bot: boolean
    """
    error, data = wrapper.request(
        entity='deals',
        action='<py3cw_action>',
        action_id=str(deal_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_update_max_safety_orders_by_deal_id(deal_id):
    """
    /ver1/deals/{deal_id}/update_max_safety_orders
    Update max safety orders (Permission: BOTS_WRITE, Security: SIGNED)

    :param max_safety_orders: REQUIRED, integer, New maximum safety orders value
    :param deal_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='deals',
        action='<py3cw_action>',
        action_id=str(deal_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_panic_sell_by_deal_id(deal_id):
    """
    /ver1/deals/{deal_id}/panic_sell
    Panic sell deal (Permission: BOTS_WRITE, Security: SIGNED)

    :param deal_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='deals',
        action='<py3cw_action>',
        action_id=str(deal_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_cancel_by_deal_id(deal_id):
    """
    /ver1/deals/{deal_id}/cancel
    Cancel deal (Permission: BOTS_WRITE, Security: SIGNED)

    :param deal_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='deals',
        action='<py3cw_action>',
        action_id=str(deal_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def patch_update_deal_by_deal_id(deal_id):
    """
    /ver1/deals/{deal_id}/update_deal
    Update deal (Permission: BOTS_WRITE, Security: SIGNED)

    :param deal_id: REQUIRED, integer
    :param take_profit: number, New take profit value
    :param profit_currency: string, values: ['quote_currency', 'base_currency']
    :param take_profit_type: string, base – from base order, total – from total volume
    :param trailing_enabled: boolean
    :param trailing_deviation: number, New trailing deviation value
    :param stop_loss_percentage: number, New stop loss percentage value
    :param max_safety_orders: integer, New max safety orders value
    :param active_safety_orders_count: integer, New active safety orders count value
    :param stop_loss_timeout_enabled: boolean
    :param stop_loss_timeout_in_seconds: integer, StopLoss timeout in seconds if StopLoss timeout enabled
    :param tsl_enabled: boolean, Trailing stop loss enabled
    :param stop_loss_type: string, values: ['stop_loss', 'stop_loss_and_disable_bot']
    :param close_timeout: integer, Close deal after given number of seconds. Must be greater than 60.
    """
    error, data = wrapper.request(
        entity='deals',
        action='<py3cw_action>',
        action_id=str(deal_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_update_tp_by_deal_id(deal_id):
    """
    /ver1/deals/{deal_id}/update_tp
    DEPRECATED, Update take profit condition. Deal status should be bought (Permission: BOTS_WRITE, Security: SIGNED)

    :param new_take_profit_percentage: REQUIRED, number, New take profit value
    :param deal_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='deals',
        action='<py3cw_action>',
        action_id=str(deal_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def get_show_by_deal_id(deal_id):
    """
    /ver1/deals/{deal_id}/show
    Info about specific deal (Permission: BOTS_READ, Security: SIGNED)

    :param deal_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='deals',
        action='<py3cw_action>',
        action_id=str(deal_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_cancel_order_by_deal_id(deal_id):
    """
    /ver1/deals/{deal_id}/cancel_order
    Cancel manual safety orders (Permission: BOTS_WRITE, Security: SIGNED)

    :param order_id: REQUIRED, string, manual safety order id
    :param deal_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='deals',
        action='<py3cw_action>',
        action_id=str(deal_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def get_market_orders_by_deal_id(deal_id):
    """
    /ver1/deals/{deal_id}/market_orders
    Deal safety orders (Permission: BOTS_READ, Security: SIGNED)

    :param deal_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='deals',
        action='<py3cw_action>',
        action_id=str(deal_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_add_funds_by_deal_id(deal_id):
    """
    /ver1/deals/{deal_id}/add_funds
    Adding manual safety order (Permission: BOTS_WRITE, Security: SIGNED)

    :param quantity: REQUIRED, number, safety order quantity
    :param is_market: REQUIRED, boolean, true - use MARKET order, false - use LIMIT order
    :param rate: REQUIRED, number, safety order rate. Required if LIMIT order used
    :param deal_id: REQUIRED, integer
    :param response_type: string, values: ['empty', 'deal', 'market_order']
    """
    error, data = wrapper.request(
        entity='deals',
        action='<py3cw_action>',
        action_id=str(deal_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def get_data_for_adding_funds_by_deal_id(deal_id):
    """
    /ver1/deals/{deal_id}/data_for_adding_funds
    Info required to add funds correctly: available amounts, exchange limitations etc  (Permission: BOTS_READ, Security: SIGNED)

    :param deal_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='deals',
        action='<py3cw_action>',
        action_id=str(deal_id),
    )
    return ThreeCommasError(error), data
'''


