from __future__ import annotations
from typing import List, Union, Callable, TypeVar, Any
import datetime
import re
import functools
import logging
from .. import configuration


logger = logging.getLogger(__name__)

T = TypeVar('T')


class ThreeCommasParser:
    DATETIME_PATTERN = '%Y-%m-%dT%H:%M:%S.%fZ'

    @staticmethod
    def parsed_timestamp(func: Callable[[Any], Any]) -> Callable[[Any], Union[None, str, datetime.datetime]]:
        @functools.wraps(func)
        def wrapper(*args, parsed: bool = None, **kwargs) -> Union[None, str, datetime.datetime]:
            timestamp = func(*args, **kwargs)
            if timestamp is None:
                return None
            if parsed is None:
                parsed = configuration.THREE_COMMAS_AUTO_PARSE_DATETIME_DEFAULT
            return datetime.datetime.strptime(timestamp, ThreeCommasParser.DATETIME_PATTERN) if parsed else timestamp
        return wrapper

    @staticmethod
    def parsed(t: T):
        def decorator(func: Callable[[Any], Any]) -> Callable[[Any],  Union[T, None]]:
            @functools.wraps(func)
            def wrapper(*args, parsed: bool = None, **kwargs) -> Union[T, str, None]:
                result = func(*args, **kwargs)
                if result is None:
                    return None
                if parsed is None:
                    parsed = configuration.THREE_COMMAS_AUTO_PARSE_DEFAULT
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

    def __repr__(self):
        return f'{self.__class__.__name__}({super().__repr__()})'


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
