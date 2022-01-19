from typing import List, Union
import datetime
from .model import OfDictClass, ThreeCommasParser
from .enums import DealStatus, MarketCode
from . import model


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

	def set_take_profit(self, take_profit: str):
		self['take_profit'] = take_profit

	@ThreeCommasParser.parsed(float)
	def get_base_order_volume(self) -> Union[str, float]:
		return self.get('base_order_volume')

	def set_base_order_volume(self, base_order_volume: str):
		self['base_order_volume'] = base_order_volume

	@ThreeCommasParser.parsed(float)
	def get_safety_order_volume(self) -> Union[str, float]:
		return self.get('safety_order_volume')

	def set_safety_order_volume(self, safety_order_volume: str):
		self['safety_order_volume'] = safety_order_volume

	@ThreeCommasParser.parsed(float)
	def get_safety_order_step_percentage(self) -> Union[str, float]:
		return self.get('safety_order_step_percentage')

	def set_safety_order_step_percentage(self, safety_order_step_percentage: str):
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

	def set_martingale_volume_coefficient(self, martingale_volume_coefficient: str):
		self['martingale_volume_coefficient'] = martingale_volume_coefficient

	@ThreeCommasParser.parsed(float)
	def get_martingale_step_coefficient(self) -> Union[str, float]:
		return self.get('martingale_step_coefficient')

	def set_martingale_step_coefficient(self, martingale_step_coefficient: str):
		self['martingale_step_coefficient'] = martingale_step_coefficient

	@ThreeCommasParser.parsed(float)
	def get_stop_loss_percentage(self) -> Union[str, float]:
		return self.get('stop_loss_percentage')

	def set_stop_loss_percentage(self, stop_loss_percentage: str):
		self['stop_loss_percentage'] = stop_loss_percentage

	@ThreeCommasParser.parsed(float)
	def get_btc_price_limit(self) -> Union[str, float]:
		return self.get('btc_price_limit')

	def set_btc_price_limit(self, btc_price_limit: str):
		self['btc_price_limit'] = btc_price_limit

	def get_strategy(self) -> str:
		return self.get('strategy')

	def set_strategy(self, strategy: str):
		self['strategy'] = strategy

	@ThreeCommasParser.parsed(float)
	def get_min_volume_btc_24h(self) -> Union[str, float]:
		return self.get('min_volume_btc_24h')

	def set_min_volume_btc_24h(self, min_volume_btc_24h: str):
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

	def set_trailing_deviation(self, trailing_deviation: str):
		self['trailing_deviation'] = trailing_deviation

	@ThreeCommasParser.parsed(float)
	def get_finished_deals_profit_usd(self) -> Union[str, float]:
		return self.get('finished_deals_profit_usd')

	def set_finished_deals_profit_usd(self, finished_deals_profit_usd: str):
		self['finished_deals_profit_usd'] = finished_deals_profit_usd

	@ThreeCommasParser.parsed(int)
	def get_finished_deals_count(self) -> Union[str, int]:
		return self.get('finished_deals_count')

	def set_finished_deals_count(self, finished_deals_count: str):
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

	def set_active_deals_usd_profit(self, active_deals_usd_profit: str):
		self['active_deals_usd_profit'] = active_deals_usd_profit

	@ThreeCommasParser.lazy_parsed(List[model.DealShow])
	def get_active_deals(self) -> Union[List[dict], List[model.DealShow]]:
		return self.get('active_deals')

	def set_active_deals(self, active_deals: List[dict]):
		self['active_deals'] = active_deals

	@ThreeCommasParser.lazy_parsed(List[model.BotEvent])
	def get_bot_events(self) -> Union[List[dict], List[model.BotEvent]]:
		return self.get('bot_events')

	def set_bot_events(self, bot_events: List[dict]):
		self['bot_events'] = bot_events


class DealMarketOrder(OfDictClass):

	@ThreeCommasParser.parsed(int)
	def get_order_id(self) -> Union[str, int]:
		return self.get('order_id')

	def set_order_id(self, order_id: str):
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

	def set_quantity(self, quantity: str):
		self['quantity'] = quantity

	@ThreeCommasParser.parsed(float)
	def get_quantity_remaining(self) -> Union[str, float]:
		return self.get('quantity_remaining')

	def set_quantity_remaining(self, quantity_remaining: str):
		self['quantity_remaining'] = quantity_remaining

	@ThreeCommasParser.parsed(float)
	def get_total(self) -> Union[str, float]:
		return self.get('total')

	def set_total(self, total: str):
		self['total'] = total

	@ThreeCommasParser.parsed(float)
	def get_rate(self) -> Union[str, float]:
		return self.get('rate')

	def set_rate(self, rate: str):
		self['rate'] = rate

	@ThreeCommasParser.parsed(float)
	def get_average_price(self) -> Union[str, float]:
		return self.get('average_price')

	def set_average_price(self, average_price: str):
		self['average_price'] = average_price


class PieChartDataElement(OfDictClass):

	def get_code(self) -> str:
		return self.get('code')

	def set_code(self, code: str):
		self['code'] = code

	@ThreeCommasParser.parsed(int)
	def get_coinmarketcapid(self) -> Union[str, int]:
		return self.get('coinmarketcapid')

	def set_coinmarketcapid(self, coinmarketcapid: str):
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

	def set_btc_value(self, btc_value: str):
		self['btc_value'] = btc_value

	@ThreeCommasParser.parsed(float)
	def get_usd_value(self) -> Union[str, float]:
		return self.get('usd_value')

	def set_usd_value(self, usd_value: str):
		self['usd_value'] = usd_value

	def get_account_id(self) -> int:
		return self.get('account_id')

	def set_account_id(self, account_id: int):
		self['account_id'] = account_id


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

	def get_status(self) -> str:
		return self.get('status')

	def set_status(self, status: Union[str, DealStatus]):
		self['status'] = status

	def is_status_active(self) -> bool:
		return self.get('status') == 'active'

	def is_status_finished(self) -> bool:
		return self.get('status') == 'finished'

	def is_status_completed(self) -> bool:
		return self.get('status') == 'completed'

	def is_status_cancelled(self) -> bool:
		return self.get('status') == 'cancelled'

	def is_status_failed(self) -> bool:
		return self.get('status') == 'failed'

	def get_localized_status(self) -> str:
		return self.get('localized_status')

	def set_localized_status(self, localized_status: str):
		self['localized_status'] = localized_status

	@ThreeCommasParser.parsed(float)
	def get_take_profit(self) -> Union[str, float]:
		return self.get('take_profit')

	def set_take_profit(self, take_profit: str):
		self['take_profit'] = take_profit

	@ThreeCommasParser.parsed(float)
	def get_base_order_volume(self) -> Union[str, float]:
		return self.get('base_order_volume')

	def set_base_order_volume(self, base_order_volume: str):
		self['base_order_volume'] = base_order_volume

	@ThreeCommasParser.parsed(float)
	def get_safety_order_volume(self) -> Union[str, float]:
		return self.get('safety_order_volume')

	def set_safety_order_volume(self, safety_order_volume: str):
		self['safety_order_volume'] = safety_order_volume

	@ThreeCommasParser.parsed(float)
	def get_safety_order_step_percentage(self) -> Union[str, float]:
		return self.get('safety_order_step_percentage')

	def set_safety_order_step_percentage(self, safety_order_step_percentage: str):
		self['safety_order_step_percentage'] = safety_order_step_percentage

	def get_leverage_type(self) -> str:
		return self.get('leverage_type')

	def set_leverage_type(self, leverage_type: str):
		self['leverage_type'] = leverage_type

	@ThreeCommasParser.parsed(float)
	def get_bought_amount(self) -> Union[str, float]:
		return self.get('bought_amount')

	def set_bought_amount(self, bought_amount: str):
		self['bought_amount'] = bought_amount

	@ThreeCommasParser.parsed(float)
	def get_bought_volume(self) -> Union[str, float]:
		return self.get('bought_volume')

	def set_bought_volume(self, bought_volume: str):
		self['bought_volume'] = bought_volume

	@ThreeCommasParser.parsed(float)
	def get_bought_average_price(self) -> Union[str, float]:
		return self.get('bought_average_price')

	def set_bought_average_price(self, bought_average_price: str):
		self['bought_average_price'] = bought_average_price

	@ThreeCommasParser.parsed(float)
	def get_base_order_average_price(self) -> Union[str, float]:
		return self.get('base_order_average_price')

	def set_base_order_average_price(self, base_order_average_price: str):
		self['base_order_average_price'] = base_order_average_price

	@ThreeCommasParser.parsed(float)
	def get_sold_amount(self) -> Union[str, float]:
		return self.get('sold_amount')

	def set_sold_amount(self, sold_amount: str):
		self['sold_amount'] = sold_amount

	@ThreeCommasParser.parsed(float)
	def get_sold_volume(self) -> Union[str, float]:
		return self.get('sold_volume')

	def set_sold_volume(self, sold_volume: str):
		self['sold_volume'] = sold_volume

	@ThreeCommasParser.parsed(float)
	def get_sold_average_price(self) -> Union[str, float]:
		return self.get('sold_average_price')

	def set_sold_average_price(self, sold_average_price: str):
		self['sold_average_price'] = sold_average_price

	def get_take_profit_type(self) -> str:
		return self.get('take_profit_type')

	def set_take_profit_type(self, take_profit_type: str):
		self['take_profit_type'] = take_profit_type

	@ThreeCommasParser.parsed(float)
	def get_final_profit(self) -> Union[str, float]:
		return self.get('final_profit')

	def set_final_profit(self, final_profit: str):
		self['final_profit'] = final_profit

	@ThreeCommasParser.parsed(float)
	def get_martingale_coefficient(self) -> Union[str, float]:
		return self.get('martingale_coefficient')

	def set_martingale_coefficient(self, martingale_coefficient: str):
		self['martingale_coefficient'] = martingale_coefficient

	@ThreeCommasParser.parsed(float)
	def get_martingale_volume_coefficient(self) -> Union[str, float]:
		return self.get('martingale_volume_coefficient')

	def set_martingale_volume_coefficient(self, martingale_volume_coefficient: str):
		self['martingale_volume_coefficient'] = martingale_volume_coefficient

	@ThreeCommasParser.parsed(float)
	def get_martingale_step_coefficient(self) -> Union[str, float]:
		return self.get('martingale_step_coefficient')

	def set_martingale_step_coefficient(self, martingale_step_coefficient: str):
		self['martingale_step_coefficient'] = martingale_step_coefficient

	@ThreeCommasParser.parsed(float)
	def get_stop_loss_percentage(self) -> Union[str, float]:
		return self.get('stop_loss_percentage')

	def set_stop_loss_percentage(self, stop_loss_percentage: str):
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

	def set_current_price(self, current_price: str):
		self['current_price'] = current_price

	@ThreeCommasParser.parsed(float)
	def get_final_profit_percentage(self) -> Union[str, float]:
		return self.get('final_profit_percentage')

	def set_final_profit_percentage(self, final_profit_percentage: str):
		self['final_profit_percentage'] = final_profit_percentage

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

	def set_usd_final_profit(self, usd_final_profit: str):
		self['usd_final_profit'] = usd_final_profit

	@ThreeCommasParser.parsed(float)
	def get_actual_profit(self) -> Union[str, float]:
		return self.get('actual_profit')

	def set_actual_profit(self, actual_profit: str):
		self['actual_profit'] = actual_profit

	@ThreeCommasParser.parsed(float)
	def get_actual_usd_profit(self) -> Union[str, float]:
		return self.get('actual_usd_profit')

	def set_actual_usd_profit(self, actual_usd_profit: str):
		self['actual_usd_profit'] = actual_usd_profit

	@ThreeCommasParser.parsed(float)
	def get_reserved_base_coin(self) -> Union[str, float]:
		return self.get('reserved_base_coin')

	def set_reserved_base_coin(self, reserved_base_coin: str):
		self['reserved_base_coin'] = reserved_base_coin

	@ThreeCommasParser.parsed(float)
	def get_reserved_second_coin(self) -> Union[str, float]:
		return self.get('reserved_second_coin')

	def set_reserved_second_coin(self, reserved_second_coin: str):
		self['reserved_second_coin'] = reserved_second_coin

	@ThreeCommasParser.parsed(float)
	def get_trailing_deviation(self) -> Union[str, float]:
		return self.get('trailing_deviation')

	def set_trailing_deviation(self, trailing_deviation: str):
		self['trailing_deviation'] = trailing_deviation

	@ThreeCommasParser.parsed(float)
	def get_trailing_max_price(self) -> Union[str, float]:
		return self.get('trailing_max_price')

	def set_trailing_max_price(self, trailing_max_price: str):
		self['trailing_max_price'] = trailing_max_price

	def get_strategy(self) -> str:
		return self.get('strategy')

	def set_strategy(self, strategy: str):
		self['strategy'] = strategy

	def get_reserved_quote_funds(self) -> int:
		return self.get('reserved_quote_funds')

	def set_reserved_quote_funds(self, reserved_quote_funds: int):
		self['reserved_quote_funds'] = reserved_quote_funds

	@ThreeCommasParser.lazy_parsed(List[model.BotEvent])
	def get_bot_events(self) -> Union[List[dict], List[model.BotEvent]]:
		return self.get('bot_events')

	def set_bot_events(self, bot_events: List[dict]):
		self['bot_events'] = bot_events


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

	def set_btc_amount(self, btc_amount: str):
		self['btc_amount'] = btc_amount

	@ThreeCommasParser.parsed(float)
	def get_usd_amount(self) -> Union[str, float]:
		return self.get('usd_amount')

	def set_usd_amount(self, usd_amount: str):
		self['usd_amount'] = usd_amount

	@ThreeCommasParser.parsed(float)
	def get_day_profit_btc(self) -> Union[str, float]:
		return self.get('day_profit_btc')

	def set_day_profit_btc(self, day_profit_btc: str):
		self['day_profit_btc'] = day_profit_btc

	@ThreeCommasParser.parsed(float)
	def get_day_profit_usd(self) -> Union[str, float]:
		return self.get('day_profit_usd')

	def set_day_profit_usd(self, day_profit_usd: str):
		self['day_profit_usd'] = day_profit_usd

	@ThreeCommasParser.parsed(float)
	def get_day_profit_btc_percentage(self) -> Union[str, float]:
		return self.get('day_profit_btc_percentage')

	def set_day_profit_btc_percentage(self, day_profit_btc_percentage: str):
		self['day_profit_btc_percentage'] = day_profit_btc_percentage

	@ThreeCommasParser.parsed(float)
	def get_day_profit_usd_percentage(self) -> Union[str, float]:
		return self.get('day_profit_usd_percentage')

	def set_day_profit_usd_percentage(self, day_profit_usd_percentage: str):
		self['day_profit_usd_percentage'] = day_profit_usd_percentage

	@ThreeCommasParser.parsed(float)
	def get_btc_profit(self) -> Union[str, float]:
		return self.get('btc_profit')

	def set_btc_profit(self, btc_profit: str):
		self['btc_profit'] = btc_profit

	@ThreeCommasParser.parsed(float)
	def get_usd_profit(self) -> Union[str, float]:
		return self.get('usd_profit')

	def set_usd_profit(self, usd_profit: str):
		self['usd_profit'] = usd_profit

	@ThreeCommasParser.parsed(float)
	def get_usd_profit_percentage(self) -> Union[str, float]:
		return self.get('usd_profit_percentage')

	def set_usd_profit_percentage(self, usd_profit_percentage: str):
		self['usd_profit_percentage'] = usd_profit_percentage

	@ThreeCommasParser.parsed(float)
	def get_btc_profit_percentage(self) -> Union[str, float]:
		return self.get('btc_profit_percentage')

	def set_btc_profit_percentage(self, btc_profit_percentage: str):
		self['btc_profit_percentage'] = btc_profit_percentage

	@ThreeCommasParser.parsed(float)
	def get_total_btc_profit(self) -> Union[str, float]:
		return self.get('total_btc_profit')

	def set_total_btc_profit(self, total_btc_profit: str):
		self['total_btc_profit'] = total_btc_profit

	@ThreeCommasParser.parsed(float)
	def get_total_usd_profit(self) -> Union[str, float]:
		return self.get('total_usd_profit')

	def set_total_usd_profit(self, total_usd_profit: str):
		self['total_usd_profit'] = total_usd_profit

	def get_pretty_display_type(self) -> str:
		return self.get('pretty_display_type')

	def set_pretty_display_type(self, pretty_display_type: str):
		self['pretty_display_type'] = pretty_display_type

	def get_exchange_name(self) -> str:
		return self.get('exchange_name')

	def set_exchange_name(self, exchange_name: str):
		self['exchange_name'] = exchange_name

	def get_market_code(self) -> str:
		return self.get('market_code')

	def set_market_code(self, market_code: Union[str, MarketCode]):
		self['market_code'] = market_code

	def is_market_code_paper_trading(self) -> bool:
		return self.get('market_code') == 'paper_trading'

	def is_market_code_binance(self) -> bool:
		return self.get('market_code') == 'binance'

	def is_market_code_bitfinex(self) -> bool:
		return self.get('market_code') == 'bitfinex'

	def is_market_code_bitstamp(self) -> bool:
		return self.get('market_code') == 'bitstamp'

	def is_market_code_bittrex(self) -> bool:
		return self.get('market_code') == 'bittrex'

	def is_market_code_gdax(self) -> bool:
		return self.get('market_code') == 'gdax'

	def is_market_code_gemini(self) -> bool:
		return self.get('market_code') == 'gemini'

	def is_market_code_huobi(self) -> bool:
		return self.get('market_code') == 'huobi'

	def is_market_code_kucoin(self) -> bool:
		return self.get('market_code') == 'kucoin'

	def is_market_code_okex(self) -> bool:
		return self.get('market_code') == 'okex'

	def is_market_code_poloniex(self) -> bool:
		return self.get('market_code') == 'poloniex'

	def is_market_code_bitmex(self) -> bool:
		return self.get('market_code') == 'bitmex'

	def is_market_code_kraken(self) -> bool:
		return self.get('market_code') == 'kraken'

	def is_market_code_gate_io(self) -> bool:
		return self.get('market_code') == 'gate_io'

	def is_market_code_binance_margin(self) -> bool:
		return self.get('market_code') == 'binance_margin'

	def is_market_code_bybit(self) -> bool:
		return self.get('market_code') == 'bybit'

	def is_market_code_binance_us(self) -> bool:
		return self.get('market_code') == 'binance_us'

	def is_market_code_binance_futures(self) -> bool:
		return self.get('market_code') == 'binance_futures'

	def is_market_code_deribit(self) -> bool:
		return self.get('market_code') == 'deribit'

	def is_market_code_ftx(self) -> bool:
		return self.get('market_code') == 'ftx'

	def is_market_code_ftx_us(self) -> bool:
		return self.get('market_code') == 'ftx_us'

	def is_market_code_bybit_usdt_perpetual(self) -> bool:
		return self.get('market_code') == 'bybit_usdt_perpetual'

	def is_market_code_binance_futures_coin(self) -> bool:
		return self.get('market_code') == 'binance_futures_coin'

	def is_market_code_bybit_spot(self) -> bool:
		return self.get('market_code') == 'bybit_spot'

	def is_market_code_gate_io_usdt_perpetual(self) -> bool:
		return self.get('market_code') == 'gate_io_usdt_perpetual'

	def is_market_code_gate_io_btc_perpetual(self) -> bool:
		return self.get('market_code') == 'gate_io_btc_perpetual'

	def is_market_code_ethereumwallet(self) -> bool:
		return self.get('market_code') == 'ethereumwallet'

	def is_market_code_trx(self) -> bool:
		return self.get('market_code') == 'trx'
