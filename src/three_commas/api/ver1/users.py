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
def get_current_mode():
    """
    GET /ver1/users/current_mode
    Current User Mode (Paper or Real) (Permission: ACCOUNTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='users',
        action='current_mode',
    )
    return ThreeCommasApiError(error), data


@logged
@with_py3cw
def post_change_mode():
    """
    POST /ver1/users/change_mode
    Change User Mode (Paper or Real) (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='users',
        action='change_mode',
    )
    return ThreeCommasApiError(error), data


