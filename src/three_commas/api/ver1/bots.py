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
def get_strategy_list():
    """
    GET /ver1/bots/strategy_list
    Available strategy list for bot (Permission: BOTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='bots',
        action='strategy_list',
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def get_pairs_black_list():
    """
    GET /ver1/bots/pairs_black_list
    Black List for bot pairs (Permission: BOTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='bots',
        action='pairs_black_list',
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def post_update_pairs_black_list():
    """
    POST /ver1/bots/update_pairs_black_list
    Create or Update pairs BlackList for bots (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='bots',
        action='update_pairs_black_list',
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def post_create_bot():
    """
    POST /ver1/bots/create_bot
    Create bot (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='bots',
        action='create_bot',
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def get() -> Tuple[ThreeCommasApiError, List[BotEntity]]:
    """
    GET /ver1/bots
    User bots (Permission: BOTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='bots',
        action='',
    )
    return ThreeCommasApiError(error), BotEntity.of_list(data)


@logged
@with_py3cw
def get_stats():
    """
    GET /ver1/bots/stats
    Get bot stats (Permission: BOTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='bots',
        action='stats',
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def post_copy_and_create_by_id(bot_id):
    """
    POST /ver1/bots/{bot_id}/copy_and_create
    POST /bots/:id/copy_and_create. Permission: BOTS_WRITE, Security: SIGNED

    """
    error, data = wrapper.request(
        entity='bots',
        action='copy_and_create',
        action_id=str(bot_id),
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def patch_update_by_id(bot_id):
    """
    PATCH /ver1/bots/{bot_id}/update
    Edit bot (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='bots',
        action='update',
        action_id=str(bot_id),
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def post_disable_by_id(bot_id):
    """
    POST /ver1/bots/{bot_id}/disable
    Disable bot (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='bots',
        action='disable',
        action_id=str(bot_id),
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def post_enable_by_id(bot_id):
    """
    POST /ver1/bots/{bot_id}/enable
    Enable bot (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='bots',
        action='enable',
        action_id=str(bot_id),
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def post_start_new_deal_by_id(bot_id):
    """
    POST /ver1/bots/{bot_id}/start_new_deal
    Start new deal asap (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='bots',
        action='start_new_deal',
        action_id=str(bot_id),
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def post_delete_by_id(bot_id):
    """
    POST /ver1/bots/{bot_id}/delete
    Delete bot (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='bots',
        action='delete',
        action_id=str(bot_id),
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def post_panic_sell_all_deals_by_id(bot_id):
    """
    POST /ver1/bots/{bot_id}/panic_sell_all_deals
    Panic sell all bot deals (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='bots',
        action='panic_sell_all_deals',
        action_id=str(bot_id),
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def post_cancel_all_deals_by_id(bot_id):
    """
    POST /ver1/bots/{bot_id}/cancel_all_deals
    Cancel all bot deals (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='bots',
        action='cancel_all_deals',
        action_id=str(bot_id),
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def get_deals_stats_by_id(bot_id):
    """
    GET /ver1/bots/{bot_id}/deals_stats
    Bot deals stats (Permission: BOTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='bots',
        action='deals_stats',
        action_id=str(bot_id),
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def get_show_by_id(bot_id) -> Tuple[ThreeCommasApiError, BotEntity]:
    """
    GET /ver1/bots/{bot_id}/show
    Bot info (Permission: BOTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='bots',
        action='show',
        action_id=str(bot_id),
    )
    return ThreeCommasApiError(error), BotEntity(data)


