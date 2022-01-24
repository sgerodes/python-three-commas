import json
import os
from pathlib import Path
from typing import List, Union, Dict, Iterable

IN_PATH = './3commas_swaggerdoc.json'
OUT_FOLDER = './generated_api'
INDENT = '    '


class SwaggerJson(dict):
    def get_paths(self) -> Dict[str, dict]:
        return self.get('paths')


class PathStructure:
    def __init__(self, version, endpoint, sub_endpoint):
        self.version = version
        self.endpoint = endpoint
        self.sub_endpoint = sub_endpoint

    @staticmethod
    def of_path(api_path: str):
        if api_path.startswith('/'):
            api_path = api_path[1:]
        split = api_path.split('/')
        version = split[0]
        endpoint = split[1]
        sub_endpoint = '/'.join(split[2:])
        return PathStructure(version, endpoint, sub_endpoint)


class PathsElement:
    def __init__(self, path: str, path_definition):
        self.path = path
        self.path_structure = PathStructure.of_path(path)
        self.path_definition = path_definition


class SignatureElement:
    def __init__(self, parameter_name: str, parameter_type: str, required=None):
        self.parameter_name = parameter_name
        self.parameter_type = parameter_type
        self.default_value = required


def generate_api():
    with open(IN_PATH, 'r') as f:
        swagger_json = json.loads(f.read())
    swagger = SwaggerJson(swagger_json)
    paths = swagger.get_paths()

    create_all_folder_and_files(paths.keys())

    iteration_limit = 1
    for path, path_definition in paths.items():
        if iteration_limit <= 0:
            break
        pe = PathsElement(path, path_definition)

        for http_method in pe.path_definition.keys():
            function_name: str = create_function_name(http_method, pe)
            function_signature: str = create_function_signature(http_method, pe.path_definition)
            return_type: str = None
            description = create_description(http_method, pe, pe.path_definition)
            function_body = 'pass'

            write_function(pe, function_name, function_signature, return_type, description, function_body)

        iteration_limit -= 1


def write_function(pe: PathsElement, function_name, function_signature, return_type, description, function_body):
    with open(get_file_for_ps(pe.path_structure), 'a') as f:
        code_buffer = list()
        code_buffer.append(f"def {function_name}{function_signature}{f' -> {return_type} ' if return_type else ''}:")
        code_buffer.append(f'{INDENT}"""')
        code_buffer.append(INDENT + description)
        code_buffer.append(f'{INDENT}"""')
        code_buffer.append(f'{INDENT}{function_body}')
        code = '\n'.join(code_buffer)
        f.write(code)


def create_description(http_method: str, pe: PathsElement, path_definition: dict) -> str:
    return f"""{http_method.upper()} {pe.path}
    {path_definition.get(http_method).get('description')}"""


def create_function_name(http_method: str, pe: PathsElement) -> str:
    return f'{http_method}_{pe.path_structure.sub_endpoint}'


def create_function_signature(http_method: str, path_definition: dict) -> str:
    type_map = {
        'integer': 'int',
        'string': 'str',
        'boolean': 'bool',
        'number': 'float'
    }
    signature_elements: List[str] = list()
    parameters: List[dict] = path_definition.get(http_method).get('parameters')
    for p in parameters:
        name = p.get('name')
        typ = p.get('type')
        required = p.get('required')
        sig_element = f'{name}: {type_map.get(typ)}'
        if not required:
            sig_element += ' = None'
        signature_elements.append(sig_element)

    return f'({", ".join(signature_elements)})'


def create_folder_and_files(ps: PathStructure):
    Path(get_folder_for_ps(ps)).mkdir(parents=True, exist_ok=True)
    Path(get_file_for_ps(ps)).touch(exist_ok=True)


def get_file_for_ps(ps: PathStructure):
    return f'{OUT_FOLDER}/{ps.version}/{ps.endpoint}.py'


def get_folder_for_ps(ps: PathStructure):
    return f'{OUT_FOLDER}/{ps.version}'


def create_all_folder_and_files(paths: Iterable):
    for p in paths:
        ps = PathStructure.of_path(p)
        create_folder_and_files(ps)

if __name__ == '__main__':
    generate_api()
