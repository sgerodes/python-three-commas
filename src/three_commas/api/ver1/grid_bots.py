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
def post_ai(payload: dict = None):
    """
    POST /ver1/grid_bots/ai
    Create AI Grid Bot (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='ai',
        payload=payload,
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def post_manual(payload: dict = None):
    """
    POST /ver1/grid_bots/manual
    Create Grid Bot (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='manual',
        payload=payload,
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def get_ai_settings(payload: dict = None):
    """
    GET /ver1/grid_bots/ai_settings
    Get AI settings (Permission: BOTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='ai_settings',
        payload=payload,
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def get(payload: dict = None):
    """
    GET /ver1/grid_bots
    Grid bots list (Permission: BOTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='',
        payload=payload,
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def get_market_orders_by_id(id, payload: dict = None):
    """
    GET /ver1/grid_bots/{id}/market_orders
    Grid Bot Market Orders (Permission: BOTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='market_orders',
        action_id=str(id),
        payload=payload,
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def get_profits_by_id(id, payload: dict = None):
    """
    GET /ver1/grid_bots/{id}/profits
    Grid Bot Profits (Permission: BOTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='profits',
        action_id=str(id),
        payload=payload,
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def patch_ai_by_id(id, payload: dict = None):
    """
    PATCH /ver1/grid_bots/{id}/ai
    Edit Grid Bot (AI) (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='ai_update',
        action_id=str(id),
        payload=payload,
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def patch_manual_by_id(id, payload: dict = None):
    """
    PATCH /ver1/grid_bots/{id}/manual
    Edit Grid Bot (Manual) (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='manual_update',
        action_id=str(id),
        payload=payload,
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def get_by_id(id, payload: dict = None):
    """
    GET /ver1/grid_bots/{id}
    Show Grid Bot (Permission: BOTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='get',
        action_id=str(id),
        payload=payload,
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def delete_by_id(id, payload: dict = None, payload: dict = None):
    """
    DELETE /ver1/grid_bots/{id}
    Delete Grid Bot (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='delete',
        action_id=str(id),
        payload=payload,
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def post_disable_by_id(id, payload: dict = None):
    """
    POST /ver1/grid_bots/{id}/disable
    Disable Grid Bot (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='disable',
        action_id=str(id),
        payload=payload,
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def post_enable_by_id(id, payload: dict = None):
    """
    POST /ver1/grid_bots/{id}/enable
    Enable Grid Bot (Permission: BOTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='enable',
        action_id=str(id),
        payload=payload,
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def get_required_balances_by_id(id, payload: dict = None):
    """
    GET /ver1/grid_bots/{id}/required_balances
    Get required balances to start bot(Permission: BOTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='grid_bots',
        action='required_balances',
        action_id=str(id),
        payload=payload,
    )
    return ThreeCommasApiError(error), data


