from typing import List
import datetime
from model import BotEvent

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
                              ThreeCommasJsonProperty('account_id', int),
                              ThreeCommasJsonProperty('is_enabled', bool),
                              ThreeCommasJsonProperty('max_safety_orders', int),
                              ThreeCommasJsonProperty('active_safety_orders_count', int),
                              ThreeCommasJsonProperty('pairs', List[str]),
                              ThreeCommasJsonProperty('strategy_list', List[dict]),
                              ThreeCommasJsonProperty('max_active_deals', int),
                              ThreeCommasJsonProperty('active_deals_count', int),
                              ThreeCommasJsonProperty('deletable?', bool),
                              ThreeCommasJsonProperty('created_at', str, datetime.datetime),
                              ThreeCommasJsonProperty('updated_at', str, datetime.datetime),
                              ThreeCommasJsonProperty('trailing_enabled', bool),
                              ThreeCommasJsonProperty('tsl_enabled', bool),
                              ThreeCommasJsonProperty('deal_start_delay_seconds', int),
                              ThreeCommasJsonProperty('stop_loss_timeout_enabled', bool),
                              ThreeCommasJsonProperty('stop_loss_timeout_in_seconds', int),
                              # ThreeCommasJsonProperty('disable_after_deals_count', ), TODO probably int
                              # ThreeCommasJsonProperty('deals_counter', ), TODO probably int
                              ThreeCommasJsonProperty('allowed_deals_on_same_pair', int),
                              ThreeCommasJsonProperty('easy_form_supported', bool),
                              # ThreeCommasJsonProperty('close_deals_timeout', ), TODO probably int
                              ThreeCommasJsonProperty('url_secret', str),
                              ThreeCommasJsonProperty('name', str),
                              ThreeCommasJsonProperty('take_profit', str, float),
                              ThreeCommasJsonProperty('base_order_volume', str, float),
                              ThreeCommasJsonProperty('safety_order_volume', str, float),
                              ThreeCommasJsonProperty('safety_order_step_percentage', str, float),
                              ThreeCommasJsonProperty('take_profit_type', str),
                              ThreeCommasJsonProperty('type', str),
                              ThreeCommasJsonProperty('martingale_volume_coefficient', str, float),
                              ThreeCommasJsonProperty('martingale_step_coefficient', str, float),
                              ThreeCommasJsonProperty('stop_loss_percentage', str, float),
                              # ThreeCommasJsonProperty('cooldown', str, ), # TODO probably parsed into int, could be float
                              ThreeCommasJsonProperty('btc_price_limit', str, float),
                              ThreeCommasJsonProperty('strategy', str),
                              ThreeCommasJsonProperty('min_volume_btc_24h', str, float),
                              ThreeCommasJsonProperty('profit_currency', str),
                              # ThreeCommasJsonProperty('min_price', ), TODO probably float
                              # ThreeCommasJsonProperty('max_price', ), TODO probably float
                              ThreeCommasJsonProperty('stop_loss_type', str),
                              ThreeCommasJsonProperty('safety_order_volume_type', str),
                              ThreeCommasJsonProperty('base_order_volume_type', str),
                              ThreeCommasJsonProperty('account_name', str),
                              ThreeCommasJsonProperty('trailing_deviation', str, float),
                              ThreeCommasJsonProperty('finished_deals_profit_usd', str, float),
                              ThreeCommasJsonProperty('finished_deals_count', str, int),
                              ThreeCommasJsonProperty('leverage_type', str),
                              # ThreeCommasJsonProperty('leverage_custom_value', ),  TODO probably str
                              ThreeCommasJsonProperty('start_order_type', str),
                              ThreeCommasJsonProperty('active_deals_usd_profit', str, float),
                              # ThreeCommasJsonProperty('bot_events', , ), TODO probably complex type
                              ThreeCommasJsonProperty('bot_events', List[dict], List[BotEvent]),
                          ])
]


def generate_models():
    with open('./generated_models.py', 'w') as f:
        file_buffer = list()
        # imports
        file_buffer.append('from typing import List, Union')
        file_buffer.append('import datetime')
        file_buffer.append('from .model import OfDictClass, ThreeCommasParser')
        file_buffer.append('from . import model')

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
    initial_type_name_str = get_type_name_string(prop.initial_type)
    parsed_type_name_str = get_type_name_string(prop.parsed_type)

    getter_name = create_getter_function_name(prop)

    return_type = f'Union[{initial_type_name_str}, {parsed_type_name_str}]' if prop.parsed_type else initial_type_name_str

    file_buffer.append('')
    if prop.parsed_type is not None:
        if prop.parsed_type is datetime.datetime:
            file_buffer.append(f"{INDENT}@ThreeCommasParser.parsed_timestamp")
        elif prop.parsed_type in (int, float):
            file_buffer.append(f"{INDENT}@ThreeCommasParser.parsed({parsed_type_name_str})")
        else:
            file_buffer.append(f"{INDENT}@ThreeCommasParser.lazy_parsed({parsed_type_name_str})")
    file_buffer.append(f"{INDENT}def {getter_name}(self) -> {return_type}:")
    file_buffer.append(f"{INDENT * 2}return self.get('{property_name}')")

    return file_buffer


def create_getter_function_name(prop):
    property_variable = prop.name.replace('?', '')  # handles properties like 'deletable?'
    if prop.initial_type is bool:
        function_name = property_variable if property_variable.startswith('is_') else f'is_{property_variable}'
        function_name = function_name.replace('?', '')
    else:
        function_name = f'get_{property_variable}'
    return function_name


def create_setter_function_name(prop):
    property_variable = prop.name.replace('?', '')  # handles properties like 'deletable?'
    return f'set_{property_variable}'


def create_setter(prop: ThreeCommasJsonProperty):
    file_buffer = list()
    property_name = prop.name
    property_variable = property_name.replace('?', '')
    initial_type_name_str = get_type_name_string(prop.initial_type)

    setter_name = create_setter_function_name(prop)

    file_buffer.append('')
    file_buffer.append(f'{INDENT}def {setter_name}(self, {property_variable}: {initial_type_name_str}):')
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
