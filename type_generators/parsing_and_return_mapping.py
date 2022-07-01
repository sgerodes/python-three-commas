import datetime
from typing import *


# {endpoint_path : str_class_to_parse_to}
ENDPOINT_PRODUCTION_MAP = {
    'GET /ver1/bots/{bot_id}/show': 'BotEntity',
    'GET /ver1/bots': 'List[BotEntity]',
    'GET /v2/smart_trades': 'List[SmartTradeV2Entity]',
    'GET /v2/smart_trades/{id}': 'SmartTradeV2Entity',
    'POST /v2/smart_trades': 'SmartTradeV2Entity',
    'GET /ver1/accounts/market_pairs': 'List[str]',
    'GET /ver1/accounts/{account_id}': 'AccountEntity',
    'POST /ver1/accounts/new': 'AccountEntity',
}


def endpoint_returns(verb: str, endpoint: str):
    return ENDPOINT_PRODUCTION_MAP.get(f'{verb.upper()} {endpoint}')


# {endpoint_path : str_class_to_consume}
ENDPOINT_CONSUMPTION_MAP = {
    'POST /v2/smart_trades': 'SmartTradeV2Entity',
    'GET /ver1/accounts/market_pairs': 'dict',
}


def endpoint_consumes(verb: str, endpoint: str):
    return ENDPOINT_CONSUMPTION_MAP.get(f'{verb.upper()} {endpoint}')

FIELD_INITIAL_TYPE_MAPPINGS = {
    'AccountEntity': {
        'supported_market_types': List[str]  # swaggerdoc states "str"
    }
}


# {name_of_model : {name_of_attr: parse_to}}
PARSING_MAPPING = {
    'DealEntity': {
        'created_at': datetime.datetime,
        'updated_at': datetime.datetime,
        'closed_at': datetime.datetime,
        'take_profit': float,
        'base_order_volume': float,
        'safety_order_volume': float,
        'safety_order_step_percentage': float,
        'bought_amount': float,
        'bought_volume': float,
        'bought_average_price': float,
        'base_order_average_price': float,
        'sold_amount': float,
        'sold_volume': float,
        'sold_average_price': float,
        'final_profit': float,
        'martingale_coefficient': float,
        'martingale_volume_coefficient': float,
        'martingale_step_coefficient': float,
        'stop_loss_percentage': float,
        'current_price': float,
        'take_profit_price': float,
        'final_profit_percentage': float,
        'actual_profit_percentage': float,
        'usd_final_profit': float,
        'actual_profit': float,
        'actual_usd_profit': float,
        'reserved_base_coin': float,
        'reserved_second_coin': float,
        'trailing_deviation': float,
        'trailing_max_price': float,
        'reserved_quote_funds': float,
        'reserved_base_funds': float,
    },
    'BotEntity': {
        'created_at': datetime.datetime,
        'updated_at': datetime.datetime,
        'take_profit': float,
        'base_order_volume': float,
        'safety_order_volume': float,
        'safety_order_step_percentage': float,
        'martingale_volume_coefficient': float,
        'martingale_step_coefficient': float,
        'stop_loss_percentage': float,
        'btc_price_limit': float,
        'min_volume_btc_24h': float,
        'trailing_deviation': float,
        'finished_deals_profit_usd': float,
        'finished_deals_count': int,
        'active_deals_usd_profit': float,
    },
    'DealMarketOrderEntity': {
        'order_id': int,
        'created_at': datetime.datetime,
        'updated_at': datetime.datetime,
        'quantity': float,
        'quantity_remaining': float,
        'total': float,
        'rate': float,
        'average_price': float,
    },
    'PieChartDataElement': {
        'coinmarketcapid': int,
        'btc_value': float,
        'usd_value': float,
    },
    'AccountEntity': {
        'created_at': datetime.datetime,
        'updated_at': datetime.datetime,
        'btc_amount': float,
        'usd_amount': float,
        'day_profit_btc': float,
        'day_profit_usd': float,
        'day_profit_btc_percentage': float,
        'day_profit_usd_percentage': float,
        'btc_profit': float,
        'usd_profit': float,
        'usd_profit_percentage': float,
        'btc_profit_percentage': float,
        'total_btc_profit': float,
        'total_usd_profit': float,
    },
    'SmartTradeV2Trade': {
        'average_price': float,
        'initial_amount': float,
        'initial_total': float,
        'realised_amount': float,
        'realised_total': float,
        'created_at': datetime.datetime,
        'updated_at': datetime.datetime,
        'realised_percentage': float,
        'initial_price': float,
        'realised_price': float,
    }
}
