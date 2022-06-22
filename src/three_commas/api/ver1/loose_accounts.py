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
def post(payload: dict = None):
    """
    POST /ver1/loose_accounts
    Create Loose Account (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        payload=payload,
    )
    return ThreeCommasApiError(error), data
'''


''' This endpoint was not present in the py3cw module
@logged
@with_py3cw
def get_available_currencies(payload: dict = None):
    """
    GET /ver1/loose_accounts/available_currencies
    Available currencies (Permission: ACCOUNTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        payload=payload,
    )
    return ThreeCommasApiError(error), data
'''


''' This endpoint was not present in the py3cw module
@logged
@with_py3cw
def put_by_id(id, payload: dict = None):
    """
    PUT /ver1/loose_accounts/{account_id}
    Update Loose Account (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(id),
        payload=payload,
    )
    return ThreeCommasApiError(error), data
'''


