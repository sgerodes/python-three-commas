from typing import List, Union
import datetime
from .models import * #OfDictClass, ThreeCommasParser, BotEvent
from .generated_enums import * #DealStatus, AccountMarketCode
from . import other_enums


class Deal(OfDictClass):

    def get_id(self) -> int:
        return self.get('id')

    def set_id(self, id: int):
        self['id'] = id

    def get_type(self) -> str:
        return self.get('type')

    def set_type(self, type: str):
        self['type'] = type

    def get_bot_id(self) -> int:
        return self.get('bot_id')

    def set_bot_id(self, bot_id: int):
        self['bot_id'] = bot_id

    def get_max_safety_orders(self) -> int:
        return self.get('max_safety_orders')

    def set_max_safety_orders(self, max_safety_orders: int):
        self['max_safety_orders'] = max_safety_orders

    def is_deal_has_error(self) -> bool:
        return self.get('deal_has_error')

    def set_deal_has_error(self, deal_has_error: bool):
        self['deal_has_error'] = deal_has_error

    def get_account_id(self) -> int:
        return self.get('account_id')

    def set_account_id(self, account_id: int):
        self['account_id'] = account_id

    def get_active_safety_orders_count(self) -> int:
        return self.get('active_safety_orders_count')

    def set_active_safety_orders_count(self, active_safety_orders_count: int):
        self['active_safety_orders_count'] = active_safety_orders_count

    @ThreeCommasParser.parsed_timestamp
    def get_created_at(self) -> Union[str, datetime.datetime]:
        return self.get('created_at')

    def set_created_at(self, created_at: str):
        self['created_at'] = created_at

    @ThreeCommasParser.parsed_timestamp
    def get_updated_at(self) -> Union[str, datetime.datetime]:
        return self.get('updated_at')

    def set_updated_at(self, updated_at: str):
        self['updated_at'] = updated_at

    @ThreeCommasParser.parsed_timestamp
    def get_closed_at(self) -> Union[str, datetime.datetime]:
        return self.get('closed_at')

    def set_closed_at(self, closed_at: str):
        self['closed_at'] = closed_at

    def is_finished(self) -> bool:
        return self.get('finished?')

    def set_finished(self, finished: bool):
        self['finished?'] = finished

    def get_current_active_safety_orders_count(self) -> int:
        return self.get('current_active_safety_orders_count')

    def set_current_active_safety_orders_count(self, current_active_safety_orders_count: int):
        self['current_active_safety_orders_count'] = current_active_safety_orders_count

    def get_current_active_safety_orders(self) -> int:
        return self.get('current_active_safety_orders')

    def set_current_active_safety_orders(self, current_active_safety_orders: int):
        self['current_active_safety_orders'] = current_active_safety_orders

    def get_completed_safety_orders_count(self) -> int:
        return self.get('completed_safety_orders_count')

    def set_completed_safety_orders_count(self, completed_safety_orders_count: int):
        self['completed_safety_orders_count'] = completed_safety_orders_count

    def get_completed_manual_safety_orders_count(self) -> int:
        return self.get('completed_manual_safety_orders_count')

    def set_completed_manual_safety_orders_count(self, completed_manual_safety_orders_count: int):
        self['completed_manual_safety_orders_count'] = completed_manual_safety_orders_count

    def is_cancellable(self) -> bool:
        return self.get('cancellable?')

    def set_cancellable(self, cancellable: bool):
        self['cancellable?'] = cancellable

    def is_panic_sellable(self) -> bool:
        return self.get('panic_sellable?')

    def set_panic_sellable(self, panic_sellable: bool):
        self['panic_sellable?'] = panic_sellable

    def is_trailing_enabled(self) -> bool:
        return self.get('trailing_enabled')

    def set_trailing_enabled(self, trailing_enabled: bool):
        self['trailing_enabled'] = trailing_enabled

    def is_tsl_enabled(self) -> bool:
        return self.get('tsl_enabled')

    def set_tsl_enabled(self, tsl_enabled: bool):
        self['tsl_enabled'] = tsl_enabled

    def is_stop_loss_timeout_enabled(self) -> bool:
        return self.get('stop_loss_timeout_enabled')

    def set_stop_loss_timeout_enabled(self, stop_loss_timeout_enabled: bool):
        self['stop_loss_timeout_enabled'] = stop_loss_timeout_enabled

    def get_stop_loss_timeout_in_seconds(self) -> int:
        return self.get('stop_loss_timeout_in_seconds')

    def set_stop_loss_timeout_in_seconds(self, stop_loss_timeout_in_seconds: int):
        self['stop_loss_timeout_in_seconds'] = stop_loss_timeout_in_seconds

    def get_active_manual_safety_orders(self) -> int:
        return self.get('active_manual_safety_orders')

    def set_active_manual_safety_orders(self, active_manual_safety_orders: int):
        self['active_manual_safety_orders'] = active_manual_safety_orders

    def get_pair(self) -> str:
        return self.get('pair')

    def set_pair(self, pair: str):
        self['pair'] = pair

    @ThreeCommasParser.parsed(DealStatus)
    def get_status(self) -> Union[str, DealStatus]:
        return self.get('status')

    def set_status(self, status: Union[str, DealStatus]):
        self['status'] = status

    def get_localized_status(self) -> str:
        return self.get('localized_status')

    def set_localized_status(self, localized_status: str):
        self['localized_status'] = localized_status

    @ThreeCommasParser.parsed(float)
    def get_take_profit(self) -> Union[str, float]:
        return self.get('take_profit')

    def set_take_profit(self, take_profit: Union[str, float]):
        self['take_profit'] = take_profit

    @ThreeCommasParser.parsed(float)
    def get_base_order_volume(self) -> Union[str, float]:
        return self.get('base_order_volume')

    def set_base_order_volume(self, base_order_volume: Union[str, float]):
        self['base_order_volume'] = base_order_volume

    @ThreeCommasParser.parsed(float)
    def get_safety_order_volume(self) -> Union[str, float]:
        return self.get('safety_order_volume')

    def set_safety_order_volume(self, safety_order_volume: Union[str, float]):
        self['safety_order_volume'] = safety_order_volume

    @ThreeCommasParser.parsed(float)
    def get_safety_order_step_percentage(self) -> Union[str, float]:
        return self.get('safety_order_step_percentage')

    def set_safety_order_step_percentage(self, safety_order_step_percentage: Union[str, float]):
        self['safety_order_step_percentage'] = safety_order_step_percentage

    def get_leverage_type(self) -> str:
        return self.get('leverage_type')

    def set_leverage_type(self, leverage_type: str):
        self['leverage_type'] = leverage_type

    @ThreeCommasParser.parsed(float)
    def get_bought_amount(self) -> Union[str, float]:
        return self.get('bought_amount')

    def set_bought_amount(self, bought_amount: Union[str, float]):
        self['bought_amount'] = bought_amount

    @ThreeCommasParser.parsed(float)
    def get_bought_volume(self) -> Union[str, float]:
        return self.get('bought_volume')

    def set_bought_volume(self, bought_volume: Union[str, float]):
        self['bought_volume'] = bought_volume

    @ThreeCommasParser.parsed(float)
    def get_bought_average_price(self) -> Union[str, float]:
        return self.get('bought_average_price')

    def set_bought_average_price(self, bought_average_price: Union[str, float]):
        self['bought_average_price'] = bought_average_price

    @ThreeCommasParser.parsed(float)
    def get_base_order_average_price(self) -> Union[str, float]:
        return self.get('base_order_average_price')

    def set_base_order_average_price(self, base_order_average_price: Union[str, float]):
        self['base_order_average_price'] = base_order_average_price

    @ThreeCommasParser.parsed(float)
    def get_sold_amount(self) -> Union[str, float]:
        return self.get('sold_amount')

    def set_sold_amount(self, sold_amount: Union[str, float]):
        self['sold_amount'] = sold_amount

    @ThreeCommasParser.parsed(float)
    def get_sold_volume(self) -> Union[str, float]:
        return self.get('sold_volume')

    def set_sold_volume(self, sold_volume: Union[str, float]):
        self['sold_volume'] = sold_volume

    @ThreeCommasParser.parsed(float)
    def get_sold_average_price(self) -> Union[str, float]:
        return self.get('sold_average_price')

    def set_sold_average_price(self, sold_average_price: Union[str, float]):
        self['sold_average_price'] = sold_average_price

    def get_take_profit_type(self) -> str:
        return self.get('take_profit_type')

    def set_take_profit_type(self, take_profit_type: str):
        self['take_profit_type'] = take_profit_type

    @ThreeCommasParser.parsed(float)
    def get_final_profit(self) -> Union[str, float]:
        return self.get('final_profit')

    def set_final_profit(self, final_profit: Union[str, float]):
        self['final_profit'] = final_profit

    @ThreeCommasParser.parsed(float)
    def get_martingale_coefficient(self) -> Union[str, float]:
        return self.get('martingale_coefficient')

    def set_martingale_coefficient(self, martingale_coefficient: Union[str, float]):
        self['martingale_coefficient'] = martingale_coefficient

    @ThreeCommasParser.parsed(float)
    def get_martingale_volume_coefficient(self) -> Union[str, float]:
        return self.get('martingale_volume_coefficient')

    def set_martingale_volume_coefficient(self, martingale_volume_coefficient: Union[str, float]):
        self['martingale_volume_coefficient'] = martingale_volume_coefficient

    @ThreeCommasParser.parsed(float)
    def get_martingale_step_coefficient(self) -> Union[str, float]:
        return self.get('martingale_step_coefficient')

    def set_martingale_step_coefficient(self, martingale_step_coefficient: Union[str, float]):
        self['martingale_step_coefficient'] = martingale_step_coefficient

    @ThreeCommasParser.parsed(float)
    def get_stop_loss_percentage(self) -> Union[str, float]:
        return self.get('stop_loss_percentage')

    def set_stop_loss_percentage(self, stop_loss_percentage: Union[str, float]):
        self['stop_loss_percentage'] = stop_loss_percentage

    def get_profit_currency(self) -> str:
        return self.get('profit_currency')

    def set_profit_currency(self, profit_currency: str):
        self['profit_currency'] = profit_currency

    def get_stop_loss_type(self) -> str:
        return self.get('stop_loss_type')

    def set_stop_loss_type(self, stop_loss_type: str):
        self['stop_loss_type'] = stop_loss_type

    def get_safety_order_volume_type(self) -> str:
        return self.get('safety_order_volume_type')

    def set_safety_order_volume_type(self, safety_order_volume_type: str):
        self['safety_order_volume_type'] = safety_order_volume_type

    def get_base_order_volume_type(self) -> str:
        return self.get('base_order_volume_type')

    def set_base_order_volume_type(self, base_order_volume_type: str):
        self['base_order_volume_type'] = base_order_volume_type

    def get_from_currency(self) -> str:
        return self.get('from_currency')

    def set_from_currency(self, from_currency: str):
        self['from_currency'] = from_currency

    def get_to_currency(self) -> str:
        return self.get('to_currency')

    def set_to_currency(self, to_currency: str):
        self['to_currency'] = to_currency

    @ThreeCommasParser.parsed(float)
    def get_current_price(self) -> Union[str, float]:
        return self.get('current_price')

    def set_current_price(self, current_price: Union[str, float]):
        self['current_price'] = current_price

    @ThreeCommasParser.parsed(float)
    def get_take_profit_price(self) -> Union[str, float]:
        return self.get('take_profit_price')

    def set_take_profit_price(self, take_profit_price: Union[str, float]):
        self['take_profit_price'] = take_profit_price

    @ThreeCommasParser.parsed(float)
    def get_final_profit_percentage(self) -> Union[str, float]:
        return self.get('final_profit_percentage')

    def set_final_profit_percentage(self, final_profit_percentage: Union[str, float]):
        self['final_profit_percentage'] = final_profit_percentage

    @ThreeCommasParser.parsed(float)
    def get_actual_profit_percentage(self) -> Union[str, float]:
        return self.get('actual_profit_percentage')

    def set_actual_profit_percentage(self, actual_profit_percentage: Union[str, float]):
        self['actual_profit_percentage'] = actual_profit_percentage

    def get_bot_name(self) -> str:
        return self.get('bot_name')

    def set_bot_name(self, bot_name: str):
        self['bot_name'] = bot_name

    def get_account_name(self) -> str:
        return self.get('account_name')

    def set_account_name(self, account_name: str):
        self['account_name'] = account_name

    @ThreeCommasParser.parsed(float)
    def get_usd_final_profit(self) -> Union[str, float]:
        return self.get('usd_final_profit')

    def set_usd_final_profit(self, usd_final_profit: Union[str, float]):
        self['usd_final_profit'] = usd_final_profit

    @ThreeCommasParser.parsed(float)
    def get_actual_profit(self) -> Union[str, float]:
        return self.get('actual_profit')

    def set_actual_profit(self, actual_profit: Union[str, float]):
        self['actual_profit'] = actual_profit

    @ThreeCommasParser.parsed(float)
    def get_actual_usd_profit(self) -> Union[str, float]:
        return self.get('actual_usd_profit')

    def set_actual_usd_profit(self, actual_usd_profit: Union[str, float]):
        self['actual_usd_profit'] = actual_usd_profit

    @ThreeCommasParser.parsed(float)
    def get_reserved_base_coin(self) -> Union[str, float]:
        return self.get('reserved_base_coin')

    def set_reserved_base_coin(self, reserved_base_coin: Union[str, float]):
        self['reserved_base_coin'] = reserved_base_coin

    @ThreeCommasParser.parsed(float)
    def get_reserved_second_coin(self) -> Union[str, float]:
        return self.get('reserved_second_coin')

    def set_reserved_second_coin(self, reserved_second_coin: Union[str, float]):
        self['reserved_second_coin'] = reserved_second_coin

    @ThreeCommasParser.parsed(float)
    def get_trailing_deviation(self) -> Union[str, float]:
        return self.get('trailing_deviation')

    def set_trailing_deviation(self, trailing_deviation: Union[str, float]):
        self['trailing_deviation'] = trailing_deviation

    @ThreeCommasParser.parsed(float)
    def get_trailing_max_price(self) -> Union[str, float]:
        return self.get('trailing_max_price')

    def set_trailing_max_price(self, trailing_max_price: Union[str, float]):
        self['trailing_max_price'] = trailing_max_price

    def get_strategy(self) -> str:
        return self.get('strategy')

    def set_strategy(self, strategy: str):
        self['strategy'] = strategy

    @ThreeCommasParser.parsed(float)
    def get_reserved_quote_funds(self) -> Union[str, float]:
        return self.get('reserved_quote_funds')

    def set_reserved_quote_funds(self, reserved_quote_funds: Union[str, float]):
        self['reserved_quote_funds'] = reserved_quote_funds

    def get_buy_steps(self) -> List[dict]:
        return self.get('buy_steps')

    def set_buy_steps(self, buy_steps: List[dict]):
        self['buy_steps'] = buy_steps

    @ThreeCommasParser.lazy_parsed(List[BotEvent])
    def get_bot_events(self) -> Union[List[dict], List[BotEvent]]:
        return self.get('bot_events')

    def set_bot_events(self, bot_events: List[dict]):
        self['bot_events'] = bot_events


class Bot(OfDictClass):

    def get_id(self) -> int:
        return self.get('id')

    def set_id(self, id: int):
        self['id'] = id

    def get_account_id(self) -> int:
        return self.get('account_id')

    def set_account_id(self, account_id: int):
        self['account_id'] = account_id

    def is_enabled(self) -> bool:
        return self.get('is_enabled')

    def set_is_enabled(self, is_enabled: bool):
        self['is_enabled'] = is_enabled

    def get_max_safety_orders(self) -> int:
        return self.get('max_safety_orders')

    def set_max_safety_orders(self, max_safety_orders: int):
        self['max_safety_orders'] = max_safety_orders

    def get_active_safety_orders_count(self) -> int:
        return self.get('active_safety_orders_count')

    def set_active_safety_orders_count(self, active_safety_orders_count: int):
        self['active_safety_orders_count'] = active_safety_orders_count

    def get_pairs(self) -> List[str]:
        return self.get('pairs')

    def set_pairs(self, pairs: List[str]):
        self['pairs'] = pairs

    def get_strategy_list(self) -> List[dict]:
        return self.get('strategy_list')

    def set_strategy_list(self, strategy_list: List[dict]):
        self['strategy_list'] = strategy_list

    def get_max_active_deals(self) -> int:
        return self.get('max_active_deals')

    def set_max_active_deals(self, max_active_deals: int):
        self['max_active_deals'] = max_active_deals

    def get_active_deals_count(self) -> int:
        return self.get('active_deals_count')

    def set_active_deals_count(self, active_deals_count: int):
        self['active_deals_count'] = active_deals_count

    def is_deletable(self) -> bool:
        return self.get('deletable?')

    def set_deletable(self, deletable: bool):
        self['deletable?'] = deletable

    @ThreeCommasParser.parsed_timestamp
    def get_created_at(self) -> Union[str, datetime.datetime]:
        return self.get('created_at')

    def set_created_at(self, created_at: str):
        self['created_at'] = created_at

    @ThreeCommasParser.parsed_timestamp
    def get_updated_at(self) -> Union[str, datetime.datetime]:
        return self.get('updated_at')

    def set_updated_at(self, updated_at: str):
        self['updated_at'] = updated_at

    def is_trailing_enabled(self) -> bool:
        return self.get('trailing_enabled')

    def set_trailing_enabled(self, trailing_enabled: bool):
        self['trailing_enabled'] = trailing_enabled

    def is_tsl_enabled(self) -> bool:
        return self.get('tsl_enabled')

    def set_tsl_enabled(self, tsl_enabled: bool):
        self['tsl_enabled'] = tsl_enabled

    def get_deal_start_delay_seconds(self) -> int:
        return self.get('deal_start_delay_seconds')

    def set_deal_start_delay_seconds(self, deal_start_delay_seconds: int):
        self['deal_start_delay_seconds'] = deal_start_delay_seconds

    def is_stop_loss_timeout_enabled(self) -> bool:
        return self.get('stop_loss_timeout_enabled')

    def set_stop_loss_timeout_enabled(self, stop_loss_timeout_enabled: bool):
        self['stop_loss_timeout_enabled'] = stop_loss_timeout_enabled

    def get_stop_loss_timeout_in_seconds(self) -> int:
        return self.get('stop_loss_timeout_in_seconds')

    def set_stop_loss_timeout_in_seconds(self, stop_loss_timeout_in_seconds: int):
        self['stop_loss_timeout_in_seconds'] = stop_loss_timeout_in_seconds

    def get_allowed_deals_on_same_pair(self) -> int:
        return self.get('allowed_deals_on_same_pair')

    def set_allowed_deals_on_same_pair(self, allowed_deals_on_same_pair: int):
        self['allowed_deals_on_same_pair'] = allowed_deals_on_same_pair

    def is_easy_form_supported(self) -> bool:
        return self.get('easy_form_supported')

    def set_easy_form_supported(self, easy_form_supported: bool):
        self['easy_form_supported'] = easy_form_supported

    def get_url_secret(self) -> str:
        return self.get('url_secret')

    def set_url_secret(self, url_secret: str):
        self['url_secret'] = url_secret

    def get_name(self) -> str:
        return self.get('name')

    def set_name(self, name: str):
        self['name'] = name

    @ThreeCommasParser.parsed(float)
    def get_take_profit(self) -> Union[str, float]:
        return self.get('take_profit')

    def set_take_profit(self, take_profit: Union[str, float]):
        self['take_profit'] = take_profit

    @ThreeCommasParser.parsed(float)
    def get_base_order_volume(self) -> Union[str, float]:
        return self.get('base_order_volume')

    def set_base_order_volume(self, base_order_volume: Union[str, float]):
        self['base_order_volume'] = base_order_volume

    @ThreeCommasParser.parsed(float)
    def get_safety_order_volume(self) -> Union[str, float]:
        return self.get('safety_order_volume')

    def set_safety_order_volume(self, safety_order_volume: Union[str, float]):
        self['safety_order_volume'] = safety_order_volume

    @ThreeCommasParser.parsed(float)
    def get_safety_order_step_percentage(self) -> Union[str, float]:
        return self.get('safety_order_step_percentage')

    def set_safety_order_step_percentage(self, safety_order_step_percentage: Union[str, float]):
        self['safety_order_step_percentage'] = safety_order_step_percentage

    def get_take_profit_type(self) -> str:
        return self.get('take_profit_type')

    def set_take_profit_type(self, take_profit_type: str):
        self['take_profit_type'] = take_profit_type

    def get_type(self) -> str:
        return self.get('type')

    def set_type(self, type: str):
        self['type'] = type

    @ThreeCommasParser.parsed(float)
    def get_martingale_volume_coefficient(self) -> Union[str, float]:
        return self.get('martingale_volume_coefficient')

    def set_martingale_volume_coefficient(self, martingale_volume_coefficient: Union[str, float]):
        self['martingale_volume_coefficient'] = martingale_volume_coefficient

    @ThreeCommasParser.parsed(float)
    def get_martingale_step_coefficient(self) -> Union[str, float]:
        return self.get('martingale_step_coefficient')

    def set_martingale_step_coefficient(self, martingale_step_coefficient: Union[str, float]):
        self['martingale_step_coefficient'] = martingale_step_coefficient

    @ThreeCommasParser.parsed(float)
    def get_stop_loss_percentage(self) -> Union[str, float]:
        return self.get('stop_loss_percentage')

    def set_stop_loss_percentage(self, stop_loss_percentage: Union[str, float]):
        self['stop_loss_percentage'] = stop_loss_percentage

    @ThreeCommasParser.parsed(float)
    def get_btc_price_limit(self) -> Union[str, float]:
        return self.get('btc_price_limit')

    def set_btc_price_limit(self, btc_price_limit: Union[str, float]):
        self['btc_price_limit'] = btc_price_limit

    def get_strategy(self) -> str:
        return self.get('strategy')

    def set_strategy(self, strategy: str):
        self['strategy'] = strategy

    @ThreeCommasParser.parsed(float)
    def get_min_volume_btc_24h(self) -> Union[str, float]:
        return self.get('min_volume_btc_24h')

    def set_min_volume_btc_24h(self, min_volume_btc_24h: Union[str, float]):
        self['min_volume_btc_24h'] = min_volume_btc_24h

    def get_profit_currency(self) -> str:
        return self.get('profit_currency')

    def set_profit_currency(self, profit_currency: str):
        self['profit_currency'] = profit_currency

    def get_stop_loss_type(self) -> str:
        return self.get('stop_loss_type')

    def set_stop_loss_type(self, stop_loss_type: str):
        self['stop_loss_type'] = stop_loss_type

    def get_safety_order_volume_type(self) -> str:
        return self.get('safety_order_volume_type')

    def set_safety_order_volume_type(self, safety_order_volume_type: str):
        self['safety_order_volume_type'] = safety_order_volume_type

    def get_base_order_volume_type(self) -> str:
        return self.get('base_order_volume_type')

    def set_base_order_volume_type(self, base_order_volume_type: str):
        self['base_order_volume_type'] = base_order_volume_type

    def get_account_name(self) -> str:
        return self.get('account_name')

    def set_account_name(self, account_name: str):
        self['account_name'] = account_name

    @ThreeCommasParser.parsed(float)
    def get_trailing_deviation(self) -> Union[str, float]:
        return self.get('trailing_deviation')

    def set_trailing_deviation(self, trailing_deviation: Union[str, float]):
        self['trailing_deviation'] = trailing_deviation

    @ThreeCommasParser.parsed(float)
    def get_finished_deals_profit_usd(self) -> Union[str, float]:
        return self.get('finished_deals_profit_usd')

    def set_finished_deals_profit_usd(self, finished_deals_profit_usd: Union[str, float]):
        self['finished_deals_profit_usd'] = finished_deals_profit_usd

    @ThreeCommasParser.parsed(int)
    def get_finished_deals_count(self) -> Union[str, int]:
        return self.get('finished_deals_count')

    def set_finished_deals_count(self, finished_deals_count: Union[str, int]):
        self['finished_deals_count'] = finished_deals_count

    def get_leverage_type(self) -> str:
        return self.get('leverage_type')

    def set_leverage_type(self, leverage_type: str):
        self['leverage_type'] = leverage_type

    def get_start_order_type(self) -> str:
        return self.get('start_order_type')

    def set_start_order_type(self, start_order_type: str):
        self['start_order_type'] = start_order_type

    @ThreeCommasParser.parsed(float)
    def get_active_deals_usd_profit(self) -> Union[str, float]:
        return self.get('active_deals_usd_profit')

    def set_active_deals_usd_profit(self, active_deals_usd_profit: Union[str, float]):
        self['active_deals_usd_profit'] = active_deals_usd_profit

    @ThreeCommasParser.lazy_parsed(List[Deal])
    def get_active_deals(self) -> Union[List[dict], List[Deal]]:
        return self.get('active_deals')

    def set_active_deals(self, active_deals: List[dict]):
        self['active_deals'] = active_deals

    @ThreeCommasParser.lazy_parsed(List[BotEvent])
    def get_bot_events(self) -> Union[List[dict], List[BotEvent]]:
        return self.get('bot_events')

    def set_bot_events(self, bot_events: List[dict]):
        self['bot_events'] = bot_events


class DealMarketOrder(OfDictClass):

    @ThreeCommasParser.parsed(int)
    def get_order_id(self) -> Union[str, int]:
        return self.get('order_id')

    def set_order_id(self, order_id: Union[str, int]):
        self['order_id'] = order_id

    def get_order_type(self) -> str:
        return self.get('order_type')

    def set_order_type(self, order_type: str):
        self['order_type'] = order_type

    def get_deal_order_type(self) -> str:
        return self.get('deal_order_type')

    def set_deal_order_type(self, deal_order_type: str):
        self['deal_order_type'] = deal_order_type

    def is_cancellable(self) -> bool:
        return self.get('cancellable')

    def set_cancellable(self, cancellable: bool):
        self['cancellable'] = cancellable

    def get_status_string(self) -> str:
        return self.get('status_string')

    def set_status_string(self, status_string: str):
        self['status_string'] = status_string

    @ThreeCommasParser.parsed_timestamp
    def get_created_at(self) -> Union[str, datetime.datetime]:
        return self.get('created_at')

    def set_created_at(self, created_at: str):
        self['created_at'] = created_at

    @ThreeCommasParser.parsed_timestamp
    def get_updated_at(self) -> Union[str, datetime.datetime]:
        return self.get('updated_at')

    def set_updated_at(self, updated_at: str):
        self['updated_at'] = updated_at

    @ThreeCommasParser.parsed(float)
    def get_quantity(self) -> Union[str, float]:
        return self.get('quantity')

    def set_quantity(self, quantity: Union[str, float]):
        self['quantity'] = quantity

    @ThreeCommasParser.parsed(float)
    def get_quantity_remaining(self) -> Union[str, float]:
        return self.get('quantity_remaining')

    def set_quantity_remaining(self, quantity_remaining: Union[str, float]):
        self['quantity_remaining'] = quantity_remaining

    @ThreeCommasParser.parsed(float)
    def get_total(self) -> Union[str, float]:
        return self.get('total')

    def set_total(self, total: Union[str, float]):
        self['total'] = total

    @ThreeCommasParser.parsed(float)
    def get_rate(self) -> Union[str, float]:
        return self.get('rate')

    def set_rate(self, rate: Union[str, float]):
        self['rate'] = rate

    @ThreeCommasParser.parsed(float)
    def get_average_price(self) -> Union[str, float]:
        return self.get('average_price')

    def set_average_price(self, average_price: Union[str, float]):
        self['average_price'] = average_price


class PieChartDataElement(OfDictClass):

    def get_code(self) -> str:
        return self.get('code')

    def set_code(self, code: str):
        self['code'] = code

    @ThreeCommasParser.parsed(int)
    def get_coinmarketcapid(self) -> Union[str, int]:
        return self.get('coinmarketcapid')

    def set_coinmarketcapid(self, coinmarketcapid: Union[str, int]):
        self['coinmarketcapid'] = coinmarketcapid

    def get_name(self) -> str:
        return self.get('name')

    def set_name(self, name: str):
        self['name'] = name

    def get_y(self) -> float:
        return self.get('y')

    def set_y(self, y: float):
        self['y'] = y

    def get_percentage(self) -> float:
        return self.get('percentage')

    def set_percentage(self, percentage: float):
        self['percentage'] = percentage

    def get_amount(self) -> float:
        return self.get('amount')

    def set_amount(self, amount: float):
        self['amount'] = amount

    @ThreeCommasParser.parsed(float)
    def get_btc_value(self) -> Union[str, float]:
        return self.get('btc_value')

    def set_btc_value(self, btc_value: Union[str, float]):
        self['btc_value'] = btc_value

    @ThreeCommasParser.parsed(float)
    def get_usd_value(self) -> Union[str, float]:
        return self.get('usd_value')

    def set_usd_value(self, usd_value: Union[str, float]):
        self['usd_value'] = usd_value

    def get_account_id(self) -> int:
        return self.get('account_id')

    def set_account_id(self, account_id: int):
        self['account_id'] = account_id


class Account(OfDictClass):

    def get_id(self) -> int:
        return self.get('id')

    def set_id(self, id: int):
        self['id'] = id

    def get_auto_balance_period(self) -> int:
        return self.get('auto_balance_period')

    def set_auto_balance_period(self, auto_balance_period: int):
        self['auto_balance_period'] = auto_balance_period

    def is_autobalance_enabled(self) -> bool:
        return self.get('autobalance_enabled')

    def set_autobalance_enabled(self, autobalance_enabled: bool):
        self['autobalance_enabled'] = autobalance_enabled

    def is_hedge_mode_available(self) -> bool:
        return self.get('hedge_mode_available')

    def set_hedge_mode_available(self, hedge_mode_available: bool):
        self['hedge_mode_available'] = hedge_mode_available

    def is_hedge_mode_enabled(self) -> bool:
        return self.get('hedge_mode_enabled')

    def set_hedge_mode_enabled(self, hedge_mode_enabled: bool):
        self['hedge_mode_enabled'] = hedge_mode_enabled

    def is_locked(self) -> bool:
        return self.get('is_locked')

    def set_is_locked(self, is_locked: bool):
        self['is_locked'] = is_locked

    def is_smart_trading_supported(self) -> bool:
        return self.get('smart_trading_supported')

    def set_smart_trading_supported(self, smart_trading_supported: bool):
        self['smart_trading_supported'] = smart_trading_supported

    def is_smart_selling_supported(self) -> bool:
        return self.get('smart_selling_supported')

    def set_smart_selling_supported(self, smart_selling_supported: bool):
        self['smart_selling_supported'] = smart_selling_supported

    def is_stats_supported(self) -> bool:
        return self.get('stats_supported')

    def set_stats_supported(self, stats_supported: bool):
        self['stats_supported'] = stats_supported

    def is_trading_supported(self) -> bool:
        return self.get('trading_supported')

    def set_trading_supported(self, trading_supported: bool):
        self['trading_supported'] = trading_supported

    def is_market_buy_supported(self) -> bool:
        return self.get('market_buy_supported')

    def set_market_buy_supported(self, market_buy_supported: bool):
        self['market_buy_supported'] = market_buy_supported

    def is_market_sell_supported(self) -> bool:
        return self.get('market_sell_supported')

    def set_market_sell_supported(self, market_sell_supported: bool):
        self['market_sell_supported'] = market_sell_supported

    def is_conditional_buy_supported(self) -> bool:
        return self.get('conditional_buy_supported')

    def set_conditional_buy_supported(self, conditional_buy_supported: bool):
        self['conditional_buy_supported'] = conditional_buy_supported

    def is_bots_allowed(self) -> bool:
        return self.get('bots_allowed')

    def set_bots_allowed(self, bots_allowed: bool):
        self['bots_allowed'] = bots_allowed

    def is_bots_ttp_allowed(self) -> bool:
        return self.get('bots_ttp_allowed')

    def set_bots_ttp_allowed(self, bots_ttp_allowed: bool):
        self['bots_ttp_allowed'] = bots_ttp_allowed

    def is_bots_tsl_allowed(self) -> bool:
        return self.get('bots_tsl_allowed')

    def set_bots_tsl_allowed(self, bots_tsl_allowed: bool):
        self['bots_tsl_allowed'] = bots_tsl_allowed

    def is_gordon_bots_available(self) -> bool:
        return self.get('gordon_bots_available')

    def set_gordon_bots_available(self, gordon_bots_available: bool):
        self['gordon_bots_available'] = gordon_bots_available

    def is_multi_bots_allowed(self) -> bool:
        return self.get('multi_bots_allowed')

    def set_multi_bots_allowed(self, multi_bots_allowed: bool):
        self['multi_bots_allowed'] = multi_bots_allowed

    @ThreeCommasParser.parsed_timestamp
    def get_created_at(self) -> Union[str, datetime.datetime]:
        return self.get('created_at')

    def set_created_at(self, created_at: str):
        self['created_at'] = created_at

    @ThreeCommasParser.parsed_timestamp
    def get_updated_at(self) -> Union[str, datetime.datetime]:
        return self.get('updated_at')

    def set_updated_at(self, updated_at: str):
        self['updated_at'] = updated_at

    def is_fast_convert_available(self) -> bool:
        return self.get('fast_convert_available')

    def set_fast_convert_available(self, fast_convert_available: bool):
        self['fast_convert_available'] = fast_convert_available

    def is_grid_bots_allowed(self) -> bool:
        return self.get('grid_bots_allowed')

    def set_grid_bots_allowed(self, grid_bots_allowed: bool):
        self['grid_bots_allowed'] = grid_bots_allowed

    def is_api_key_invalid(self) -> bool:
        return self.get('api_key_invalid')

    def set_api_key_invalid(self, api_key_invalid: bool):
        self['api_key_invalid'] = api_key_invalid

    def get_nomics_id(self) -> str:
        return self.get('nomics_id')

    def set_nomics_id(self, nomics_id: str):
        self['nomics_id'] = nomics_id

    def get_market_icon(self) -> str:
        return self.get('market_icon')

    def set_market_icon(self, market_icon: str):
        self['market_icon'] = market_icon

    def is_deposit_enabled(self) -> bool:
        return self.get('deposit_enabled')

    def set_deposit_enabled(self, deposit_enabled: bool):
        self['deposit_enabled'] = deposit_enabled

    def get_supported_market_types(self) -> List[str]:
        return self.get('supported_market_types')

    def set_supported_market_types(self, supported_market_types: List[str]):
        self['supported_market_types'] = supported_market_types

    def get_api_key(self) -> str:
        return self.get('api_key')

    def set_api_key(self, api_key: str):
        self['api_key'] = api_key

    def get_name(self) -> str:
        return self.get('name')

    def set_name(self, name: str):
        self['name'] = name

    @ThreeCommasParser.parsed(float)
    def get_btc_amount(self) -> Union[str, float]:
        return self.get('btc_amount')

    def set_btc_amount(self, btc_amount: Union[str, float]):
        self['btc_amount'] = btc_amount

    @ThreeCommasParser.parsed(float)
    def get_usd_amount(self) -> Union[str, float]:
        return self.get('usd_amount')

    def set_usd_amount(self, usd_amount: Union[str, float]):
        self['usd_amount'] = usd_amount

    @ThreeCommasParser.parsed(float)
    def get_day_profit_btc(self) -> Union[str, float]:
        return self.get('day_profit_btc')

    def set_day_profit_btc(self, day_profit_btc: Union[str, float]):
        self['day_profit_btc'] = day_profit_btc

    @ThreeCommasParser.parsed(float)
    def get_day_profit_usd(self) -> Union[str, float]:
        return self.get('day_profit_usd')

    def set_day_profit_usd(self, day_profit_usd: Union[str, float]):
        self['day_profit_usd'] = day_profit_usd

    @ThreeCommasParser.parsed(float)
    def get_day_profit_btc_percentage(self) -> Union[str, float]:
        return self.get('day_profit_btc_percentage')

    def set_day_profit_btc_percentage(self, day_profit_btc_percentage: Union[str, float]):
        self['day_profit_btc_percentage'] = day_profit_btc_percentage

    @ThreeCommasParser.parsed(float)
    def get_day_profit_usd_percentage(self) -> Union[str, float]:
        return self.get('day_profit_usd_percentage')

    def set_day_profit_usd_percentage(self, day_profit_usd_percentage: Union[str, float]):
        self['day_profit_usd_percentage'] = day_profit_usd_percentage

    @ThreeCommasParser.parsed(float)
    def get_btc_profit(self) -> Union[str, float]:
        return self.get('btc_profit')

    def set_btc_profit(self, btc_profit: Union[str, float]):
        self['btc_profit'] = btc_profit

    @ThreeCommasParser.parsed(float)
    def get_usd_profit(self) -> Union[str, float]:
        return self.get('usd_profit')

    def set_usd_profit(self, usd_profit: Union[str, float]):
        self['usd_profit'] = usd_profit

    @ThreeCommasParser.parsed(float)
    def get_usd_profit_percentage(self) -> Union[str, float]:
        return self.get('usd_profit_percentage')

    def set_usd_profit_percentage(self, usd_profit_percentage: Union[str, float]):
        self['usd_profit_percentage'] = usd_profit_percentage

    @ThreeCommasParser.parsed(float)
    def get_btc_profit_percentage(self) -> Union[str, float]:
        return self.get('btc_profit_percentage')

    def set_btc_profit_percentage(self, btc_profit_percentage: Union[str, float]):
        self['btc_profit_percentage'] = btc_profit_percentage

    @ThreeCommasParser.parsed(float)
    def get_total_btc_profit(self) -> Union[str, float]:
        return self.get('total_btc_profit')

    def set_total_btc_profit(self, total_btc_profit: Union[str, float]):
        self['total_btc_profit'] = total_btc_profit

    @ThreeCommasParser.parsed(float)
    def get_total_usd_profit(self) -> Union[str, float]:
        return self.get('total_usd_profit')

    def set_total_usd_profit(self, total_usd_profit: Union[str, float]):
        self['total_usd_profit'] = total_usd_profit

    def get_pretty_display_type(self) -> str:
        return self.get('pretty_display_type')

    def set_pretty_display_type(self, pretty_display_type: str):
        self['pretty_display_type'] = pretty_display_type

    def get_exchange_name(self) -> str:
        return self.get('exchange_name')

    def set_exchange_name(self, exchange_name: str):
        self['exchange_name'] = exchange_name

    @ThreeCommasParser.parsed(AccountMarketCode)
    def get_market_code(self) -> Union[str, AccountMarketCode]:
        return self.get('market_code')

    def set_market_code(self, market_code: Union[str, AccountMarketCode]):
        self['market_code'] = market_code


class PairsBlackList(OfDictClass):

    def get_pairs(self) -> List[str]:
        return self.get('pairs')

    def set_pairs(self, pairs: List[str]):
        self['pairs'] = pairs


class SmartTradeV2(OfDictClass):

    def get_id(self) -> int:
        return self.get('id')

    def set_id(self, id: int):
        self['id'] = id

    def get_version(self) -> int:
        return self.get('version')

    def set_version(self, version: int):
        self['version'] = version

    def get_account(self) -> dict:
        return self.get('account')

    def set_account(self, account: dict):
        self['account'] = account

    def get_pair(self) -> str:
        return self.get('pair')

    def set_pair(self, pair: str):
        self['pair'] = pair

    def is_instant(self) -> bool:
        return self.get('instant')

    def set_instant(self, instant: bool):
        self['instant'] = instant

    def get_status(self) -> dict:
        return self.get('status')

    def set_status(self, status: dict):
        self['status'] = status

    def get_leverage(self) -> dict:
        return self.get('leverage')

    def set_leverage(self, leverage: dict):
        self['leverage'] = leverage

    def get_position(self) -> dict:
        return self.get('position')

    def set_position(self, position: dict):
        self['position'] = position

    def get_take_profit(self) -> dict:
        return self.get('take_profit')

    def set_take_profit(self, take_profit: dict):
        self['take_profit'] = take_profit

    def get_stop_loss(self) -> dict:
        return self.get('stop_loss')

    def set_stop_loss(self, stop_loss: dict):
        self['stop_loss'] = stop_loss

    def get_reduce_funds(self) -> dict:
        return self.get('reduce_funds')

    def set_reduce_funds(self, reduce_funds: dict):
        self['reduce_funds'] = reduce_funds

    def get_market_close(self) -> dict:
        return self.get('market_close')

    def set_market_close(self, market_close: dict):
        self['market_close'] = market_close

    def get_note(self) -> str:
        return self.get('note')

    def set_note(self, note: str):
        self['note'] = note

    def is_skip_enter_step(self) -> bool:
        return self.get('skip_enter_step')

    def set_skip_enter_step(self, skip_enter_step: bool):
        self['skip_enter_step'] = skip_enter_step

    def get_data(self) -> dict:
        return self.get('data')

    def set_data(self, data: dict):
        self['data'] = data

    def get_profit(self) -> dict:
        return self.get('profit')

    def set_profit(self, profit: dict):
        self['profit'] = profit

    def get_margin(self) -> dict:
        return self.get('margin')

    def set_margin(self, margin: dict):
        self['margin'] = margin

    def is_position_not_filled(self) -> bool:
        return self.get('is_position_not_filled')

    def set_is_position_not_filled(self, is_position_not_filled: bool):
        self['is_position_not_filled'] = is_position_not_filled


class SmartTradeV2Trade(OfDictClass):

    def get_id(self) -> int:
        return self.get('id')

    def set_id(self, id: int):
        self['id'] = id

    @ThreeCommasParser.parsed(float)
    def get_average_price(self) -> Union[str, float]:
        return self.get('average_price')

    def set_average_price(self, average_price: Union[str, float]):
        self['average_price'] = average_price

    def get_follow_price_type(self) -> str:
        return self.get('follow_price_type')

    def set_follow_price_type(self, follow_price_type: str):
        self['follow_price_type'] = follow_price_type

    @ThreeCommasParser.parsed(float)
    def get_initial_amount(self) -> Union[str, float]:
        return self.get('initial_amount')

    def set_initial_amount(self, initial_amount: Union[str, float]):
        self['initial_amount'] = initial_amount

    @ThreeCommasParser.parsed(float)
    def get_initial_total(self) -> Union[str, float]:
        return self.get('initial_total')

    def set_initial_total(self, initial_total: Union[str, float]):
        self['initial_total'] = initial_total

    def get_order_side(self) -> str:
        return self.get('order_side')

    def set_order_side(self, order_side: str):
        self['order_side'] = order_side

    def get_order_type(self) -> str:
        return self.get('order_type')

    def set_order_type(self, order_type: str):
        self['order_type'] = order_type

    def get_pair(self) -> str:
        return self.get('pair')

    def set_pair(self, pair: str):
        self['pair'] = pair

    @ThreeCommasParser.parsed(float)
    def get_realised_amount(self) -> Union[str, float]:
        return self.get('realised_amount')

    def set_realised_amount(self, realised_amount: Union[str, float]):
        self['realised_amount'] = realised_amount

    @ThreeCommasParser.parsed(float)
    def get_realised_total(self) -> Union[str, float]:
        return self.get('realised_total')

    def set_realised_total(self, realised_total: Union[str, float]):
        self['realised_total'] = realised_total

    def get_status(self) -> str:
        return self.get('status')

    def set_status(self, status: str):
        self['status'] = status

    def get_trade_purpose(self) -> str:
        return self.get('trade_purpose')

    def set_trade_purpose(self, trade_purpose: str):
        self['trade_purpose'] = trade_purpose

    def is_trailing_enabled(self) -> bool:
        return self.get('trailing_enabled')

    def set_trailing_enabled(self, trailing_enabled: bool):
        self['trailing_enabled'] = trailing_enabled

    def get_trigger_type(self) -> str:
        return self.get('trigger_type')

    def set_trigger_type(self, trigger_type: str):
        self['trigger_type'] = trigger_type

    @ThreeCommasParser.parsed_timestamp
    def get_created_at(self) -> Union[str, datetime.datetime]:
        return self.get('created_at')

    def set_created_at(self, created_at: str):
        self['created_at'] = created_at

    @ThreeCommasParser.parsed_timestamp
    def get_updated_at(self) -> Union[str, datetime.datetime]:
        return self.get('updated_at')

    def set_updated_at(self, updated_at: str):
        self['updated_at'] = updated_at

    @ThreeCommasParser.parsed(float)
    def get_realised_percentage(self) -> Union[str, float]:
        return self.get('realised_percentage')

    def set_realised_percentage(self, realised_percentage: Union[str, float]):
        self['realised_percentage'] = realised_percentage

    @ThreeCommasParser.parsed(float)
    def get_initial_price(self) -> Union[str, float]:
        return self.get('initial_price')

    def set_initial_price(self, initial_price: Union[str, float]):
        self['initial_price'] = initial_price

    @ThreeCommasParser.parsed(float)
    def get_realised_price(self) -> Union[str, float]:
        return self.get('realised_price')

    def set_realised_price(self, realised_price: Union[str, float]):
        self['realised_price'] = realised_price

    def is_cancelable(self) -> bool:
        return self.get('cancelable')

    def set_cancelable(self, cancelable: bool):
        self['cancelable'] = cancelable

    def is_force_processable(self) -> bool:
        return self.get('force_processable')

    def set_force_processable(self, force_processable: bool):
        self['force_processable'] = force_processable
