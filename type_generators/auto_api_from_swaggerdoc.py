import json
from typing import Dict, List
from collections import defaultdict
from pathlib import Path
import os
from py3cw.config import API_METHODS as PY3CW_API_METHODS


INDENT = ' ' * 4
PARENT_FOLDER_NAME = 'api'
MODEL_FOLDER_NAME = 'models.py'


def get_path_variables(path: str):
    path_variables_list: list = list(filter(lambda e: '{' in e, path.split('/')))
    path_variable_1 = path_variables_list.pop(0).replace('{', '').replace('}', '') if path_variables_list else None
    path_variable_2 = path_variables_list.pop(0).replace('{', '').replace('}', '') if path_variables_list else None
    return path_variable_1, path_variable_2


def create_docstring(path: str, parameters: list, description, return_type=None):
    if not parameters and not description:
        return None

    code = list()
    code.append(f'{INDENT}"""')
    code.append(f'{INDENT}{path}')
    if description:
        code.append(f'{INDENT}{description}')
        code.append(f'')

    if parameters:
        parameters.sort(key=lambda p: p.get('required'), reverse=True)
        for p in parameters:
            _in = p.get('in')
            param_name = p.get('name')
            param_type = p.get('type')
            required = p.get('required')
            param_description = p.get('description')
            enum = p.get('enum')

            param_docstring = list()
            if required:
                param_docstring.append('REQUIRED')
            if param_type:
                param_docstring.append(param_type)
            if enum:
                param_docstring.append("values: " + str(enum))
            if param_description:
                param_docstring.append(param_description)

            code.append(f'{INDENT}:param {param_name}: ' + ', '.join(param_docstring))

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


def create_logic(verb: str, path: str, parameters: List[dict]) -> str:
    path_variable_1, path_variable_2 = get_path_variables(path)

    version = get_api_version_from_path(path)
    endpoint = get_major_endpoint_from_path(path)
    sub_path = get_sub_path(path)
    if version == 'v2':
        endpoint = 'smart_trades_v2'

    py3cw_endpoint = PY3CW_API_METHODS.get(endpoint)

    py3cw_entity = endpoint if endpoint in PY3CW_API_METHODS else '<py3cw_entity>'
    py3cw_action = '<py3cw_action>'
    print(endpoint)
    if py3cw_endpoint:
        for k, v in py3cw_endpoint.items():
            if verb.upper() == v[0] and sub_path == v[1]:
                py3cw_action = k

    code = list()
    code.append(f'{INDENT}error, data = wrapper.request(')
    code.append(f"{INDENT*2}entity='{py3cw_entity}',")
    code.append(f"{INDENT*2}action='{py3cw_action}',")
    if path_variable_1:
        code.append(f"{INDENT*2}action_id=str({path_variable_1}),")
    if path_variable_2:
        code.append(f"{INDENT*2}action_sub_id=str({path_variable_2}),")
    code.append(f"{INDENT})")

    return '\n'.join(code)


def create_models(swaggerdoc: Dict[str, dict]):
    code = list()
    for model_name, model_definition in swaggerdoc.get('definitions').items():
        code.append(f'class {model_name}:')
        code.append(f'{INDENT}pass')
        code.append(f'')
        code.append(f'')
        code_str = '\n'.join(code)

    with open(MODEL_FOLDER_NAME, 'w') as f:
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

            function_parameters = path_variable_1 or ''
            if path_variable_2:
                function_parameters += f', {path_variable_2}'
            code = list()
            for verb in http_verbs:
                description = definition.get(verb).get('description')
                # operationId = definition.get(verb).get('operationId')
                parameters = definition.get(verb).get('parameters')


                function_name = f'{verb}{"_" + sub_endpoint if sub_endpoint else ""}{"_by_" + path_variable_1 if path_variable_1 else ""}'
                return_type = f''  # TODO
                code.append(f'def {function_name}({function_parameters}):{return_type}')
                docstring = create_docstring(path, parameters, description)
                if docstring:
                    code.append(docstring)
                logic = create_logic(verb, path, parameters)
                code.append(logic)
                code.append('')
                code.append('')
                code.append('')

            structured_code[f'{version}/{endpoint}'].append('\n'.join(code))

        create_models(swaggerdoc)

        for k, v in structured_code.items():
            imports = list()
            imports.append("from py3cw.request import Py3CW")
            imports.append("from models import *")
            imports.append("")
            imports.append("")
            imports.append("wrapper = Py3CW('', '')")
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


if __name__ == '__main__':
    generate()
