from py3cw.request import Py3CW
from models import *


wrapper = Py3CW('', '')


def get_strategy_list():
    """
    /ver1/bots/strategy_list
    Available strategy list for bot (Permission: BOTS_READ, Security: SIGNED)

    :param account_id: integer, id from GET /ver1/accounts
    :param type: string, values: ['simple', 'composite']
    :param strategy: string, values: ['long', 'short']
    """
    error, data = wrapper.request(
        entity='bots',
        action='strategy_list',
    )
    return ThreeCommasError(error), data


def get_pairs_black_list():
    """
    /ver1/bots/pairs_black_list
    Black List for bot pairs (Permission: BOTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='bots',
        action='pairs_black_list',
    )
    return ThreeCommasError(error), data


def post_update_pairs_black_list():
    """
    /ver1/bots/update_pairs_black_list
    Create or Update pairs BlackList for bots (Permission: BOTS_WRITE, Security: SIGNED)

    :param pairs: REQUIRED, array
    """
    error, data = wrapper.request(
        entity='bots',
        action='update_pairs_black_list',
    )
    return ThreeCommasError(error), data


def post_create_bot():
    """
    /ver1/bots/create_bot
    Create bot (Permission: BOTS_WRITE, Security: SIGNED)

    :param name: REQUIRED, string
    :param account_id: REQUIRED, integer, id from GET /ver1/accounts
    :param pairs: REQUIRED, array, Pass single pair to create SingleBot or any other number of pairs to create MultiBot
    :param base_order_volume: REQUIRED, number, Base order size
    :param take_profit: REQUIRED, number, Target profit(percentage)
    :param safety_order_volume: REQUIRED, number, Safety trade size
    :param martingale_volume_coefficient: REQUIRED, number
    :param martingale_step_coefficient: REQUIRED, number
    :param max_safety_orders: REQUIRED, integer, Max safety trades count
    :param active_safety_orders_count: REQUIRED, integer, Max active safety trades count
    :param safety_order_step_percentage: REQUIRED, number, Price deviation to open safety trades(percentage)
    :param take_profit_type: REQUIRED, string, values: ['base', 'total'], Percentage: base – from base order, total – from total volume
    :param strategy_list: REQUIRED, array, For manual signals: [{"strategy":"manual"}] or []<br>
                                                        For non-stop(1 pair only): [{"strategy":"nonstop"}]<br>
                                                        QFL: {"options": {"type": "original"}, {"percent": 3}, "strategy": "qfl"}] <br>
                                                        TradingView: [{"options": {"time": "5m", "type": "buy_or_strong_buy"}, "strategy": "trading_view"} 
    :param max_active_deals: integer
    :param base_order_volume_type: string, values: ['quote_currency', 'base_currency', 'percent', 'xbt'], base order volume currency
    :param safety_order_volume_type: string, values: ['quote_currency', 'base_currency', 'percent', 'xbt'], safety order volume currency
    :param stop_loss_percentage: number
    :param cooldown: number
    :param trailing_enabled: boolean, Enable trailing take profit. Binance only.
    :param trailing_deviation: number, required if trailing_enabled
    :param btc_price_limit: number
    :param strategy: string, values: ['short', 'long']
    :param leverage_type: string, values: ['custom', 'cross', 'not_specified', 'isolated'], Used for Bitmex bots only
    :param leverage_custom_value: number, required if leverage_type is isolated
    :param min_price: number, minimum price to open deal
    :param max_price: number, maximum price to open deal
    :param stop_loss_timeout_enabled: boolean
    :param stop_loss_timeout_in_seconds: integer, StopLoss timeout in seconds if StopLoss timeout enabled
    :param min_volume_btc_24h: number
    :param tsl_enabled: boolean, Enable trailing stop loss. Bitmex only.
    :param deal_start_delay_seconds: integer, Deal start delay in seconds
    :param profit_currency: string, values: ['quote_currency', 'base_currency'], Take profit currency
    :param start_order_type: string, values: ['limit', 'market']
    :param stop_loss_type: string, values: ['stop_loss', 'stop_loss_and_disable_bot']
    :param disable_after_deals_count: integer, Bot will be disabled after opening this number of deals
    :param allowed_deals_on_same_pair: integer, Allow specific number of deals on the same pair. Multibot only.
    :param close_deals_timeout: integer, Close bot deals after given number of seconds. Must be greater than 60.
    """
    error, data = wrapper.request(
        entity='bots',
        action='create_bot',
    )
    return ThreeCommasError(error), data


def get():
    """
    /ver1/bots
    User bots (Permission: BOTS_READ, Security: SIGNED)

    :param limit: integer, Limit records. Max: 100
    :param offset: integer, Offset records
    :param from: string, Param for a filter by created date
    :param account_id: integer, Account to show bots on. Return all if not specified. Gather this from GET /ver1/accounts
    :param scope: string, values: ['enabled', 'disabled']
    :param strategy: string, values: ['long', 'short']
    :param sort_by: string, values: ['profit', 'created_at', 'updated_at']
    :param sort_direction: string, values: ['asc', 'desc']
    :param quote: string, Quote currency
    """
    error, data = wrapper.request(
        entity='bots',
        action='',
    )
    return ThreeCommasError(error), data


def get_stats():
    """
    /ver1/bots/stats
    Get bot stats (Permission: BOTS_READ, Security: SIGNED)

    :param account_id: integer, Account to show on. Null - show for all. Gather this from GET /ver1/accounts
    :param bot_id: integer, Bots to show on. Null - show for all
    """
    error, data = wrapper.request(
        entity='bots',
        action='stats',
    )
    return ThreeCommasError(error), data


''' This endpoint was not present in the py3cw module
def post_copy_and_create_by_bot_id(bot_id):
    """
    /ver1/bots/{bot_id}/copy_and_create
    POST /bots/:id/copy_and_create. Permission: BOTS_WRITE, Security: SIGNED

    :param name: REQUIRED, string
    :param secret: REQUIRED, string
    :param bot_id: REQUIRED, integer
    :param amount: number, Max amount for bot usage (Based on current rate)
    """
    error, data = wrapper.request(
        entity='bots',
        action='<py3cw_action>',
        action_id=str(bot_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def patch_update_by_bot_id(bot_id):
    """
    /ver1/bots/{bot_id}/update
    Edit bot (Permission: BOTS_WRITE, Security: SIGNED)

    :param name: REQUIRED, string
    :param pairs: REQUIRED, array
    :param base_order_volume: REQUIRED, number, Base order size
    :param take_profit: REQUIRED, number, Target profit(percentage)
    :param safety_order_volume: REQUIRED, number, Safety trade size
    :param martingale_volume_coefficient: REQUIRED, number
    :param martingale_step_coefficient: REQUIRED, number
    :param max_safety_orders: REQUIRED, integer, Max safety trades count
    :param active_safety_orders_count: REQUIRED, integer, Max active safety trades count
    :param safety_order_step_percentage: REQUIRED, number, Price deviation to open safety trades(percentage)
    :param take_profit_type: REQUIRED, string, values: ['total', 'base'], Percentage: base – from base order, total – from total volume
    :param strategy_list: REQUIRED, array, For manual signals: [{"strategy":"manual"}] or []<br>
                                                        For non-stop(1 pair only): [{"strategy":"nonstop"}]<br>
                                                        QFL: {"options": {"type": "original"}, {"percent": 3}, "strategy": "qfl"}] <br>
                                                        TradingView: [{"options": {"time": "5m", "type": "buy_or_strong_buy", "strategy": "trading_view"} 
    :param bot_id: REQUIRED, integer
    :param max_active_deals: integer
    :param base_order_volume_type: string, values: ['quote_currency', 'base_currency', 'percent', 'xbt'], base order volume currency
    :param safety_order_volume_type: string, values: ['quote_currency', 'base_currency', 'percent', 'xbt'], safety order volume currency
    :param stop_loss_percentage: number
    :param cooldown: number
    :param trailing_enabled: boolean, Enable trailing take profit. Binance only.
    :param trailing_deviation: number, required if trailing_enabled
    :param btc_price_limit: number
    :param leverage_type: string, values: ['custom', 'cross', 'not_specified', 'isolated'], Used for Bitmex bots only
    :param leverage_custom_value: number, required if leverage_type is isolated
    :param min_price: number, minimum price to open deal
    :param max_price: number, maximum price to open deal
    :param stop_loss_timeout_enabled: boolean
    :param stop_loss_timeout_in_seconds: integer, StopLoss timeout in seconds if StopLoss timeout enabled
    :param min_volume_btc_24h: number
    :param tsl_enabled: boolean, Enable trailing stop loss. Bitmex only.
    :param deal_start_delay_seconds: integer, Deal start delay in seconds
    :param profit_currency: string, values: ['quote_currency', 'base_currency'], Take profit currency
    :param start_order_type: string, values: ['limit', 'market']
    :param stop_loss_type: string, values: ['stop_loss', 'stop_loss_and_disable_bot']
    :param disable_after_deals_count: integer, Bot will be disabled after opening this number of deals
    :param allowed_deals_on_same_pair: integer, Allow specific number of deals on the same pair. Multibot only.
    """
    error, data = wrapper.request(
        entity='bots',
        action='<py3cw_action>',
        action_id=str(bot_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_disable_by_bot_id(bot_id):
    """
    /ver1/bots/{bot_id}/disable
    Disable bot (Permission: BOTS_WRITE, Security: SIGNED)

    :param bot_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='bots',
        action='<py3cw_action>',
        action_id=str(bot_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_enable_by_bot_id(bot_id):
    """
    /ver1/bots/{bot_id}/enable
    Enable bot (Permission: BOTS_WRITE, Security: SIGNED)

    :param bot_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='bots',
        action='<py3cw_action>',
        action_id=str(bot_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_start_new_deal_by_bot_id(bot_id):
    """
    /ver1/bots/{bot_id}/start_new_deal
    Start new deal asap (Permission: BOTS_WRITE, Security: SIGNED)

    :param bot_id: REQUIRED, integer
    :param pair: string, Can be omited for simple bot
    :param skip_signal_checks: boolean, If false or not specified then all paramaters like signals or volume filters will be checked. If true - those checks will be skipped
    :param skip_open_deals_checks: boolean, If true then you will be allowed to open more then one deal per pair in composite bot
    """
    error, data = wrapper.request(
        entity='bots',
        action='<py3cw_action>',
        action_id=str(bot_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_delete_by_bot_id(bot_id):
    """
    /ver1/bots/{bot_id}/delete
    Delete bot (Permission: BOTS_WRITE, Security: SIGNED)

    :param bot_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='bots',
        action='<py3cw_action>',
        action_id=str(bot_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_panic_sell_all_deals_by_bot_id(bot_id):
    """
    /ver1/bots/{bot_id}/panic_sell_all_deals
    Panic sell all bot deals (Permission: BOTS_WRITE, Security: SIGNED)

    :param bot_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='bots',
        action='<py3cw_action>',
        action_id=str(bot_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_cancel_all_deals_by_bot_id(bot_id):
    """
    /ver1/bots/{bot_id}/cancel_all_deals
    Cancel all bot deals (Permission: BOTS_WRITE, Security: SIGNED)

    :param bot_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='bots',
        action='<py3cw_action>',
        action_id=str(bot_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def get_deals_stats_by_bot_id(bot_id):
    """
    /ver1/bots/{bot_id}/deals_stats
    Bot deals stats (Permission: BOTS_READ, Security: SIGNED)

    :param bot_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='bots',
        action='<py3cw_action>',
        action_id=str(bot_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def get_show_by_bot_id(bot_id):
    """
    /ver1/bots/{bot_id}/show
    Bot info (Permission: BOTS_READ, Security: SIGNED)

    :param bot_id: REQUIRED, integer
    :param include_events: boolean
    """
    error, data = wrapper.request(
        entity='bots',
        action='<py3cw_action>',
        action_id=str(bot_id),
    )
    return ThreeCommasError(error), data
'''


