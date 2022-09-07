from __future__ import annotations
from typing import List, Union, Callable, TypeVar, Any, Generic, Optional
import datetime
import functools
import logging
from .. import configuration
import copy


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


class ThreeCommasDict(dict):
    # TODO probably switch to prodict https://github.com/ramazanpolat/prodict
    def __init__(self, *args, **kwargs):
        if not args and not kwargs or (args and args[0] is None):
            return
        super().__init__(*args, **kwargs)

    @classmethod
    def deepcopy(cls, copy_from: dict):
        cp = copy.deepcopy(copy_from)
        return cls(cp)

    def __deepcopy__(self, memo=None):
        return self.__class__(copy.deepcopy(dict(self), memo=memo))

    @classmethod
    def of_list(cls, list_of_d: List[dict]) -> List[cls]:
        if list_of_d is None:
            return list()
        return [cls(d) for d in list_of_d]

    def __repr__(self):
        return f'{self.__class__.__name__}({super().__repr__()})'


class ThreeCommasModel(ThreeCommasDict):
    def __getattr__(self, name, parsed: bool = None):
        proxy_name = self._name_proxy.get(name)
        if proxy_name:
            name = proxy_name
        value = self.get(name)

        if value is None:
            return None
        if parsed is False:
            return value

        parser: Parser = self.__class__._parse_map.get(name)
        if parser is None:
            return value
        try:
            if parsed is None:
                return parser.parse(value=value)
            else:
                return parser.parse(value=value, parsed=parsed)
        except Exception:
            return value

    def __setattr__(self, name, value):
        proxy_name = self._name_proxy.get(name)
        if proxy_name is not None:
            self[proxy_name] = value
        else:
            self[name] = value

    TP = TypeVar('TP')

    def parsed(self: TP, parsed: bool) -> TP:
        return ParsedProxy(model=self, parsed=parsed)


class ParsedProxy:
    MODEL_KEY = '_model'
    PARSED_KEY = '_parsed'

    def __init__(self, model: ThreeCommasModel, parsed: bool):
        self.__dict__[ParsedProxy.MODEL_KEY] = model
        self.__dict__[ParsedProxy.PARSED_KEY] = parsed

    def __getattr__(self, name):
        return self.__dict__[ParsedProxy.MODEL_KEY].__getattr__(name, parsed=self.__dict__[ParsedProxy.PARSED_KEY])

    def __setattr__(self, key, value):
        self.model.__setattr__(key, value)


class Parser:
    @staticmethod
    def parse(value: str, parsed: bool = None):
        raise NotImplemented("The method for parsing was not implemented")


class IntParser(Parser):
    @staticmethod
    def parse(value: str, parsed: bool = True) -> Union[str, int]:
        return int(value) if parsed else value


class FloatParser(Parser):
    @staticmethod
    def parse(value: str, parsed: bool = True) -> Union[str, float]:
        return float(value) if parsed else value


class DatetimeParser(Parser):
    DATETIME_PATTERN = '%Y-%m-%dT%H:%M:%S.%fZ'

    @staticmethod
    def parse(value, parsed: bool = False) -> Union[str, datetime]:
        return datetime.datetime.strptime(value, DatetimeParser.DATETIME_PATTERN) if parsed else value
