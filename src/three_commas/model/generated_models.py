from typing import List, Union
import datetime
from .model import OfDictClass, ThreeCommasParser


class BotShow(OfDictClass):

	def get_id(self) -> int:
		return self.get('id')

	def set_id(self, id: int):
		self['id'] = id

	def is_enabled(self) -> bool:
		return self.get('is_enabled')

	def set_is_enabled(self, is_enabled: bool):
		self['is_enabled'] = is_enabled

	def is_deletable(self) -> bool:
		return self.get('deletable?')

	def set_deletable(self, deletable: bool):
		self['deletable?'] = deletable

	def get_pairs(self) -> List[str]:
		return self.get('pairs')

	def set_pairs(self, pairs: List[str]):
		self['pairs'] = pairs

	def get_strategy_list(self) -> List[dict]:
		return self.get('strategy_list')

	def set_strategy_list(self, strategy_list: List[dict]):
		self['strategy_list'] = strategy_list

	@ThreeCommasParser.parsed_timestamp
	def get_created_at(self) -> Union[str, datetime.datetime]:
		return self.get('created_at')

	def set_created_at(self, created_at: str):
		self['created_at'] = created_at

	def get_name(self) -> str:
		return self.get('name')

	def set_name(self, name: str):
		self['name'] = name

	@ThreeCommasParser.parsed(float)
	def get_take_profit(self) -> Union[str, float]:
		return self.get('take_profit')

	def set_take_profit(self, take_profit: str):
		self['take_profit'] = take_profit

	@ThreeCommasParser.parsed(int)
	def get_finished_deals_count(self) -> Union[str, int]:
		return self.get('finished_deals_count')

	def set_finished_deals_count(self, finished_deals_count: str):
		self['finished_deals_count'] = finished_deals_count
