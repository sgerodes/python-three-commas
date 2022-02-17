from typing import List, Dict, Union
import logging
from ...sys_utils import logged, with_py3cw, Py3cwClosure, verify_no_error
from ...model import SmartTradeV2Entity


logger = logging.getLogger(__name__)
wrapper: Py3cwClosure = None


@logged
@with_py3cw
def get_by_id(id) -> SmartTradeV2Entity:
    """
    /v2/smart_trades/{id}
    Get smart trade v2 by id (Permission: SMART_TRADE_READ, Security: SIGNED)

    :param id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='get_by_id',
        action_id=str(id),
    )
    verify_no_error(error=error, data=data)
    return SmartTradeV2Entity.of(data)


@logged
@with_py3cw
def post(smart_trade_entity: SmartTradeV2Entity) -> SmartTradeV2Entity:
    """
    /v2/smart_trades
    Create smart trade v2 (Permission: SMART_TRADE_WRITE, Security: SIGNED)
    """

    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='new',
    )
    verify_no_error(error=error, data=data)
    return SmartTradeV2Entity.of(data)

