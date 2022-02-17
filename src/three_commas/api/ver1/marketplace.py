from py3cw.request import Py3CW
from models import *


wrapper = Py3CW('', '')


''' This endpoint was not present in the py3cw module
def get_presets():
    """
    /ver1/marketplace/presets
    Marketplace presets (Permission: NONE, Security: SIGNED)

    :param profit_per_day_from: number
    :param profit_per_day_to: number
    :param profit_per_month_from: number
    :param profit_per_month_to: number
    :param account_types: array
    :param markets: array
    :param with_all_market_pairs: boolean
    :param pairs: array
    :param days_running_from: integer
    :param days_running_to: integer
    :param deal_start_conditions: array
    :param bot_type: string
    :param bot_strategy: string
    :param cmc: string
    :param sort_by: string
    :param sort_direction: string, values: ['asc', 'desc']
    :param page: integer
    :param per_page: integer
    """
    error, data = wrapper.request(
        entity='marketplace',
        action='<py3cw_action>',
    )
    return ThreeCommasError(error), data
'''


def get_items():
    """
    /ver1/marketplace/items
    All marketplace items (Permission: NONE, Security: NONE)

    :param limit: integer, Limit records. Max: 1_000
    :param offset: integer, Offset records
    :param scope: string, values: ['all', 'paid', 'free'], paid - show only paid signal providers. free - show only free signal providers
    :param order: string, values: ['subscribers', 'name', 'newest']
    :param locale: string, values: ['en', 'ru', 'zh', 'zh-CN', 'es', 'pt', 'ko', 'fr', 'cs']
    """
    error, data = wrapper.request(
        entity='marketplace',
        action='items',
    )
    return ThreeCommasError(error), data


''' This endpoint was not present in the py3cw module
def get_signals_by_item_id(item_id):
    """
    /ver1/marketplace/{item_id}/signals
    Marketplace Item Signals (Permission: NONE, Security: NONE)

    :param item_id: REQUIRED, integer
    :param limit: integer, Limit records. Max: 1_000
    :param offset: integer, Offset records
    :param order: string, values: ['pair', 'exchange', 'signal_type', 'date']
    :param order_direction: string, values: ['asc', 'desc']
    :param locale: string, values: ['en', 'ru', 'zh', 'zh-CN', 'es', 'pt', 'ko', 'fr', 'cs']
    """
    error, data = wrapper.request(
        entity='marketplace',
        action='<py3cw_action>',
        action_id=str(item_id),
    )
    return ThreeCommasError(error), data
'''


