from py3cw.request import Py3CW
from ...model import *
from ...error import ThreeCommasApiError
from typing import Tuple, List
import logging
from ...sys_utils import logged, with_py3cw, Py3cwClosure


logger = logging.getLogger(__name__)
wrapper: Py3cwClosure = None


''' This endpoint was not present in the py3cw module
@logged
@with_py3cw
def get_presets():
    """
    GET /ver1/marketplace/presets
    Marketplace presets (Permission: NONE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='marketplace',
        action='<py3cw_action>',
    )
    return ThreeCommasApiError(error), data
'''


@logged
@with_py3cw
def get_items():
    """
    GET /ver1/marketplace/items
    All marketplace items (Permission: NONE, Security: NONE)

    """
    error, data = wrapper.request(
        entity='marketplace',
        action='items',
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def get_signals_by_id(item_id):
    """
    GET /ver1/marketplace/{item_id}/signals
    Marketplace Item Signals (Permission: NONE, Security: NONE)

    """
    error, data = wrapper.request(
        entity='marketplace',
        action='signals',
        action_id=str(item_id),
    )
    return ThreeCommasApiError(error), data


