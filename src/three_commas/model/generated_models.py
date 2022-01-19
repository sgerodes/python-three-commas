from typing import List, Union
import datetime
from .model import OfDictClass, ThreeCommasParser
from . import model


class BotShow(OfDictClass):

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

	@ThreeCommasParser.lazy_parsed(List[model.BotEvent])
	def get_bot_events(self) -> Union[List[dict], List[model.BotEvent]]:
		return self.get('bot_events')

	def set_bot_events(self, bot_events: List[dict]):
		self['bot_events'] = bot_events
