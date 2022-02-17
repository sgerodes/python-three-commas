from py3cw.request import Py3CW
from models import *


wrapper = Py3CW('', '')


def get_current_mode():
    """
    /ver1/users/current_mode
    Current User Mode (Paper or Real) (Permission: ACCOUNTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='users',
        action='current_mode',
    )
    return ThreeCommasError(error), data


def post_change_mode():
    """
    /ver1/users/change_mode
    Change User Mode (Paper or Real) (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    :param mode: REQUIRED, string, values: ['paper', 'real']
    """
    error, data = wrapper.request(
        entity='users',
        action='change_mode',
    )
    return ThreeCommasError(error), data


