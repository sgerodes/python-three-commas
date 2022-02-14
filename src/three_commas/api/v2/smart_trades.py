from typing import List, Dict, Union
import logging
from ...sys_utils import logged, with_py3cw, Py3cwClosure, verify_no_error
from ...model import SmartTradeV2


logger = logging.getLogger(__name__)
py3cw: Py3cwClosure = None


@logged
@with_py3cw
def get_by_id(smart_trade_id: int) -> SmartTradeV2:
    """
    /v2/smart_trades/:id
    """
    error, data = py3cw.request(
        entity='smart_trades_v2',
        action='get_by_id',
        action_id=str(smart_trade_id),
    )
    verify_no_error(error=error, data=data)
    return SmartTradeV2.of(data)
