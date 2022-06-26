import dataclasses
from symbol import parameters
from typing import List


@dataclasses.dataclass
class FunctionParameter:
    name: str
    type: str
    default_value: str


@dataclasses.dataclass
class ThreeCommasApiFunction:
    INDENT = ' ' * 4
    verb: str
    path: str
    swagger_description: str
    parameters:  List[FunctionParameter]
    return_type: str
    docstring: str
    entity: str
    action: str
    action_id_name: str
    sub_id_name: str
