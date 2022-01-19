from __future__ import annotations
from typing import List, Union, Callable
import datetime
import re
import functools
import logging


logger = logging.getLogger(__name__)


class ThreeCommasParser:
    DATETIME_PATTERN = '%Y-%m-%dT%H:%M:%S.%fZ'

    @staticmethod
    def parsed_timestamp(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, parsed: bool = False, **kwargs) -> Union[None, str, datetime.datetime]:
            timestamp = func(*args, **kwargs)
            if timestamp is None:
                return None
            return datetime.datetime.strptime(timestamp, ThreeCommasParser.DATETIME_PATTERN) if parsed else timestamp
        return wrapper

    @staticmethod
    def parsed(t: type):
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args, parsed: bool = True, **kwargs) -> Union[t, str, None]:
                result = func(*args, **kwargs)
                if result is None:
                    return None
                return t(result) if parsed else result
            return wrapper
        return decorator

    @staticmethod
    def get_setter_with_getter(getter: Callable) -> Callable:
        """
        this assumes that the setter exists and has the same name convention. the 'g' is replaces with 's'
        """
        getter_name: str = getter.__name__
        setter_name = 's' + getter_name[1:]

        print()
        print(getter)
        print(getter.__globals__)
        print(dir(getter))
        print(getter.__dict__)

        instance_of_getter: dict = getter.__self__
        setter = dir(instance_of_getter)[setter_name]
        return setter
        # setting the result back
        # instance_of_method: dict = func.__self__
        # parameter = None
        # if len(args) == 1:
        #     parameter = args[0]
        # elif len(kwargs) == 1:
        #     parameter = kwargs.popitem()[1]
        #
        # if not isinstance(instance_of_method, dict):
        #     logger.warning(f'Enclosing instance is not a dict, cant set the lazy parsed result back')
        # elif not parameter:
        #     logger.warning(f'Could not determine the parameter from {args=}, {kwargs=}')
        # elif parameter not in instance_of_method:
        #     logger.warning(f'{parameter} was not found in the instance {instance_of_method}')
        # else:
        #     instance_of_method[parameter] = parsed_result

    @staticmethod
    def lazy_parsed_wip(t: Union[type, List]):
        def decorator(getter: Callable) -> Callable:
            was_parsed = False

            @functools.wraps(getter)
            def wrapper(*args, parsed: bool = True, **kwargs):
                nonlocal was_parsed
                if was_parsed or not parsed:
                    return getter(*args, **kwargs)

                result = getter(*args, **kwargs)
                was_parsed = True
                if result is None:
                    return None

                if str(t).startswith('typing.List['):
                    elem_type = t.__args__[0]
                    # TODO probably should not use the __init__ of the type
                    parsed_result = [elem_type(elem) for elem in result]
                else:
                    parsed_result = t(result)

                # setter = ThreeCommasParser.get_setter_with_getter(getter=getter)
                # setter(parsed_result)

                return parsed_result
            return wrapper
        return decorator

    @staticmethod
    def lazy_parsed(t: Union[type, List]):
        def decorator(getter: Callable) -> Callable:
            @functools.wraps(getter)
            def wrapper(*args, parsed: bool = True, **kwargs):
                result = getter(*args, **kwargs)
                if result is None:
                    return None
                if not parsed:
                    return result
                if str(t).startswith('typing.List['):
                    elem_type = t.__args__[0]
                    parsed_result = [elem_type(elem) for elem in result]
                else:
                    parsed_result = t(result)
                return parsed_result
            return wrapper
        return decorator


class OfDictClass(dict):
    @classmethod
    def of(cls, d: dict) -> Union[None, cls]:
        if d is None:
            return None
        return cls(d)

    @classmethod
    def of_list(cls, list_of_d: List[dict]) -> Union[None, List[cls]]:
        if list_of_d is None:
            return None
        return [cls.of(d) for d in list_of_d]


class DealShow(OfDictClass):
    def get_id(self) -> int:
        return self.get('id')

    @ThreeCommasParser.parsed_timestamp
    def get_created_at(self) -> Union[None, str, datetime.datetime]:
        return self.get('created_at')

    @ThreeCommasParser.parsed_timestamp
    def get_updated_at(self) -> Union[None, str, datetime.datetime]:
        return self.get('updated_at')

    @ThreeCommasParser.parsed_timestamp
    def get_closed_at(self) -> Union[None, str, datetime.datetime]:
        return self.get('closed_at')

    def is_finished(self) -> bool:
        return self.get('finished?')

    def get_pair(self) -> str:
        return self.get('pair')

    @ThreeCommasParser.parsed(float)
    def get_bought_volume(self) -> Union[None, str, float]:
        return self.get('bought_volume')


class DealMarketOrder(OfDictClass):
    # Getters

    @ThreeCommasParser.parsed(int)
    def get_order_id(self) -> Union[None, str, int]:
        return self.get('order_id')

    def get_order_type(self) -> str:
        return self.get('order_type')

    def get_cancellable(self) -> bool:
        return self.get('cancellable')

    def get_deal_order_type(self) -> str:
        return self.get('deal_order_type')

    def get_status_string(self) -> str:
        return self.get('status_string')

    @ThreeCommasParser.parsed_timestamp
    def get_created_at(self) -> Union[None, str, datetime.datetime]:
        return self.get('created_at')

    @ThreeCommasParser.parsed_timestamp
    def get_updated_at(self) -> Union[None, str, datetime.datetime]:
        return self.get('updated_at')

    @ThreeCommasParser.parsed(float)
    def get_quantity(self) -> Union[None, str, float]:
        return self.get('quantity')

    @ThreeCommasParser.parsed(float)
    def get_quantity_remaining(self) -> Union[None, str, float]:
        return self.get('quantity_remaining')

    @ThreeCommasParser.parsed(float)
    def get_total(self) -> Union[None, str, float]:
        return self.get('total')

    @ThreeCommasParser.parsed(float)
    def get_rate(self) -> Union[None, str, float]:
        return self.get('rate')

    @ThreeCommasParser.parsed(float)
    def get_average_price(self) -> Union[None, str, float]:
        return self.get('average_price')

    # Setter

    def set_created_at(self, created_at: str):
        self['created_at'] = created_at

    def set_updated_at(self, updated_at: str):
        self['updated_at'] = updated_at

    def set_active_status_string(self):
        self['status_string'] = 'Active'

    # Etc
    # is status_string

    def is_active_status_string(self) -> bool:
        return self.get_status_string() == 'Active'

    def is_filled_status_string(self) -> bool:
        return self.get_status_string() == 'Filled'

    def is_canceled_status_string(self) -> bool:
        return self.get_status_string() == 'Cancelled'

    # is deal_order_type
    def is_base_order_type(self) -> bool:
        return self.get_deal_order_type() == 'Base'

    def is_safety_order_type(self) -> bool:
        return self.get_deal_order_type() == 'Safety'

    def is_manual_safety_order_type(self) -> bool:
        return self.get_deal_order_type() == 'Manual Safety'

    def is_take_profit_order_type(self) -> bool:
        return self.get_deal_order_type() == 'Take Profit'


class BotShow(OfDictClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        bot_events = self.get_bot_events()
        bot_events_parsed = None if bot_events is None else BotEvent.of_list(bot_events)
        self.set_bot_events(bot_events_parsed)

        active_deals = self.get_bot_events()
        active_deals_parsed = None if active_deals is None else DealShow.of_list(active_deals)
        self.set_active_deals(active_deals_parsed)

    def get_active_deals(self) -> List[DealShow]:
        return self.get('active_deals')

    def set_active_deals(self, active_deals: List[DealShow]):
        self['active_deals'] = active_deals

    def get_bot_events(self) -> List[BotEvent]:
        return self.get('bot_events')

    def set_bot_events(self, bot_events: List[BotEvent]):
        self['bot_events'] = bot_events

    def get_url_secret(self) -> str:
        return self.get('url_secret')

    def is_enabled(self) -> bool:
        return self.get('is_enabled')

    def set_is_enabled(self, is_enabled: bool):
        self['is_enabled'] = is_enabled

    def get_pairs(self) -> List[str]:
        return self.get("pairs")

    def set_pairs(self, pairs: List[str]):
        self['pairs'] = pairs

    def set_pair(self, pair: str):
        self.set_pairs([pair])

    def get_name(self) -> str:
        return self.get('name')

    def set_name(self, name: str):
        self['name'] = name

    def get_account_id(self) -> int:
        return self.get("account_id")

    def get_id(self) -> int:
        return self.get('id')

    def has_pair(self, pair: str) -> bool:
        return pair in self.get_pairs()

    @ThreeCommasParser.parsed(float)
    def get_base_order_volume(self) -> Union[None, str, float]:
        return self.get('base_order_volume')

    def set_base_order_volume(self, value: Union[float, str]):
        self['base_order_volume'] = value

    @ThreeCommasParser.parsed(float)
    def get_safety_order_volume(self) -> Union[None, str, float]:
        return self.get('safety_order_volume')

    @ThreeCommasParser.parsed(float)
    def get_martingale_volume_coefficient(self) -> Union[None, str, float]:
        return self.get('martingale_volume_coefficient')

    def get_max_safety_orders(self) -> int:
        return self.get('max_safety_orders')

    def get_max_active_deals(self) -> int:
        return self.get('max_active_deals')

    def get_bot_quote(self) -> Union[str, None]:
        pairs = self.get_pairs()
        if not pairs:
            return None
        return pairs[0].split('_')[0].upper()

    def pairs_are_quote(self, quote: str) -> bool:
        return quote.upper() == self.get_bot_quote()

    @ThreeCommasParser.parsed_timestamp
    def get_created_at(self) -> Union[None, str, datetime.datetime]:
        return self.get('created_at')


class PieChartDataElement(OfDictClass):
    def get_code(self) -> str:
        return self.get('code')

    def get_coinmarketcapid(self) -> str:
        return self.get('coinmarketcapid')

    def get_name(self) -> str:
        return self.get('name')

    def get_y(self) -> float:
        return self.get('y')

    def get_percentage(self) -> float:
        return self.get('percentage')

    def get_amount(self) -> float:
        return self.get('amount')

    @ThreeCommasParser.parsed(float)
    def get_btc_value(self) -> Union[str, float]:
        return self.get('btc_value')

    @ThreeCommasParser.parsed(float)
    def get_usd_value(self) -> Union[str, float]:
        return self.get('usd_value')

    def get_account_id(self) -> int:
        return self.get('account_id')


class Account(OfDictClass):
    def is_futures(self) -> bool:
        return "futures" in self.get('supported_market_types')

    def is_spot(self) -> bool:
        return "spot" in self.get('supported_market_types')

    def get_market_code(self) -> str:
        return self.get("market_code")

    def is_paper(self) -> bool:
        return self.get_market_code() == 'paper_trading'


class BotEvent(OfDictClass):
    PRICE_PATTERN = re.compile(r"Price: ([\d.]+)\b", re.IGNORECASE)
    SIZE_PATTERN = re.compile(r"Size: ([\d.]+)\b", re.IGNORECASE)
    QUOTE_CURRENCY_PATTERN = re.compile(r"Price: [\d.]+ (\w+).", re.IGNORECASE)
    BASE_CURRENCY_PATTERN = re.compile(r"\([\d.]+ (\w+)\)", re.IGNORECASE)
    SAFETY_TRADE_EXECUTED_PATTERN = re.compile(r"Safety trade \(\d+ out of \d+\) executed", re.IGNORECASE)
    SAFETY_TRADE_NR_PATTERN = re.compile(r"Safety trade \((\d+) out of \d+\) executed", re.IGNORECASE)

    @ThreeCommasParser.parsed_timestamp
    def get_created_at(self) -> Union[None, str, datetime.datetime]:
        return self.get('created_at')

    def get_message(self) -> str:
        return self.get('message')

    def is_base_order_executed_message(self):
        return 'Base order executed' in self.get_message()

    def is_error(self):
        return 'error occurred' in self.get_message()

    def is_deal_completed_message(self):
        return 'Deal completed' in self.get_message()

    def is_safety_trade_executed_message(self):
        return len(self.SAFETY_TRADE_EXECUTED_PATTERN.findall(self.get_message())) > 0

    def get_safety_trade_number(self):
        findall = self.SAFETY_TRADE_NR_PATTERN.findall(self.get_message())
        return findall[0] if findall else None

    def get_price(self):
        findall = self.PRICE_PATTERN.findall(self.get_message())
        return findall[0] if findall else None

    def get_size(self):
        findall = self.SIZE_PATTERN.findall(self.get_message())
        return findall[0] if findall else None

    def get_quote_currency(self):
        findall = self.QUOTE_CURRENCY_PATTERN.findall(self.get_message())
        return findall[0] if findall else None

    def get_base_currency(self):
        findall = self.BASE_CURRENCY_PATTERN.findall(self.get_message())
        return findall[0] if findall else None
