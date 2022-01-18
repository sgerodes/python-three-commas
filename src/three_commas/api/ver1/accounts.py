from typing import List
import logging
from ...sys_utils import logged, with_py3cw, Py3cwClosure
from ... import utils
from ...model import Account, PieChartDataElement


logger = logging.getLogger(__name__)
py3cw: Py3cwClosure = None

@logged
@with_py3cw
def get_pie_chart_data(account_id: int) -> List[PieChartDataElement]:
    error, data = py3cw.request(
        entity='accounts',
        action='pie_chart_data',
        action_id=str(account_id)
    )
    utils.verify_no_error(error=error, data=data)
    return PieChartDataElement.of_list(data)


@logged
@with_py3cw
def get_account_balance_chart_data(account_id: int, date_from: str, date_to: str = None):
    """
    :param account_id:
    :param date_from: format YYYY-MM-DD
    :param date_to: format YYYY-MM-DD
    :return:
    """
    payload = {
        'date_from': date_from,
    }
    if date_to is not None:
        payload['date_to'] = date_to

    error, data = py3cw.request(
        entity='accounts',
        action='balance_chart_data',
        action_id=str(account_id),
        payload=payload
    )
    utils.verify_no_error(error=error, data=data)
    return data


@logged
@with_py3cw
def get_market_pairs(market_code: str) -> List[str]:
    error, data = py3cw.request(
        entity='accounts',
        action='market_pairs',
        payload={'market_code': market_code}
    )
    utils.verify_no_error(error=error, data=data)
    return data


@logged
@with_py3cw
def get_accounts() -> List[Account]:
    """
    /ver1/accounts
    :return:
    """
    error, data = py3cw.request(
        entity='accounts',
        action=''
    )
    utils.verify_no_error(error=error, data=data)
    return Account.of_list(data)


@logged
@with_py3cw
def get_account(account_id: int) -> Account:
    """
    /ver1/accounts/:account_id
    :param account_id:
    :return:
    """
    error, data = py3cw.request(
        entity='accounts',
        action='account_info',
        action_id=str(account_id)
    )
    utils.verify_no_error(error=error, data=data)
    return Account.of(data)
