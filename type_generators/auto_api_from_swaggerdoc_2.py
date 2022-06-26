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


# ideas
# api.ver1.accounts.by_id.get(id=<id>)
# api.ver1.accounts.get() # use __call__()
# api.ver1.accounts.get.by_id_and_sub_id(id=<id>, sub_id=<sub_id>)
# api.ver1.accounts.get.by_id(id=<id>, sub_id=<sub_id>)
# api.get.ver1.accounts.by_id(id=<id>, sub_id=<sub_id>) # not preffered, better to have all account endpoint clustered in one file
# api.get.ver1.accounts.remove.post(id=<id>)
# api.get.ver1.accounts.get(id=<id>)
# api.get.ver1.accounts.get()

