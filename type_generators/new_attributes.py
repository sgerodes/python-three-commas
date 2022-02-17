from __future__ import annotations
from typing import *
from inspect import getframeinfo, stack
from typing import get_type_hints
import functools
import datetime



class ThreeCommasParser:

    @staticmethod
    def parsed(t: T):
        def decorator(func: Callable[[Any], Any]) -> Callable[[Any],  Union[T, None]]:
            @functools.wraps(func)
            def wrapper(*args, parsed: bool = None, **kwargs) -> Union[T, str, None]:
                result = func(*args, **kwargs)
                if result is None:
                    return None
                if parsed is None:
                    parsed = False
                return t(result) if parsed else result
            return wrapper
        return decorator


class ThreeCommasDict(dict):
    def __init__(self, d: dict = None):
        if d is None:
            return
        super().__init__(d)

    @classmethod
    def of(cls, d: dict) -> Union[None, cls]:
        if d is None:
            return None
        return cls(d)

    @classmethod
    def of_list(cls, list_of_d: List[dict]) -> List[cls]:
        if list_of_d is None:
            return None
        return [cls(d) for d in list_of_d]

    def __repr__(self):
        return f'{self.__class__.__name__}({super().__repr__()})'


class ThreeCommasModel(ThreeCommasDict):
    def __setattr__(self, name, value):
        if not isinstance(value, GenericParsedGetSetProxy):
            raise RuntimeError(f'Please set the attributes of the object with <your_object>.<attribute>.set(<your_value>), not <your_object>.<attribute> = <your_value>')
        super().__setattr__(name, value)


T_initial = TypeVar('T_initial')
T_parsed = TypeVar('T_parsed')


class GenericParsedGetSetProxy(Generic[T_initial, T_parsed]):

    def __init__(self, obj: ThreeCommasDict, attribute_name: str, t_initial: T_initial = None, t_parsed: T_parsed = None):
        self.obj = obj
        self.attribute_name = attribute_name
        self.t_initial = t_initial
        self.t_parsed = t_parsed

        if t_parsed is not None:
            @ThreeCommasParser.parsed(t_parsed)
            def get_proxy() -> Optional[Union[t_initial, t_parsed]]:
                return self.obj.get(self.attribute_name)
        else:
            def get_proxy() -> Optional[t_initial]:
                return self.obj.get(self.attribute_name)

        self.get_proxy = get_proxy

    def set(self, value):
        self.obj[self.attribute_name] = value

    def get(self, *args, **kwargs) -> Optional[Union[T_initial, T_parsed]]:
        return self.get_proxy(*args, **kwargs)

    def __repr__(self):
        parsed_repr = f', {self.t_initial or ""} --> {self.t_parsed or ""}' if self.t_initial or self.t_parsed else ''
        return f'{self.__class__.__name__}(class={self.obj.__class__.__name__}, attribute={self.attribute_name}{parsed_repr})'


class DealEntity(ThreeCommasModel):
    def __init__(self, d: dict = None):
        super().__init__(d)
        self.int_attr = GenericParsedGetSetProxy(self, 'int_attr', int)
        self.str_attr = GenericParsedGetSetProxy(self, 'str_attr', str, int)


a = DealEntity({'str_attr': '1111', 'int_attr': 1234})
print(a.str_attr)
print(a.str_attr.get())
print(type(a.str_attr.get()))
print(type(a.str_attr.get(parsed=True)))
at = a.str_attr.get(parsed=True)
a.str_attr.set("hi")
print(isinstance(a, DealEntity))

o = DealEntity({})
print(bool(o))
print(DealEntity(a))
print(o.str_attr)
print(a.int_attr.get())


