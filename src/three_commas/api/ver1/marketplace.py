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
def get_presets(payload: dict = None):
    """
    GET /ver1/marketplace/presets
    Marketplace presets (Permission: NONE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='marketplace',
        action='presets',
        payload=payload,
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def get_items(payload: dict = None):
    """
    GET /ver1/marketplace/items
    All marketplace items (Permission: NONE, Security: NONE)

    """
    error, data = wrapper.request(
        entity='marketplace',
        action='items',
        payload=payload,
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def get_signals_by_id(id, payload: dict = None):
    """
    GET /ver1/marketplace/{item_id}/signals
    Marketplace Item Signals (Permission: NONE, Security: NONE)

    """
    error, data = wrapper.request(
        entity='marketplace',
        action='signals',
        action_id=str(id),
        payload=payload,
    )
    return ThreeCommasApiError(error), data


