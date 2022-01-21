from enum import Enum
from typing import List
from aenum import extend_enum
import logging


logger = logging.getLogger(__name__)


class AbstractStringEnum(str, Enum):
    @classmethod
    def _missing_(cls, value):
        logger.warning(f"Enum value='{value}' for {cls} is not known. Will extend the Enum. Allowed values were {cls._list_values()}")
        return extend_enum(cls, value.upper(), value)

    @classmethod
    def _list_values(cls) -> List[str]:
        return list(cls._value2member_map_.keys())
        # return list(map(lambda c: c.value, cls))

    @classmethod
    def _has_value(cls, value: str):
        return value in cls._value2member_map_

    @classmethod
    def _has_member(cls, member: str):
        return member in cls._member_names_

    def __eq__(self, other):
        if isinstance(other, str):
            return self.value == other
        else:
            return super.__eq__(self, other)

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return self.value
