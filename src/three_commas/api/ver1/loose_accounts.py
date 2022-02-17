from py3cw.request import Py3CW
from models import *


wrapper = Py3CW('', '')


''' This endpoint was not present in the py3cw module
def post():
    """
    /ver1/loose_accounts
    Create Loose Account (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    :param name: REQUIRED, string
    :param tokens[code]: REQUIRED, array
    :param tokens[amount]: REQUIRED, array
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

    :param contains: string
    :param limit: integer
    :param offset: integer
    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def put_by_account_id(account_id):
    """
    /ver1/loose_accounts/{account_id}
    Update Loose Account (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    :param tokens[code]: REQUIRED, array
    :param tokens[amount]: REQUIRED, array
    :param account_id: REQUIRED, integer
    :param name: string
    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data
'''


