from typing import List
import logging
from ...sys_utils import logged, with_py3cw
from ... import utils
from ...model import BotShow


logger = logging.getLogger(__name__)


@logged
@with_py3cw
def get_pairs_black_list(py3cw) -> List[str]:
    error, data = py3cw.request(
        entity='bots',
        action='pairs_black_list'
    )
    utils.verify_no_error(error=error, data=data)
    return data


@logged
@with_py3cw
def disable_bot(py3cw, bot_id: int):
    error, data = py3cw.request(
        entity='bots',
        action='disable',
        action_id=str(bot_id)
    )
    utils.verify_no_error(error=error, data=data)
    return data


@logged(log_return=True)
@with_py3cw
def copy_and_create(py3cw, bot_id: int, new_bot_name: str,  old_bot_url_secret: str):
    """
    POST /ver1/bots/{bot_id}/copy_and_create
    """
    error, data = py3cw.request(
        entity='bots',
        action='copy_and_create',
        action_id=str(bot_id),
        payload={
            'name': new_bot_name,
            'secret': old_bot_url_secret
        }
    )
    utils.verify_no_error(error=error, data=data)
    return data


@logged(reduce_long_arguments=True)
@with_py3cw
def update_bot(py3cw, bot_id: int, new_bot_show: dict) -> BotShow:
    error, data = py3cw.request(
        entity='bots',
        action='update',
        action_id=str(bot_id),
        payload=new_bot_show
    )
    utils.verify_no_error(error=error, data=data)
    return BotShow.of(data)


@logged
@with_py3cw
def get_bots(py3cw, enabled: bool = None, limit: int = None) -> List[BotShow]:
    payload = {}
    if enabled is not None:
        payload['scope'] = 'enabled' if enabled else 'disabled'
    if limit is not None:
        payload['limit'] = limit
    error, data = py3cw.request(
        entity='bots',
        action='',
        payload=payload
    )
    utils.verify_no_error(error=error, data=data)
    return BotShow.of_list(data)


@logged
@with_py3cw
def get_bot(py3cw, bot_id: int, include_events: bool = None) -> BotShow:
    """
    /ver1/bots/:bot_id/show
    """
    payload = {}
    if include_events is not None:
        payload['include_events'] = 'true' if include_events else 'false'
    error, data = py3cw.request(
        entity='bots',
        action='show',
        action_id=str(bot_id),
        payload=payload
    )
    utils.verify_no_error(error=error, data=data)
    return BotShow.of(data)


@logged
@with_py3cw
def enable_bot(py3cw, bot_id: int):
    error, data = py3cw.request(
        entity='bots',
        action='enable',
        action_id=str(bot_id)
    )
    utils.verify_no_error(error=error, data=data)
    return data


@logged
@with_py3cw
def create_bot(py3cw, bot_model: BotShow) -> BotShow:
    error, data = py3cw.request(
        entity='bots',
        action='create_bot',
        payload=bot_model
    )
    utils.verify_no_error(error=error, data=data)
    return BotShow.of(data)
