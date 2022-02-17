from py3cw.request import Py3CW
from ...model import *
from ...error import ThreeCommasError
from typing import Tuple


wrapper = Py3CW('', '')


''' This endpoint was not present in the py3cw module
def get_presets():
    """
    /ver1/marketplace/presets
    Marketplace presets (Permission: NONE, Security: SIGNED)

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

    """
    error, data = wrapper.request(
        entity='marketplace',
        action='items',
    )
    return ThreeCommasError(error), data


def get_signals_by_id(item_id):
    """
    /ver1/marketplace/{item_id}/signals
    Marketplace Item Signals (Permission: NONE, Security: NONE)

    """
    error, data = wrapper.request(
        entity='marketplace',
        action='signals',
        action_id=str(item_id),
    )
    return ThreeCommasError(error), data


