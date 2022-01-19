from typing import List, Dict
import logging
from ...sys_utils import logged, with_py3cw, Py3cwClosure
from ... import utils
from ...model import Bot as BotShow


logger = logging.getLogger(__name__)
py3cw: Py3cwClosure = None


@logged(reduce_long_arguments=True)
@with_py3cw
def update(bot_id: int, new_bot_show: dict) -> BotShow:
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
def disable(bot_id: int) -> BotShow:
    error, data = py3cw.request(
        entity='bots',
        action='disable',
        action_id=str(bot_id)
    )
    utils.verify_no_error(error=error, data=data)
    return BotShow.of(data)


@logged
@with_py3cw
def enable(bot_id: int):
    error, data = py3cw.request(
        entity='bots',
        action='enable',
        action_id=str(bot_id)
    )
    utils.verify_no_error(error=error, data=data)
    return data


def start_new_deal():
    pass


def delete():
    pass


def panic_sell_all_deals():
    pass


def cancel_all_deals():
    pass


@logged
@with_py3cw
def get_show(bot_id: int, include_events: bool = None) -> BotShow:
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


@logged(log_return=True)
@with_py3cw
def copy_and_create(bot_id: int, name: str,  secret: str) -> dict:
    """
    POST /ver1/bots/{bot_id}/copy_and_create
    :param bot_id: bot to copy
    :param name: new bot name
    :param secret: bot secret that is copied
    :return: e.g. {'bot_id': 7812487, 'bot_required_amount': '0.018'}
    """
    error, data = py3cw.request(
        entity='bots',
        action='copy_and_create',
        action_id=str(bot_id),
        payload={
            'name': name,
            'secret': secret
        }
    )
    utils.verify_no_error(error=error, data=data)
    return data


@logged
@with_py3cw
def get_bots(scope: str, limit: int = None) -> List[BotShow]:
    """
    GET /ver1/bots
    :param scope: enabled, disabled
    :param limit: Limit records
    :return: return specified list of bots
    """
    payload = {}
    if scope:
        payload['scope'] = scope
    if limit:
        payload['limit'] = limit
    error, data = py3cw.request(
        entity='bots',
        action='',
        payload=payload
    )
    utils.verify_no_error(error=error, data=data)
    return BotShow.of_list(data)


def get_strategy_list() -> dict:
    pass


@logged
@with_py3cw
def get_pairs_black_list() -> Dict[str, List[str]]:
    error, data = py3cw.request(
        entity='bots',
        action='pairs_black_list'
    )
    utils.verify_no_error(error=error, data=data)
    return data


def update_pairs_black_list():
    pass


@logged
@with_py3cw
def create_bot(bot_model: BotShow) -> BotShow:
    error, data = py3cw.request(
        entity='bots',
        action='create_bot',
        payload=bot_model
    )
    utils.verify_no_error(error=error, data=data)
    return BotShow.of(data)


def get_stats():
    # TODO create BotStats model
    pass
