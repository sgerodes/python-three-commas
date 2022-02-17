from py3cw.request import Py3CW
from models import *


wrapper = Py3CW('', '')


def post_ai():
    """
    /ver1/grid_bots/ai
    Create AI Grid Bot (Permission: BOTS_WRITE, Security: SIGNED)

    :param account_id: REQUIRED, integer, id from GET /ver1/accounts
    :param pair: REQUIRED, string
    :param total_quantity: REQUIRED, number
    :param name: string, Grid Bot's name
    :param leverage_type: string, values: ['custom', 'cross', 'not_specified', 'isolated'], Leverage type for futures accounts
    :param leverage_custom_value: number, Required if leverage_type = 'isolated'
    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='ai',
    )
    return ThreeCommasError(error), data


def post_manual():
    """
    /ver1/grid_bots/manual
    Create Grid Bot (Permission: BOTS_WRITE, Security: SIGNED)

    :param account_id: REQUIRED, integer, id from GET /ver1/accounts
    :param pair: REQUIRED, string
    :param upper_price: REQUIRED, number
    :param lower_price: REQUIRED, number
    :param quantity_per_grid: REQUIRED, number
    :param grids_quantity: REQUIRED, number
    :param name: string, Grid Bot's name
    :param leverage_type: string, values: ['custom', 'cross', 'not_specified', 'isolated'], Leverage type for futures accounts
    :param leverage_custom_value: number, Required if leverage_type = 'isolated'
    :param is_enabled: boolean, Turn on or off grid_bot after creation
    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='manual',
    )
    return ThreeCommasError(error), data


def get_ai_settings():
    """
    /ver1/grid_bots/ai_settings
    Get AI settings (Permission: BOTS_READ, Security: SIGNED)

    :param pair: REQUIRED, string
    :param market_code: REQUIRED, string, Market code from /accounts/market_list
    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='ai_settings',
    )
    return ThreeCommasError(error), data


def get():
    """
    /ver1/grid_bots
    Grid bots list (Permission: BOTS_READ, Security: SIGNED)

    :param account_ids: array, Filter by account id
    :param account_types: array, Filter by account type
    :param state: string, values: ['enabled', 'disabled'], Filter by bot state
    :param sort_by: string, values: ['current_profit', 'profit', 'bot_id', 'pair', 'created_at', 'updated_at'], Sort column
    :param sort_direction: string, values: ['desc', 'asc'], Sort direction
    :param limit: integer
    :param offset: integer
    :param from: string, Param for a filter by created date
    :param base: string, Base currency
    :param quote: string, Quote currency
    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='',
    )
    return ThreeCommasError(error), data


def get_market_orders_by_id(id):
    """
    /ver1/grid_bots/{id}/market_orders
    Grid Bot Market Orders (Permission: BOTS_READ, Security: SIGNED)

    :param id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='market_orders',
        action_id=str(id),
    )
    return ThreeCommasError(error), data


def get_profits_by_id(id):
    """
    /ver1/grid_bots/{id}/profits
    Grid Bot Profits (Permission: BOTS_READ, Security: SIGNED)

    :param id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='profits',
        action_id=str(id),
    )
    return ThreeCommasError(error), data


def patch_ai_by_id(id):
    """
    /ver1/grid_bots/{id}/ai
    Edit Grid Bot (AI) (Permission: BOTS_WRITE, Security: SIGNED)

    :param pair: REQUIRED, string
    :param total_quantity: REQUIRED, number
    :param id: REQUIRED, integer
    :param name: string, Grid Bot's name
    :param leverage_type: string, values: ['custom', 'cross', 'not_specified', 'isolated'], Leverage type for futures accounts
    :param leverage_custom_value: number, Required if leverage_type = 'isolated'
    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='ai_update',
        action_id=str(id),
    )
    return ThreeCommasError(error), data


def patch_manual_by_id(id):
    """
    /ver1/grid_bots/{id}/manual
    Edit Grid Bot (Manual) (Permission: BOTS_WRITE, Security: SIGNED)

    :param pair: REQUIRED, string
    :param upper_price: REQUIRED, number
    :param lower_price: REQUIRED, number
    :param quantity_per_grid: REQUIRED, number
    :param grids_quantity: REQUIRED, number
    :param id: REQUIRED, integer
    :param name: string, Grid Bot's name
    :param leverage_type: string, values: ['custom', 'cross', 'not_specified', 'isolated'], Leverage type for futures accounts
    :param leverage_custom_value: number, Required if leverage_type = 'isolated'
    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='manual_update',
        action_id=str(id),
    )
    return ThreeCommasError(error), data


def delete_by_id(id):
    """
    /ver1/grid_bots/{id}
    Delete Grid Bot (Permission: BOTS_WRITE, Security: SIGNED)

    :param id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='delete',
        action_id=str(id),
    )
    return ThreeCommasError(error), data


def post_disable_by_id(id):
    """
    /ver1/grid_bots/{id}/disable
    Disable Grid Bot (Permission: BOTS_WRITE, Security: SIGNED)

    :param id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='disable',
        action_id=str(id),
    )
    return ThreeCommasError(error), data


def post_enable_by_id(id):
    """
    /ver1/grid_bots/{id}/enable
    Enable Grid Bot (Permission: BOTS_WRITE, Security: SIGNED)

    :param id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='enable',
        action_id=str(id),
    )
    return ThreeCommasError(error), data


def get_required_balances_by_id(id):
    """
    /ver1/grid_bots/{id}/required_balances
    Get required balances to start bot(Permission: BOTS_READ, Security: SIGNED)

    :param id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='required_balances',
        action_id=str(id),
    )
    return ThreeCommasError(error), data


