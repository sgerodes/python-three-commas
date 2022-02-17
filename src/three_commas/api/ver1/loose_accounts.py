from py3cw.request import Py3CW
from ...model import *
from ...error import ThreeCommasError
from typing import Tuple


wrapper = Py3CW('', '')


''' This endpoint was not present in the py3cw module
def post():
    """
    /ver1/loose_accounts
    Create Loose Account (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def get_available_currencies():
    """
    /ver1/loose_accounts/available_currencies
    Available currencies (Permission: ACCOUNTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def put_by_id(account_id):
    """
    /ver1/loose_accounts/{account_id}
    Update Loose Account (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data
'''


