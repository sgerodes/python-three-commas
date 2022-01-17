from typing import List
import logging
from ...sys_utils import logged, get_p3cw
from ... import utils
from ...model import BotShow


logger = logging.getLogger(__name__)


@logged
def get_pairs_black_list() -> List[str]:
    error, data = get_p3cw().request(
        entity='bots',
        action='pairs_black_list'
    )
    utils.verify_no_error(error=error, data=data)
    return data


@logged
def disable_bot(bot_id: int):
    error, data = get_p3cw().request(
        entity='bots',
        action='disable',
        action_id=str(bot_id)
    )
    utils.verify_no_error(error=error, data=data)
    return data


@logged(log_return=True)
def copy_and_create(bot_id: int, new_bot_name: str,  old_bot_url_secret: str):
    """
    POST /ver1/bots/{bot_id}/copy_and_create
    """
    error, data = get_p3cw().request(
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
def update_bot(bot_id: int, new_bot_show: dict) -> BotShow:
    error, data = get_p3cw().request(
        entity='bots',
        action='update',
        action_id=str(bot_id),
        payload=new_bot_show
    )
    utils.verify_no_error(error=error, data=data)
    return BotShow.of(data)


@logged
def get_bots(enabled: bool = None, limit: int = None) -> List[BotShow]:
    payload = {}
    if enabled is not None:
        payload['scope'] = 'enabled' if enabled else 'disabled'
    if limit is not None:
        payload['limit'] = limit
    error, data = get_p3cw().request(
        entity='bots',
        action='',
        payload=payload
    )
    utils.verify_no_error(error=error, data=data)
    return BotShow.of_list(data)


@logged
def get_bot(bot_id: int, include_events: bool = None) -> BotShow:
    """
    /ver1/bots/:bot_id/show
    """
    payload = {}
    if include_events is not None:
        payload['include_events'] = 'true' if include_events else 'false'
    error, data = get_p3cw().request(
        entity='bots',
        action='show',
        action_id=str(bot_id),
        payload=payload
    )
    utils.verify_no_error(error=error, data=data)
    return BotShow.of(data)


@logged
def enable_bot(bot_id: int):
    error, data = get_p3cw().request(
        entity='bots',
        action='enable',
        action_id=str(bot_id)
    )
    utils.verify_no_error(error=error, data=data)
    return data


@logged
def create_bot(bot_model: BotShow) -> BotShow:
    error, data = get_p3cw().request(
        entity='bots',
        action='create_bot',
        payload=bot_model
    )
    utils.verify_no_error(error=error, data=data)
    return BotShow.of(data)
