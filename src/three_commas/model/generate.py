from typing import List
import datetime

INDENT = '\t'


class ThreeCommasJsonProperty:
    def __init__(self, name: str, initial_type: type, parsed_type: type = None):
        self.name = name
        self.initial_type = initial_type
        self.parsed_type = parsed_type


class ThreeCommasModelClass:
    def __init__(self, name: str, properties: List[ThreeCommasJsonProperty]):
        self.name = name
        self.properties = properties


tc_generated_classes = [
    ThreeCommasModelClass(name='BotShow',
                          properties=[
                              ThreeCommasJsonProperty('id', int),
                              ThreeCommasJsonProperty('is_enabled', bool),
                              ThreeCommasJsonProperty('deletable?', bool),
                              ThreeCommasJsonProperty('pairs', List[str]),
                              ThreeCommasJsonProperty('strategy_list', List[dict]),
                              ThreeCommasJsonProperty('created_at', str, datetime.datetime),
                              ThreeCommasJsonProperty('name', str),
                              ThreeCommasJsonProperty('take_profit', str, float),
                              ThreeCommasJsonProperty('finished_deals_count', str, int),
                          ])
]


def generate_models():
    with open('./generated_models.py', 'w') as f:
        file_buffer = list()
        # imports
        file_buffer.append('from typing import List, Union')
        file_buffer.append('import datetime')
        file_buffer.append('from .model import OfDictClass, ThreeCommasParser')

        for tc_gen_class in tc_generated_classes:
            file_buffer.append('')
            file_buffer.append('')
            file_buffer.append(f'class {tc_gen_class.name}(OfDictClass):')

        for prop in tc_gen_class.properties:
            file_buffer.extend(create_getter(prop))
            file_buffer.extend(create_setter(prop))

        file_buffer.append('')

        generated_code = '\n'.join(file_buffer)
        f.write(generated_code)


def create_getter(prop: ThreeCommasJsonProperty):
    file_buffer = list()
    property_name = prop.name
    property_variable = property_name.replace('?', '')  # handles 'deletable?'
    initial_type_name_str = get_type_name_string(prop.initial_type)
    parsed_type_name_str = get_type_name_string(prop.parsed_type)

    # function name
    if prop.initial_type is bool:
        function_name = property_variable if property_variable.startswith('is_') else f'is_{property_variable}'
        function_name = function_name.replace('?', '')
    else:
        function_name = f'get_{property_variable}'

    return_type = f'Union[{initial_type_name_str}, {parsed_type_name_str}]' if prop.parsed_type else initial_type_name_str

    file_buffer.append('')
    if prop.parsed_type is not None:
        if prop.parsed_type is datetime.datetime:
            file_buffer.append(f"{INDENT}@ThreeCommasParser.parsed_timestamp")
        else:
            file_buffer.append(f"{INDENT}@ThreeCommasParser.parsed({parsed_type_name_str})")
    file_buffer.append(f"{INDENT}def {function_name}(self) -> {return_type}:")
    file_buffer.append(f"{INDENT * 2}return self.get('{property_name}')")

    return file_buffer


def create_setter(prop: ThreeCommasJsonProperty):
    file_buffer = list()
    property_name = prop.name
    property_variable = property_name.replace('?', '')
    initial_type_name_str = get_type_name_string(prop.initial_type)
    parsed_type_name_str = get_type_name_string(prop.parsed_type)

    file_buffer.append('')
    file_buffer.append(f'{INDENT}def set_{property_variable}(self, {property_variable}: {initial_type_name_str}):')
    file_buffer.append(f"{INDENT * 2}self['{property_name}'] = {property_variable}")

    return file_buffer


def get_type_name_string(t: type) -> str:
    if t is None:
        return None
    if 'typing' in str(type(t)):
        return str(t).replace('typing.', '')
    if t is datetime.datetime:
        return 'datetime.datetime'
    return t.__name__


if __name__ == '__main__':
    generate_models()
