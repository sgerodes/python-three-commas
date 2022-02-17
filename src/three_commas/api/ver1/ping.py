from py3cw.request import Py3CW
from ...model import *
from ...error import ThreeCommasError
from typing import Tuple


wrapper = Py3CW('', '')


''' This endpoint was not present in the py3cw module
def get():
    """
    /ver1/ping
    Test connectivity to the Rest API (Permission: NONE, Security: NONE)

    """
    error, data = wrapper.request(
        entity='<py3cw_entity>',
        action='<py3cw_action>',
    )
    return ThreeCommasError(error), data
'''


