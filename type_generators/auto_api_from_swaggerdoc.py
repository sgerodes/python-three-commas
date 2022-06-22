import json
from typing import Dict, List
from collections import defaultdict
from pathlib import Path
import os
from py3cw.config import API_METHODS as PY3CW_API_METHODS
import datetime
import re
from parsing_and_return_mapping import PARSING_MAPPING, endpoint_returns, endpoint_consumes


INDENT = ' ' * 4
PARENT_FOLDER_NAME = '../src/three_commas/api'
MODEL_FILE_NAME = '../src/three_commas/model/generated_models.py'


def get_path_variables(path: str):
    path_variables_list: list = list(filter(lambda e: '{' in e, path.split('/')))
    path_variable_1 = path_variables_list.pop(0).replace('{', '').replace('}', '') if path_variables_list else None
    path_variable_2 = path_variables_list.pop(0).replace('{', '').replace('}', '') if path_variables_list else None
    return path_variable_1, path_variable_2


def create_docstring(verb: str, path: str, parameters: list, description, return_type=None):
    if not parameters and not description:
        return None

    code = list()
    code.append(f'{INDENT}"""')
    code.append(f'{INDENT}{verb.upper()} {path}')
    if description:
        code.append(f'{INDENT}{description}')
        code.append(f'')

    # if parameters:
    #     parameters.sort(key=lambda p: p.get('required'), reverse=True)
    #     for p in parameters:
    #         _in = p.get('in')
    #         param_name = p.get('name')
    #         param_type = p.get('type')
    #         required = p.get('required')
    #         param_description = p.get('description')
    #         enum = p.get('enum')
    #
    #         param_docstring = list()
    #         if required:
    #             param_docstring.append('REQUIRED')
    #         if param_type:
    #             param_docstring.append(param_type)
    #         if enum:
    #             param_docstring.append("values: " + str(enum))
    #         if param_description:
    #             param_docstring.append(param_description)
    #
    #         code.append(f'{INDENT}:param {param_name}: ' + ', '.join(param_docstring))

    if return_type:
        code.append(f'{INDENT}:return:{str(return_type)}')

    code.append(f'{INDENT}"""')
    return '\n'.join(code)


def get_api_version_from_path(path: str):
    return path.split('/')[1]


def get_major_endpoint_from_path(path: str):
    return path.split('/')[2]


def get_sub_path(path: str):
    return '/'.join(path.split('/')[3:])


def make_ids_uniform_for_path(sub_path):
    second_replaced = re.sub(r'\{[^}]*\}', '{sub_id}', sub_path)
    return re.sub(r'\{[^}]*\}', '{id}', second_replaced, 1)


def create_function_logic(verb: str, path: str, parameters: List[dict], return_type: str = None, function_has_payload: bool = None) -> str:
    path_variable_1, path_variable_2 = get_path_variables(path)

    version = get_api_version_from_path(path)
    endpoint = get_major_endpoint_from_path(path)
    sub_path = get_sub_path(path)
    py3cw_parsed_sub_path = make_ids_uniform_for_path(sub_path)

    if version == 'v2':
        endpoint = 'smart_trades_v2'

    py3cw_endpoint = PY3CW_API_METHODS.get(endpoint)

    py3cw_entity = '<py3cw_entity>'
    if endpoint in PY3CW_API_METHODS:
        py3cw_entity = endpoint

    py3cw_action = '<py3cw_action>'
    # print(endpoint)
    if py3cw_endpoint:
        for k, v in py3cw_endpoint.items():
            if verb.upper() == v[0] and py3cw_parsed_sub_path == v[1]:
                py3cw_action = k

    code = list()

    code.append(f'{INDENT}error, data = wrapper.request(')
    code.append(f"{INDENT*2}entity='{py3cw_entity}',")
    code.append(f"{INDENT*2}action='{py3cw_action}',")
    if path_variable_1:
        # code.append(f"{INDENT*2}action_id=str({path_variable_1}),")
        code.append(f"{INDENT*2}action_id=str(id),")
    if path_variable_2:
        # code.append(f"{INDENT*2}action_sub_id=str({path_variable_2}),")
        code.append(f"{INDENT*2}action_sub_id=str(sub_id),")
    if function_has_payload:
        code.append(f"{INDENT*2}payload=payload,")
    code.append(f"{INDENT})")
    if return_type:
        if return_type.startswith('List['):
            list_element_type = return_type.split('[')[1].split(']')[0]
            if list_element_type in {"str", "float", "int", "bool", "dict", "list"}:
                code.append(f"{INDENT}return ThreeCommasApiError(error), data")
            else:
                code.append(f"{INDENT}return ThreeCommasApiError(error), {list_element_type}.of_list(data)")
        else:
            code.append(f"{INDENT}return ThreeCommasApiError(error), {return_type}(data)")
    else:
        code.append(f"{INDENT}return ThreeCommasApiError(error), data")

    return '\n'.join(code)


def get_str_repr_for_type(parsed_type: type):
    if parsed_type in {str, float, int, bool}:
        return parsed_type.__name__
    if isinstance(parsed_type, str):
        return parsed_type
    if parsed_type is datetime.datetime:
        return 'datetime.datetime'

    return parsed_type.__name__


def create_models(swaggerdoc: Dict[str, dict]):
    swagger_type_2_py_type = {
        'number': 'float',
        'string': 'str',
        'integer': 'int',
        'object': 'dict',
        'array': 'list',
        'boolean': 'bool',
    }
    proxy_parse_type_mapping = {
        float: 'FloatParser',
        int: 'IntParser',
        datetime.datetime: 'DatetimeParser',
    }
    superclass = 'ThreeCommasModel'
    code = list()
    code.append(f'from __future__ import annotations')
    code.append('from .models import ThreeCommasModel, FloatParser, IntParser, DatetimeParser, ParsedProxy')
    code.append('import datetime')
    code.append('from typing import Union')
    code.append(f'')
    code.append(f'')

    for model_name, model_definition in swaggerdoc.get('definitions').items():
        _parse_map = dict()
        _name_proxy = dict()
        # proxy_parse_type_parsing_map = dict()
        code.append(f'class {model_name}({superclass}):')
        # code.append(f'{INDENT}def __init__(self, d: dict = None):')
        # code.append(f'{INDENT*2}super().__init__(d)')
        for json_attribute_name, attribute_definition in model_definition.get('properties').items():
            swagger_type = attribute_definition.get('type')
            py_type = swagger_type_2_py_type.get(swagger_type)
            example = attribute_definition.get('example')
            model_attribute_name = json_attribute_name.replace('?', '')
            parsed_type = None

            if example and isinstance(example, str):
                # '2019-01-01T00:00:00.000Z'
                # TODO the formats are messed up
                pat = re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z')
                if pat.match(example) is not None:
                    parsed_type = 'datetime.datetime'

            if parsed_type is None:
                model_parsings = PARSING_MAPPING.get(model_name)
                if model_parsings and json_attribute_name in model_parsings:
                    parsed_type = model_parsings.get(json_attribute_name)

            parse_type = proxy_parse_type_mapping.get(parsed_type)
            if parse_type:
                _parse_map[model_attribute_name] = parse_type
                # proxy_parse_type_parsing_map[model_attribute_name] = proxy_type
            if json_attribute_name.endswith('?'):
                # proxy_parse_type_parsing_map[model_attribute_name] = 'QuestionMarkProxy'
                _name_proxy[model_attribute_name] = json_attribute_name

            attribute_type = f'Union[{py_type}, {get_str_repr_for_type(parsed_type)}]' if parse_type else f'{py_type}'
            codeline = f'{INDENT}{model_attribute_name}: {attribute_type}'

            code.append(codeline)

        # code.append(f'')
        # code.append(f'{INDENT}def parsed(self, parsed: bool) -> {model_name}:')
        # code.append(f'{INDENT*2}return ParsedProxy(model=self, parsed=parsed)')

        code.append(f'')
        code.append(f'{INDENT}_parse_map = {"{"}')
        for model_attribute_name, parse_type in _parse_map.items():
            code.append(f"{INDENT*2}'{model_attribute_name}': {parse_type},")
        code.append(f'{INDENT}{"}"}')

        code.append(f'{INDENT}_name_proxy = {"{"}')
        for model_attribute_name, json_name in _name_proxy.items():
            code.append(f"{INDENT*2}'{model_attribute_name}': '{json_name}',")
        code.append(f'{INDENT}{"}"}')

        code.append(f'')
        code.append(f'')
    code_str = '\n'.join(code)

    with open(MODEL_FILE_NAME, 'w') as f:
        f.write(code_str)


def generate():
    with open('./3commas_swaggerdoc.json', 'r') as f:
        swaggerdoc: Dict[str, dict] = json.loads(f.read())
        structured_code: Dict[str, list] = defaultdict(list)

        for path, definition in swaggerdoc.get('paths').items():
            split: list = path.split('/')

            http_verbs = list(definition.keys())
            endpoint_list = list(filter(lambda e: '{' not in e, split))[1:]
            version = endpoint_list.pop(0)
            endpoint = endpoint_list.pop(0)
            sub_endpoint = '_'.join(endpoint_list) if endpoint_list else ''
            path_variable_1, path_variable_2 = get_path_variables(path)

            # function_parameters = path_variable_1 or ''
            function_parameters = 'id' if path_variable_1 else ''
            if path_variable_2:
                # function_parameters += f', {path_variable_2}'
                function_parameters += f', sub_id'

            for verb in http_verbs:
                # function_has_payload = endpoint_consumes(verb, path)
                function_has_payload = True
                if function_has_payload:
                    function_parameters += f'{", " if function_parameters else ""}payload: dict = None'

                description = definition.get(verb).get('description')
                # operationId = definition.get(verb).get('operationId')
                parameters = definition.get(verb).get('parameters')

                function_name = f'{verb}{"_" + sub_endpoint if sub_endpoint else ""}{"_by_id" if path_variable_1 else ""}'
                return_type = endpoint_returns(verb, path)

                code = list()
                function_logic = create_function_logic(verb, path, parameters, return_type, function_has_payload)

                endpoint_found_in_py3cw = True
                if '<py3cw_entity>' in function_logic or '<py3cw_action>' in function_logic:
                    endpoint_found_in_py3cw = False
                if not endpoint_found_in_py3cw:
                    code.append("''' This endpoint was not present in the py3cw module")

                return_type_statement = ''
                if return_type:
                    return_type_statement = f' -> Tuple[ThreeCommasApiError, {return_type}]'

                code.append(f'@logged')
                code.append(f'@with_py3cw')
                code.append(f'def {function_name}({function_parameters}){return_type_statement}:')
                docstring = create_docstring(verb, path, parameters, description)
                if docstring:
                    code.append(docstring)
                code.append(function_logic)

                if not endpoint_found_in_py3cw:
                    code.append("'''")

                code.append('')
                code.append('')
                code.append('')

                structured_code[f'{version}/{endpoint}'].append('\n'.join(code))

        create_models(swaggerdoc)

        for k, v in structured_code.items():
            imports = list()
            imports.append("from py3cw.request import Py3CW")
            imports.append("from ...model import *")
            imports.append("from ...error import ThreeCommasApiError")
            imports.append("from typing import Tuple, List")
            imports.append("import logging")
            imports.append("from ...sys_utils import logged, with_py3cw, Py3cwClosure")
            imports.append("")
            imports.append("")
            imports.append("logger = logging.getLogger(__name__)")
            imports.append("wrapper: Py3cwClosure = None")
            imports.append("")
            imports.append("")
            imports.append("")
            v.insert(0, '\n'.join(imports))

        for path, c in structured_code.items():
            full_path = f'{PARENT_FOLDER_NAME}/{path}.py'
            if not os.path.exists(full_path):
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w') as f2:
                f2.write(''.join(c))

        with open(f'{PARENT_FOLDER_NAME}/__init__.py', 'w') as f3:
            f3.write('from . import ver1, v2')
            f3.write('\n')
        with open(f'{PARENT_FOLDER_NAME}/v2/__init__.py', 'w') as f4:
            f4.write('from . import smart_trades')
            f4.write('\n')
        with open(f'{PARENT_FOLDER_NAME}/ver1/__init__.py', 'w') as f5:
            f5.write('from . import accounts, bots, deals, grid_bots, marketplace, users')
            f5.write('\n')


if __name__ == '__main__':
    generate()
