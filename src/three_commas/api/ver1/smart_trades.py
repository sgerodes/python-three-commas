from py3cw.request import Py3CW
from models import *


wrapper = Py3CW('', '')


''' This endpoint was not present in the py3cw module
def post_create_simple_sell():
    """
    /ver1/smart_trades/create_simple_sell
    Create SimpleSell (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    :param account_id: REQUIRED, integer, id from GET /ver1/accounts
    :param pair: REQUIRED, string
    :param units_to_buy: REQUIRED, number, Amount of units to buy
    :param buy_price: REQUIRED, number
    :param buy_method: REQUIRED, string, values: ['limit', 'market', 'conditional']
    :param conditional_limit_price: number, Order price for conditional SimpleSell with limit order
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

    :param account_id: REQUIRED, integer, id from GET /ver1/accounts
    :param pair: REQUIRED, string
    :param units_to_buy: REQUIRED, number, Amount of units to buy
    :param buy_price: REQUIRED, number
    :param buy_method: REQUIRED, string, values: ['limit', 'market', 'conditional']
    :param conditional_limit_price: number, Order price for conditional SimpleBuy with limit order
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

    :param account_id: REQUIRED, integer, id from GET /ver1/accounts
    :param pair: REQUIRED, string
    :param units_to_buy: REQUIRED, number, Bought amount
    :param average_buy_price: REQUIRED, number, Bought price
    :param take_profit_enabled: REQUIRED, boolean
    :param take_profit_step_orders[percent]: REQUIRED, array, Required if take_profit_step_orders
    :param take_profit_step_orders[price_method]: REQUIRED, array, Required if take_profit_step_orders
    :param stop_loss_enabled: REQUIRED, boolean
    :param take_profit_type: string, values: ['classic', 'step_sell'], Required if take_profit_enabled. classic - common take profit, step_sell - step sell take profit
    :param take_profit_price_condition: number, Required if take_profit_type = classic
    :param take_profit_percentage_condition: number, Required if take_profit_type = classic AND trailing_buy_enabled. Must be positive
    :param take_profit_step_orders[price]: array, Required if take_profit_step_orders
    :param take_profit_step_orders[price_percentage]: array, Required if take_profit_step_orders AND trailing_buy_enabled. Must be positive
    :param take_profit_price_method: string, values: ['bid', 'ask', 'last'], Price type for take profit(bid,asl,last)
    :param take_profit_sell_method: string, values: ['market', 'limit']
    :param take_profit_sell_order_price: number, Required if limit
    :param trailing_take_profit: boolean
    :param trailing_take_profit_step: number, Required if trailing_take_profit
    :param stop_loss_price_condition: number, Required if stop_loss_enabled
    :param stop_loss_percentage_condition: number, Required if stop_loss_enabled AND trailing_buy_enabled. Must be negative
    :param stop_loss_price_method: string, values: ['bid', 'ask', 'last'], Price type for stop loss
    :param stop_loss_sell_method: string, values: ['market', 'limit']
    :param stop_loss_sell_order_price: number, Required if limit
    :param trailing_stop_loss: boolean
    :param stop_loss_timeout_enabled: boolean
    :param stop_loss_timeout_seconds: integer, Timeout in seconds
    :param note: string
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

    :param account_id: REQUIRED, integer, id from GET /ver1/accounts
    :param pair: REQUIRED, string
    :param units_to_buy: REQUIRED, number, Amount of units to buy
    :param buy_price: REQUIRED, number
    :param take_profit_enabled: REQUIRED, boolean
    :param take_profit_step_orders[percent]: REQUIRED, array, Required if take_profit_step_orders
    :param take_profit_step_orders[price_method]: REQUIRED, array, Required if take_profit_step_orders
    :param stop_loss_enabled: REQUIRED, boolean
    :param conditional_limit_price: number, Order price for conditional SmartCover with limit order
    :param buy_method: string, values: ['limit', 'market', 'conditional']
    :param trailing_buy_enabled: boolean
    :param trailing_buy_step: number, Required if trailing_buy_enabled
    :param take_profit_type: string, values: ['classic', 'step_sell'], Required if take_profit_enabled. classic - common take profit, step_sell - step sell take profit
    :param take_profit_price_condition: number, Required if take_profit_type = classic
    :param take_profit_percentage_condition: number, Required if take_profit_type = classic AND trailing_buy_enabled. Must be negative
    :param take_profit_step_orders[price]: array, Required if take_profit_step_orders
    :param take_profit_step_orders[price_percentage]: array, Required if take_profit_step_orders AND trailing_buy_enabled. Must be negative
    :param take_profit_price_method: string, values: ['bid', 'ask', 'last'], Price type for take profit
    :param take_profit_sell_method: string, values: ['market', 'limit']
    :param take_profit_sell_order_price: number, Required if limit
    :param trailing_take_profit: boolean
    :param trailing_take_profit_step: number, Required if trailing_take_profit
    :param stop_loss_price_condition: number, Required if stop_loss_enabled
    :param stop_loss_percentage_condition: number, Required if stop_loss_enabled AND trailing_buy_enabled. Must Be positive
    :param stop_loss_price_method: string, values: ['bid', 'ask', 'last'], Price type for stop loss
    :param stop_loss_sell_method: string, values: ['market', 'limit']
    :param stop_loss_sell_order_price: number, Required if limit
    :param trailing_stop_loss: boolean
    :param stop_loss_timeout_enabled: boolean
    :param stop_loss_timeout_seconds: integer, timeout in seconds
    :param note: string
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

    :param account_id: REQUIRED, integer, id from GET /ver1/accounts
    :param pair: REQUIRED, string
    :param units_to_buy: REQUIRED, number, Amount of units to buy
    :param buy_price: REQUIRED, number
    :param take_profit_enabled: REQUIRED, boolean
    :param take_profit_step_orders[percent]: REQUIRED, array, Required if take_profit_step_orders
    :param take_profit_step_orders[price_method]: REQUIRED, array, Required if take_profit_step_orders
    :param stop_loss_enabled: REQUIRED, boolean
    :param conditional_limit_price: number, Order price for conditional SmartTrade with limit order
    :param buy_method: string, values: ['limit', 'market', 'conditional']
    :param trailing_buy_enabled: boolean
    :param trailing_buy_step: number, Required if trailing_buy_enabled
    :param take_profit_type: string, values: ['classic', 'step_sell'], Required if take_profit_enabled. classic - common take profit, step_sell - step sell take profit
    :param take_profit_price_condition: number, Required if take_profit_type = classic
    :param take_profit_percentage_condition: number, Required if take_profit_type = classic AND trailing_buy_enabled. Must be positive
    :param take_profit_step_orders[price]: array, Required if take_profit_step_orders
    :param take_profit_step_orders[price_percentage]: array, Required if take_profit_step_orders AND trailing_buy_enabled. Must be positive
    :param take_profit_price_method: string, values: ['bid', 'ask', 'last'], Price type for take profit
    :param take_profit_sell_method: string, values: ['market', 'limit']
    :param take_profit_sell_order_price: number, Required if limit
    :param trailing_take_profit: boolean
    :param trailing_take_profit_step: number, Required if trailing_take_profit
    :param stop_loss_price_condition: number, Required if stop_loss_enabled
    :param stop_loss_percentage_condition: number, Required if stop_loss_enabled AND trailing_buy_enabled. Must be negative
    :param stop_loss_price_method: string, values: ['bid', 'ask', 'last'], Price type for stop loss
    :param stop_loss_sell_method: string, values: ['market', 'limit']
    :param stop_loss_sell_order_price: number, Required if limit
    :param trailing_stop_loss: boolean
    :param stop_loss_timeout_enabled: boolean
    :param stop_loss_timeout_seconds: integer, timeout in seconds
    :param note: string
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

    :param limit: integer, Limit records
    :param offset: integer, Offset records
    :param account_id: integer, Account to show smart_trades on. Pass null (default) - show all
    :param scope: string, active - show only active trades, finished - history of closed trades, cancelled - cancelled trades, failed - failed trades, any other value or null (default) - all trades
    :param type: string, SmartTrade::SmartSale , SmartTrade::Classic , SmartTrade::ConditionalBuy
    :param order: string, values: ['created_at', 'closed_at', 'updated_at']
    :param pairs: array, Array of pairs
    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_cancel_order_by_smart_trade_id(smart_trade_id):
    """
    /ver1/smart_trades/{smart_trade_id}/cancel_order
    Manual cancel order (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    :param step_id: REQUIRED, string, SmartTrade step id to cancel
    :param smart_trade_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_add_funds_by_smart_trade_id(smart_trade_id):
    """
    /ver1/smart_trades/{smart_trade_id}/add_funds
    Smart Trade add funds (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    :param quantity: REQUIRED, number, buy order quantity
    :param is_market: REQUIRED, boolean, true - use MARKET order, false - use LIMIT order
    :param rate: REQUIRED, number, buy order rate. Required if LIMIT order used
    :param smart_trade_id: REQUIRED, integer
    :param response_type: string, values: ['smart_trade', 'empty', 'order', 'step']
    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_step_panic_sell_by_smart_trade_id(smart_trade_id):
    """
    /ver1/smart_trades/{smart_trade_id}/step_panic_sell
    Step panic sell (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    :param step_id: REQUIRED, integer
    :param smart_trade_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def patch_update_by_smart_trade_id(smart_trade_id):
    """
    /ver1/smart_trades/{smart_trade_id}/update
    Edit SmartTrade/SmartSale/SmartCover (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    :param take_profit_enabled: REQUIRED, boolean
    :param take_profit_step_orders[percent]: REQUIRED, array, Required if take_profit_step_orders
    :param take_profit_step_orders[position]: REQUIRED, array, Required if take_profit_step_orders
    :param take_profit_step_orders[price_method]: REQUIRED, array, Required if take_profit_step_orders
    :param stop_loss_enabled: REQUIRED, boolean
    :param smart_trade_id: REQUIRED, integer
    :param buy_price: number, Available if Conditional SmartTrade
    :param conditional_limit_price: number
    :param average_buy_price: number, Available if SmartSale
    :param trailing_buy_enabled: boolean, Available if Conditional SmartTrade
    :param trailing_buy_step: number, Available if trailing_buy_enabled
    :param take_profit_type: string, values: ['classic', 'step_sell'], Required if take_profit_enabled. classic - common take profit, step_sell - step sell take profit
    :param take_profit_price_condition: number, Required if take_profit_type = classic
    :param take_profit_percentage_condition: number, Required if take_profit_type = classic AND trailing_buy_enabled
    :param take_profit_step_orders[price]: array, Required if take_profit_step_orders
    :param take_profit_step_orders[price_percentage]: array, Required if take_profit_step_orders AND trailing_buy_enabled
    :param take_profit_price_method: string, values: ['bid', 'ask', 'last'], Price type for take profit(bid,asl,last)
    :param take_profit_sell_method: string, values: ['market', 'limit']
    :param take_profit_sell_order_price: number, Required if limit
    :param trailing_take_profit: boolean
    :param trailing_take_profit_step: number, Required if trailing_take_profit
    :param stop_loss_price_condition: number, Required if stop_loss_enabled
    :param stop_loss_percentage_condition: number, Required if stop_loss_enabled AND trailing_buy_enabled
    :param stop_loss_price_method: string, values: ['bid', 'ask', 'last'], Price type for stop loss
    :param stop_loss_sell_method: string, values: ['market', 'limit']
    :param stop_loss_sell_order_price: number, Required if limit
    :param trailing_stop_loss: boolean
    :param stop_loss_timeout_enabled: boolean
    :param stop_loss_timeout_seconds: integer, Timeout in seconds
    :param note: string
    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_cancel_by_smart_trade_id(smart_trade_id):
    """
    /ver1/smart_trades/{smart_trade_id}/cancel
    Cancel SmartTrade (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    :param smart_trade_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_panic_sell_by_smart_trade_id(smart_trade_id):
    """
    /ver1/smart_trades/{smart_trade_id}/panic_sell
    Sell currency immediately (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    :param smart_trade_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_force_start_by_smart_trade_id(smart_trade_id):
    """
    /ver1/smart_trades/{smart_trade_id}/force_start
    Process BuyStep immediately  (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    :param smart_trade_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_force_process_by_smart_trade_id(smart_trade_id):
    """
    /ver1/smart_trades/{smart_trade_id}/force_process
    Refresh SmartTrade state (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    :param smart_trade_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def get_show_by_smart_trade_id(smart_trade_id):
    """
    /ver1/smart_trades/{smart_trade_id}/show
    :param smart_trade_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasError(error), data
'''


