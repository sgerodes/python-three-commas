from typing import List, Union
import datetime
from .models import * #OfDictClass, ThreeCommasParser, BotEvent
from .generated_enums import * #DealStatus, AccountMarketCode
from . import other_enums


class Deal(OfDictClass):

    @property
    def id(self) -> int:
        return self.get('id')

    @id.setter
    def id(self, id: int):
        self['id'] = id

    @property
    def type(self) -> str:
        return self.get('type')

    @type.setter
    def type(self, type: str):
        self['type'] = type

    @property
    def bot_id(self) -> int:
        return self.get('bot_id')

    @bot_id.setter
    def bot_id(self, bot_id: int):
        self['bot_id'] = bot_id

    @property
    def max_safety_orders(self) -> int:
        return self.get('max_safety_orders')

    @max_safety_orders.setter
    def max_safety_orders(self, max_safety_orders: int):
        self['max_safety_orders'] = max_safety_orders

    @property
    def deal_has_error(self) -> bool:
        return self.get('deal_has_error')

    @deal_has_error.setter
    def deal_has_error(self, deal_has_error: bool):
        self['deal_has_error'] = deal_has_error

    @property
    def account_id(self) -> int:
        return self.get('account_id')

    @account_id.setter
    def account_id(self, account_id: int):
        self['account_id'] = account_id

    @property
    def active_safety_orders_count(self) -> int:
        return self.get('active_safety_orders_count')

    @active_safety_orders_count.setter
    def active_safety_orders_count(self, active_safety_orders_count: int):
        self['active_safety_orders_count'] = active_safety_orders_count

    @property
    @ThreeCommasParser.parsed_timestamp
    def created_at(self) -> Union[str, datetime.datetime]:
        return self.get('created_at')

    @created_at.setter
    def created_at(self, created_at: str):
        self['created_at'] = created_at

    @property
    @ThreeCommasParser.parsed_timestamp
    def updated_at(self) -> Union[str, datetime.datetime]:
        return self.get('updated_at')

    @updated_at.setter
    def updated_at(self, updated_at: str):
        self['updated_at'] = updated_at

    @property
    @ThreeCommasParser.parsed_timestamp
    def closed_at(self) -> Union[str, datetime.datetime]:
        return self.get('closed_at')

    @closed_at.setter
    def closed_at(self, closed_at: str):
        self['closed_at'] = closed_at

    @property
    def finished(self) -> bool:
        return self.get('finished?')

    @finished.setter
    def finished(self, finished: bool):
        self['finished?'] = finished

    @property
    def current_active_safety_orders_count(self) -> int:
        return self.get('current_active_safety_orders_count')

    @current_active_safety_orders_count.setter
    def current_active_safety_orders_count(self, current_active_safety_orders_count: int):
        self['current_active_safety_orders_count'] = current_active_safety_orders_count

    @property
    def current_active_safety_orders(self) -> int:
        return self.get('current_active_safety_orders')

    @current_active_safety_orders.setter
    def current_active_safety_orders(self, current_active_safety_orders: int):
        self['current_active_safety_orders'] = current_active_safety_orders

    @property
    def completed_safety_orders_count(self) -> int:
        return self.get('completed_safety_orders_count')

    @completed_safety_orders_count.setter
    def completed_safety_orders_count(self, completed_safety_orders_count: int):
        self['completed_safety_orders_count'] = completed_safety_orders_count

    @property
    def completed_manual_safety_orders_count(self) -> int:
        return self.get('completed_manual_safety_orders_count')

    @completed_manual_safety_orders_count.setter
    def completed_manual_safety_orders_count(self, completed_manual_safety_orders_count: int):
        self['completed_manual_safety_orders_count'] = completed_manual_safety_orders_count

    @property
    def cancellable(self) -> bool:
        return self.get('cancellable?')

    @cancellable.setter
    def cancellable(self, cancellable: bool):
        self['cancellable?'] = cancellable

    @property
    def panic_sellable(self) -> bool:
        return self.get('panic_sellable?')

    @panic_sellable.setter
    def panic_sellable(self, panic_sellable: bool):
        self['panic_sellable?'] = panic_sellable

    @property
    def trailing_enabled(self) -> bool:
        return self.get('trailing_enabled')

    @trailing_enabled.setter
    def trailing_enabled(self, trailing_enabled: bool):
        self['trailing_enabled'] = trailing_enabled

    @property
    def tsl_enabled(self) -> bool:
        return self.get('tsl_enabled')

    @tsl_enabled.setter
    def tsl_enabled(self, tsl_enabled: bool):
        self['tsl_enabled'] = tsl_enabled

    @property
    def stop_loss_timeout_enabled(self) -> bool:
        return self.get('stop_loss_timeout_enabled')

    @stop_loss_timeout_enabled.setter
    def stop_loss_timeout_enabled(self, stop_loss_timeout_enabled: bool):
        self['stop_loss_timeout_enabled'] = stop_loss_timeout_enabled

    @property
    def stop_loss_timeout_in_seconds(self) -> int:
        return self.get('stop_loss_timeout_in_seconds')

    @stop_loss_timeout_in_seconds.setter
    def stop_loss_timeout_in_seconds(self, stop_loss_timeout_in_seconds: int):
        self['stop_loss_timeout_in_seconds'] = stop_loss_timeout_in_seconds

    @property
    def active_manual_safety_orders(self) -> int:
        return self.get('active_manual_safety_orders')

    @active_manual_safety_orders.setter
    def active_manual_safety_orders(self, active_manual_safety_orders: int):
        self['active_manual_safety_orders'] = active_manual_safety_orders

    @property
    def pair(self) -> str:
        return self.get('pair')

    @pair.setter
    def pair(self, pair: str):
        self['pair'] = pair

    @property
    @ThreeCommasParser.parsed(DealStatus)
    def status(self) -> Union[str, DealStatus]:
        return self.get('status')

    @status.setter
    def status(self, status: Union[str, DealStatus]):
        self['status'] = status

    @property
    def localized_status(self) -> str:
        return self.get('localized_status')

    @localized_status.setter
    def localized_status(self, localized_status: str):
        self['localized_status'] = localized_status

    @property
    @ThreeCommasParser.parsed(float)
    def take_profit(self) -> Union[str, float]:
        return self.get('take_profit')

    @take_profit.setter
    def take_profit(self, take_profit: Union[str, float]):
        self['take_profit'] = take_profit

    @property
    @ThreeCommasParser.parsed(float)
    def base_order_volume(self) -> Union[str, float]:
        return self.get('base_order_volume')

    @base_order_volume.setter
    def base_order_volume(self, base_order_volume: Union[str, float]):
        self['base_order_volume'] = base_order_volume

    @property
    @ThreeCommasParser.parsed(float)
    def safety_order_volume(self) -> Union[str, float]:
        return self.get('safety_order_volume')

    @safety_order_volume.setter
    def safety_order_volume(self, safety_order_volume: Union[str, float]):
        self['safety_order_volume'] = safety_order_volume

    @property
    @ThreeCommasParser.parsed(float)
    def safety_order_step_percentage(self) -> Union[str, float]:
        return self.get('safety_order_step_percentage')

    @safety_order_step_percentage.setter
    def safety_order_step_percentage(self, safety_order_step_percentage: Union[str, float]):
        self['safety_order_step_percentage'] = safety_order_step_percentage

    @property
    def leverage_type(self) -> str:
        return self.get('leverage_type')

    @leverage_type.setter
    def leverage_type(self, leverage_type: str):
        self['leverage_type'] = leverage_type

    @property
    @ThreeCommasParser.parsed(float)
    def bought_amount(self) -> Union[str, float]:
        return self.get('bought_amount')

    @bought_amount.setter
    def bought_amount(self, bought_amount: Union[str, float]):
        self['bought_amount'] = bought_amount

    @property
    @ThreeCommasParser.parsed(float)
    def bought_volume(self) -> Union[str, float]:
        return self.get('bought_volume')

    @bought_volume.setter
    def bought_volume(self, bought_volume: Union[str, float]):
        self['bought_volume'] = bought_volume

    @property
    @ThreeCommasParser.parsed(float)
    def bought_average_price(self) -> Union[str, float]:
        return self.get('bought_average_price')

    @bought_average_price.setter
    def bought_average_price(self, bought_average_price: Union[str, float]):
        self['bought_average_price'] = bought_average_price

    @property
    @ThreeCommasParser.parsed(float)
    def base_order_average_price(self) -> Union[str, float]:
        return self.get('base_order_average_price')

    @base_order_average_price.setter
    def base_order_average_price(self, base_order_average_price: Union[str, float]):
        self['base_order_average_price'] = base_order_average_price

    @property
    @ThreeCommasParser.parsed(float)
    def sold_amount(self) -> Union[str, float]:
        return self.get('sold_amount')

    @sold_amount.setter
    def sold_amount(self, sold_amount: Union[str, float]):
        self['sold_amount'] = sold_amount

    @property
    @ThreeCommasParser.parsed(float)
    def sold_volume(self) -> Union[str, float]:
        return self.get('sold_volume')

    @sold_volume.setter
    def sold_volume(self, sold_volume: Union[str, float]):
        self['sold_volume'] = sold_volume

    @property
    @ThreeCommasParser.parsed(float)
    def sold_average_price(self) -> Union[str, float]:
        return self.get('sold_average_price')

    @sold_average_price.setter
    def sold_average_price(self, sold_average_price: Union[str, float]):
        self['sold_average_price'] = sold_average_price

    @property
    def take_profit_type(self) -> str:
        return self.get('take_profit_type')

    @take_profit_type.setter
    def take_profit_type(self, take_profit_type: str):
        self['take_profit_type'] = take_profit_type

    @property
    @ThreeCommasParser.parsed(float)
    def final_profit(self) -> Union[str, float]:
        return self.get('final_profit')

    @final_profit.setter
    def final_profit(self, final_profit: Union[str, float]):
        self['final_profit'] = final_profit

    @property
    @ThreeCommasParser.parsed(float)
    def martingale_coefficient(self) -> Union[str, float]:
        return self.get('martingale_coefficient')

    @martingale_coefficient.setter
    def martingale_coefficient(self, martingale_coefficient: Union[str, float]):
        self['martingale_coefficient'] = martingale_coefficient

    @property
    @ThreeCommasParser.parsed(float)
    def martingale_volume_coefficient(self) -> Union[str, float]:
        return self.get('martingale_volume_coefficient')

    @martingale_volume_coefficient.setter
    def martingale_volume_coefficient(self, martingale_volume_coefficient: Union[str, float]):
        self['martingale_volume_coefficient'] = martingale_volume_coefficient

    @property
    @ThreeCommasParser.parsed(float)
    def martingale_step_coefficient(self) -> Union[str, float]:
        return self.get('martingale_step_coefficient')

    @martingale_step_coefficient.setter
    def martingale_step_coefficient(self, martingale_step_coefficient: Union[str, float]):
        self['martingale_step_coefficient'] = martingale_step_coefficient

    @property
    @ThreeCommasParser.parsed(float)
    def stop_loss_percentage(self) -> Union[str, float]:
        return self.get('stop_loss_percentage')

    @stop_loss_percentage.setter
    def stop_loss_percentage(self, stop_loss_percentage: Union[str, float]):
        self['stop_loss_percentage'] = stop_loss_percentage

    @property
    def profit_currency(self) -> str:
        return self.get('profit_currency')

    @profit_currency.setter
    def profit_currency(self, profit_currency: str):
        self['profit_currency'] = profit_currency

    @property
    def stop_loss_type(self) -> str:
        return self.get('stop_loss_type')

    @stop_loss_type.setter
    def stop_loss_type(self, stop_loss_type: str):
        self['stop_loss_type'] = stop_loss_type

    @property
    def safety_order_volume_type(self) -> str:
        return self.get('safety_order_volume_type')

    @safety_order_volume_type.setter
    def safety_order_volume_type(self, safety_order_volume_type: str):
        self['safety_order_volume_type'] = safety_order_volume_type

    @property
    def base_order_volume_type(self) -> str:
        return self.get('base_order_volume_type')

    @base_order_volume_type.setter
    def base_order_volume_type(self, base_order_volume_type: str):
        self['base_order_volume_type'] = base_order_volume_type

    @property
    def from_currency(self) -> str:
        return self.get('from_currency')

    @from_currency.setter
    def from_currency(self, from_currency: str):
        self['from_currency'] = from_currency

    @property
    def to_currency(self) -> str:
        return self.get('to_currency')

    @to_currency.setter
    def to_currency(self, to_currency: str):
        self['to_currency'] = to_currency

    @property
    @ThreeCommasParser.parsed(float)
    def current_price(self) -> Union[str, float]:
        return self.get('current_price')

    @current_price.setter
    def current_price(self, current_price: Union[str, float]):
        self['current_price'] = current_price

    @property
    @ThreeCommasParser.parsed(float)
    def final_profit_percentage(self) -> Union[str, float]:
        return self.get('final_profit_percentage')

    @final_profit_percentage.setter
    def final_profit_percentage(self, final_profit_percentage: Union[str, float]):
        self['final_profit_percentage'] = final_profit_percentage

    @property
    def bot_name(self) -> str:
        return self.get('bot_name')

    @bot_name.setter
    def bot_name(self, bot_name: str):
        self['bot_name'] = bot_name

    @property
    def account_name(self) -> str:
        return self.get('account_name')

    @account_name.setter
    def account_name(self, account_name: str):
        self['account_name'] = account_name

    @property
    @ThreeCommasParser.parsed(float)
    def usd_final_profit(self) -> Union[str, float]:
        return self.get('usd_final_profit')

    @usd_final_profit.setter
    def usd_final_profit(self, usd_final_profit: Union[str, float]):
        self['usd_final_profit'] = usd_final_profit

    @property
    @ThreeCommasParser.parsed(float)
    def actual_profit(self) -> Union[str, float]:
        return self.get('actual_profit')

    @actual_profit.setter
    def actual_profit(self, actual_profit: Union[str, float]):
        self['actual_profit'] = actual_profit

    @property
    @ThreeCommasParser.parsed(float)
    def actual_usd_profit(self) -> Union[str, float]:
        return self.get('actual_usd_profit')

    @actual_usd_profit.setter
    def actual_usd_profit(self, actual_usd_profit: Union[str, float]):
        self['actual_usd_profit'] = actual_usd_profit

    @property
    @ThreeCommasParser.parsed(float)
    def reserved_base_coin(self) -> Union[str, float]:
        return self.get('reserved_base_coin')

    @reserved_base_coin.setter
    def reserved_base_coin(self, reserved_base_coin: Union[str, float]):
        self['reserved_base_coin'] = reserved_base_coin

    @property
    @ThreeCommasParser.parsed(float)
    def reserved_second_coin(self) -> Union[str, float]:
        return self.get('reserved_second_coin')

    @reserved_second_coin.setter
    def reserved_second_coin(self, reserved_second_coin: Union[str, float]):
        self['reserved_second_coin'] = reserved_second_coin

    @property
    @ThreeCommasParser.parsed(float)
    def trailing_deviation(self) -> Union[str, float]:
        return self.get('trailing_deviation')

    @trailing_deviation.setter
    def trailing_deviation(self, trailing_deviation: Union[str, float]):
        self['trailing_deviation'] = trailing_deviation

    @property
    @ThreeCommasParser.parsed(float)
    def trailing_max_price(self) -> Union[str, float]:
        return self.get('trailing_max_price')

    @trailing_max_price.setter
    def trailing_max_price(self, trailing_max_price: Union[str, float]):
        self['trailing_max_price'] = trailing_max_price

    @property
    def strategy(self) -> str:
        return self.get('strategy')

    @strategy.setter
    def strategy(self, strategy: str):
        self['strategy'] = strategy

    @property
    def reserved_quote_funds(self) -> int:
        return self.get('reserved_quote_funds')

    @reserved_quote_funds.setter
    def reserved_quote_funds(self, reserved_quote_funds: int):
        self['reserved_quote_funds'] = reserved_quote_funds

    @property
    @ThreeCommasParser.lazy_parsed(List[BotEvent])
    def bot_events(self) -> Union[List[dict], List[BotEvent]]:
        return self.get('bot_events')

    @bot_events.setter
    def bot_events(self, bot_events: List[dict]):
        self['bot_events'] = bot_events


class Bot(OfDictClass):

    @property
    def id(self) -> int:
        return self.get('id')

    @id.setter
    def id(self, id: int):
        self['id'] = id

    @property
    def account_id(self) -> int:
        return self.get('account_id')

    @account_id.setter
    def account_id(self, account_id: int):
        self['account_id'] = account_id

    @property
    def is_enabled(self) -> bool:
        return self.get('is_enabled')

    @is_enabled.setter
    def is_enabled(self, is_enabled: bool):
        self['is_enabled'] = is_enabled

    @property
    def max_safety_orders(self) -> int:
        return self.get('max_safety_orders')

    @max_safety_orders.setter
    def max_safety_orders(self, max_safety_orders: int):
        self['max_safety_orders'] = max_safety_orders

    @property
    def active_safety_orders_count(self) -> int:
        return self.get('active_safety_orders_count')

    @active_safety_orders_count.setter
    def active_safety_orders_count(self, active_safety_orders_count: int):
        self['active_safety_orders_count'] = active_safety_orders_count

    @property
    def pairs(self) -> List[str]:
        return self.get('pairs')

    @pairs.setter
    def pairs(self, pairs: List[str]):
        self['pairs'] = pairs

    @property
    def strategy_list(self) -> List[dict]:
        return self.get('strategy_list')

    @strategy_list.setter
    def strategy_list(self, strategy_list: List[dict]):
        self['strategy_list'] = strategy_list

    @property
    def max_active_deals(self) -> int:
        return self.get('max_active_deals')

    @max_active_deals.setter
    def max_active_deals(self, max_active_deals: int):
        self['max_active_deals'] = max_active_deals

    @property
    def active_deals_count(self) -> int:
        return self.get('active_deals_count')

    @active_deals_count.setter
    def active_deals_count(self, active_deals_count: int):
        self['active_deals_count'] = active_deals_count

    @property
    def deletable(self) -> bool:
        return self.get('deletable?')

    @deletable.setter
    def deletable(self, deletable: bool):
        self['deletable?'] = deletable

    @property
    @ThreeCommasParser.parsed_timestamp
    def created_at(self) -> Union[str, datetime.datetime]:
        return self.get('created_at')

    @created_at.setter
    def created_at(self, created_at: str):
        self['created_at'] = created_at

    @property
    @ThreeCommasParser.parsed_timestamp
    def updated_at(self) -> Union[str, datetime.datetime]:
        return self.get('updated_at')

    @updated_at.setter
    def updated_at(self, updated_at: str):
        self['updated_at'] = updated_at

    @property
    def trailing_enabled(self) -> bool:
        return self.get('trailing_enabled')

    @trailing_enabled.setter
    def trailing_enabled(self, trailing_enabled: bool):
        self['trailing_enabled'] = trailing_enabled

    @property
    def tsl_enabled(self) -> bool:
        return self.get('tsl_enabled')

    @tsl_enabled.setter
    def tsl_enabled(self, tsl_enabled: bool):
        self['tsl_enabled'] = tsl_enabled

    @property
    def deal_start_delay_seconds(self) -> int:
        return self.get('deal_start_delay_seconds')

    @deal_start_delay_seconds.setter
    def deal_start_delay_seconds(self, deal_start_delay_seconds: int):
        self['deal_start_delay_seconds'] = deal_start_delay_seconds

    @property
    def stop_loss_timeout_enabled(self) -> bool:
        return self.get('stop_loss_timeout_enabled')

    @stop_loss_timeout_enabled.setter
    def stop_loss_timeout_enabled(self, stop_loss_timeout_enabled: bool):
        self['stop_loss_timeout_enabled'] = stop_loss_timeout_enabled

    @property
    def stop_loss_timeout_in_seconds(self) -> int:
        return self.get('stop_loss_timeout_in_seconds')

    @stop_loss_timeout_in_seconds.setter
    def stop_loss_timeout_in_seconds(self, stop_loss_timeout_in_seconds: int):
        self['stop_loss_timeout_in_seconds'] = stop_loss_timeout_in_seconds

    @property
    def allowed_deals_on_same_pair(self) -> int:
        return self.get('allowed_deals_on_same_pair')

    @allowed_deals_on_same_pair.setter
    def allowed_deals_on_same_pair(self, allowed_deals_on_same_pair: int):
        self['allowed_deals_on_same_pair'] = allowed_deals_on_same_pair

    @property
    def easy_form_supported(self) -> bool:
        return self.get('easy_form_supported')

    @easy_form_supported.setter
    def easy_form_supported(self, easy_form_supported: bool):
        self['easy_form_supported'] = easy_form_supported

    @property
    def url_secret(self) -> str:
        return self.get('url_secret')

    @url_secret.setter
    def url_secret(self, url_secret: str):
        self['url_secret'] = url_secret

    @property
    def name(self) -> str:
        return self.get('name')

    @name.setter
    def name(self, name: str):
        self['name'] = name

    @property
    @ThreeCommasParser.parsed(float)
    def take_profit(self) -> Union[str, float]:
        return self.get('take_profit')

    @take_profit.setter
    def take_profit(self, take_profit: Union[str, float]):
        self['take_profit'] = take_profit

    @property
    @ThreeCommasParser.parsed(float)
    def base_order_volume(self) -> Union[str, float]:
        return self.get('base_order_volume')

    @base_order_volume.setter
    def base_order_volume(self, base_order_volume: Union[str, float]):
        self['base_order_volume'] = base_order_volume

    @property
    @ThreeCommasParser.parsed(float)
    def safety_order_volume(self) -> Union[str, float]:
        return self.get('safety_order_volume')

    @safety_order_volume.setter
    def safety_order_volume(self, safety_order_volume: Union[str, float]):
        self['safety_order_volume'] = safety_order_volume

    @property
    @ThreeCommasParser.parsed(float)
    def safety_order_step_percentage(self) -> Union[str, float]:
        return self.get('safety_order_step_percentage')

    @safety_order_step_percentage.setter
    def safety_order_step_percentage(self, safety_order_step_percentage: Union[str, float]):
        self['safety_order_step_percentage'] = safety_order_step_percentage

    @property
    def take_profit_type(self) -> str:
        return self.get('take_profit_type')

    @take_profit_type.setter
    def take_profit_type(self, take_profit_type: str):
        self['take_profit_type'] = take_profit_type

    @property
    def type(self) -> str:
        return self.get('type')

    @type.setter
    def type(self, type: str):
        self['type'] = type

    @property
    @ThreeCommasParser.parsed(float)
    def martingale_volume_coefficient(self) -> Union[str, float]:
        return self.get('martingale_volume_coefficient')

    @martingale_volume_coefficient.setter
    def martingale_volume_coefficient(self, martingale_volume_coefficient: Union[str, float]):
        self['martingale_volume_coefficient'] = martingale_volume_coefficient

    @property
    @ThreeCommasParser.parsed(float)
    def martingale_step_coefficient(self) -> Union[str, float]:
        return self.get('martingale_step_coefficient')

    @martingale_step_coefficient.setter
    def martingale_step_coefficient(self, martingale_step_coefficient: Union[str, float]):
        self['martingale_step_coefficient'] = martingale_step_coefficient

    @property
    @ThreeCommasParser.parsed(float)
    def stop_loss_percentage(self) -> Union[str, float]:
        return self.get('stop_loss_percentage')

    @stop_loss_percentage.setter
    def stop_loss_percentage(self, stop_loss_percentage: Union[str, float]):
        self['stop_loss_percentage'] = stop_loss_percentage

    @property
    @ThreeCommasParser.parsed(float)
    def btc_price_limit(self) -> Union[str, float]:
        return self.get('btc_price_limit')

    @btc_price_limit.setter
    def btc_price_limit(self, btc_price_limit: Union[str, float]):
        self['btc_price_limit'] = btc_price_limit

    @property
    def strategy(self) -> str:
        return self.get('strategy')

    @strategy.setter
    def strategy(self, strategy: str):
        self['strategy'] = strategy

    @property
    @ThreeCommasParser.parsed(float)
    def min_volume_btc_24h(self) -> Union[str, float]:
        return self.get('min_volume_btc_24h')

    @min_volume_btc_24h.setter
    def min_volume_btc_24h(self, min_volume_btc_24h: Union[str, float]):
        self['min_volume_btc_24h'] = min_volume_btc_24h

    @property
    def profit_currency(self) -> str:
        return self.get('profit_currency')

    @profit_currency.setter
    def profit_currency(self, profit_currency: str):
        self['profit_currency'] = profit_currency

    @property
    def stop_loss_type(self) -> str:
        return self.get('stop_loss_type')

    @stop_loss_type.setter
    def stop_loss_type(self, stop_loss_type: str):
        self['stop_loss_type'] = stop_loss_type

    @property
    def safety_order_volume_type(self) -> str:
        return self.get('safety_order_volume_type')

    @safety_order_volume_type.setter
    def safety_order_volume_type(self, safety_order_volume_type: str):
        self['safety_order_volume_type'] = safety_order_volume_type

    @property
    def base_order_volume_type(self) -> str:
        return self.get('base_order_volume_type')

    @base_order_volume_type.setter
    def base_order_volume_type(self, base_order_volume_type: str):
        self['base_order_volume_type'] = base_order_volume_type

    @property
    def account_name(self) -> str:
        return self.get('account_name')

    @account_name.setter
    def account_name(self, account_name: str):
        self['account_name'] = account_name

    @property
    @ThreeCommasParser.parsed(float)
    def trailing_deviation(self) -> Union[str, float]:
        return self.get('trailing_deviation')

    @trailing_deviation.setter
    def trailing_deviation(self, trailing_deviation: Union[str, float]):
        self['trailing_deviation'] = trailing_deviation

    @property
    @ThreeCommasParser.parsed(float)
    def finished_deals_profit_usd(self) -> Union[str, float]:
        return self.get('finished_deals_profit_usd')

    @finished_deals_profit_usd.setter
    def finished_deals_profit_usd(self, finished_deals_profit_usd: Union[str, float]):
        self['finished_deals_profit_usd'] = finished_deals_profit_usd

    @property
    @ThreeCommasParser.parsed(int)
    def finished_deals_count(self) -> Union[str, int]:
        return self.get('finished_deals_count')

    @finished_deals_count.setter
    def finished_deals_count(self, finished_deals_count: Union[str, int]):
        self['finished_deals_count'] = finished_deals_count

    @property
    def leverage_type(self) -> str:
        return self.get('leverage_type')

    @leverage_type.setter
    def leverage_type(self, leverage_type: str):
        self['leverage_type'] = leverage_type

    @property
    def start_order_type(self) -> str:
        return self.get('start_order_type')

    @start_order_type.setter
    def start_order_type(self, start_order_type: str):
        self['start_order_type'] = start_order_type

    @property
    @ThreeCommasParser.parsed(float)
    def active_deals_usd_profit(self) -> Union[str, float]:
        return self.get('active_deals_usd_profit')

    @active_deals_usd_profit.setter
    def active_deals_usd_profit(self, active_deals_usd_profit: Union[str, float]):
        self['active_deals_usd_profit'] = active_deals_usd_profit

    @property
    @ThreeCommasParser.lazy_parsed(List[Deal])
    def active_deals(self) -> Union[List[dict], List[Deal]]:
        return self.get('active_deals')

    @active_deals.setter
    def active_deals(self, active_deals: List[dict]):
        self['active_deals'] = active_deals

    @property
    @ThreeCommasParser.lazy_parsed(List[BotEvent])
    def bot_events(self) -> Union[List[dict], List[BotEvent]]:
        return self.get('bot_events')

    @bot_events.setter
    def bot_events(self, bot_events: List[dict]):
        self['bot_events'] = bot_events


class DealMarketOrder(OfDictClass):

    @property
    @ThreeCommasParser.parsed(int)
    def order_id(self) -> Union[str, int]:
        return self.get('order_id')

    @order_id.setter
    def order_id(self, order_id: Union[str, int]):
        self['order_id'] = order_id

    @property
    def order_type(self) -> str:
        return self.get('order_type')

    @order_type.setter
    def order_type(self, order_type: str):
        self['order_type'] = order_type

    @property
    def deal_order_type(self) -> str:
        return self.get('deal_order_type')

    @deal_order_type.setter
    def deal_order_type(self, deal_order_type: str):
        self['deal_order_type'] = deal_order_type

    @property
    def cancellable(self) -> bool:
        return self.get('cancellable')

    @cancellable.setter
    def cancellable(self, cancellable: bool):
        self['cancellable'] = cancellable

    @property
    def status_string(self) -> str:
        return self.get('status_string')

    @status_string.setter
    def status_string(self, status_string: str):
        self['status_string'] = status_string

    @property
    @ThreeCommasParser.parsed_timestamp
    def created_at(self) -> Union[str, datetime.datetime]:
        return self.get('created_at')

    @created_at.setter
    def created_at(self, created_at: str):
        self['created_at'] = created_at

    @property
    @ThreeCommasParser.parsed_timestamp
    def updated_at(self) -> Union[str, datetime.datetime]:
        return self.get('updated_at')

    @updated_at.setter
    def updated_at(self, updated_at: str):
        self['updated_at'] = updated_at

    @property
    @ThreeCommasParser.parsed(float)
    def quantity(self) -> Union[str, float]:
        return self.get('quantity')

    @quantity.setter
    def quantity(self, quantity: Union[str, float]):
        self['quantity'] = quantity

    @property
    @ThreeCommasParser.parsed(float)
    def quantity_remaining(self) -> Union[str, float]:
        return self.get('quantity_remaining')

    @quantity_remaining.setter
    def quantity_remaining(self, quantity_remaining: Union[str, float]):
        self['quantity_remaining'] = quantity_remaining

    @property
    @ThreeCommasParser.parsed(float)
    def total(self) -> Union[str, float]:
        return self.get('total')

    @total.setter
    def total(self, total: Union[str, float]):
        self['total'] = total

    @property
    @ThreeCommasParser.parsed(float)
    def rate(self) -> Union[str, float]:
        return self.get('rate')

    @rate.setter
    def rate(self, rate: Union[str, float]):
        self['rate'] = rate

    @property
    @ThreeCommasParser.parsed(float)
    def average_price(self) -> Union[str, float]:
        return self.get('average_price')

    @average_price.setter
    def average_price(self, average_price: Union[str, float]):
        self['average_price'] = average_price


class PieChartDataElement(OfDictClass):

    @property
    def code(self) -> str:
        return self.get('code')

    @code.setter
    def code(self, code: str):
        self['code'] = code

    @property
    @ThreeCommasParser.parsed(int)
    def coinmarketcapid(self) -> Union[str, int]:
        return self.get('coinmarketcapid')

    @coinmarketcapid.setter
    def coinmarketcapid(self, coinmarketcapid: Union[str, int]):
        self['coinmarketcapid'] = coinmarketcapid

    @property
    def name(self) -> str:
        return self.get('name')

    @name.setter
    def name(self, name: str):
        self['name'] = name

    @property
    def y(self) -> float:
        return self.get('y')

    @y.setter
    def y(self, y: float):
        self['y'] = y

    @property
    def percentage(self) -> float:
        return self.get('percentage')

    @percentage.setter
    def percentage(self, percentage: float):
        self['percentage'] = percentage

    @property
    def amount(self) -> float:
        return self.get('amount')

    @amount.setter
    def amount(self, amount: float):
        self['amount'] = amount

    @property
    @ThreeCommasParser.parsed(float)
    def btc_value(self) -> Union[str, float]:
        return self.get('btc_value')

    @btc_value.setter
    def btc_value(self, btc_value: Union[str, float]):
        self['btc_value'] = btc_value

    @property
    @ThreeCommasParser.parsed(float)
    def usd_value(self) -> Union[str, float]:
        return self.get('usd_value')

    @usd_value.setter
    def usd_value(self, usd_value: Union[str, float]):
        self['usd_value'] = usd_value

    @property
    def account_id(self) -> int:
        return self.get('account_id')

    @account_id.setter
    def account_id(self, account_id: int):
        self['account_id'] = account_id


class Account(OfDictClass):

    @property
    def id(self) -> int:
        return self.get('id')

    @id.setter
    def id(self, id: int):
        self['id'] = id

    @property
    def auto_balance_period(self) -> int:
        return self.get('auto_balance_period')

    @auto_balance_period.setter
    def auto_balance_period(self, auto_balance_period: int):
        self['auto_balance_period'] = auto_balance_period

    @property
    def autobalance_enabled(self) -> bool:
        return self.get('autobalance_enabled')

    @autobalance_enabled.setter
    def autobalance_enabled(self, autobalance_enabled: bool):
        self['autobalance_enabled'] = autobalance_enabled

    @property
    def hedge_mode_available(self) -> bool:
        return self.get('hedge_mode_available')

    @hedge_mode_available.setter
    def hedge_mode_available(self, hedge_mode_available: bool):
        self['hedge_mode_available'] = hedge_mode_available

    @property
    def hedge_mode_enabled(self) -> bool:
        return self.get('hedge_mode_enabled')

    @hedge_mode_enabled.setter
    def hedge_mode_enabled(self, hedge_mode_enabled: bool):
        self['hedge_mode_enabled'] = hedge_mode_enabled

    @property
    def is_locked(self) -> bool:
        return self.get('is_locked')

    @is_locked.setter
    def is_locked(self, is_locked: bool):
        self['is_locked'] = is_locked

    @property
    def smart_trading_supported(self) -> bool:
        return self.get('smart_trading_supported')

    @smart_trading_supported.setter
    def smart_trading_supported(self, smart_trading_supported: bool):
        self['smart_trading_supported'] = smart_trading_supported

    @property
    def smart_selling_supported(self) -> bool:
        return self.get('smart_selling_supported')

    @smart_selling_supported.setter
    def smart_selling_supported(self, smart_selling_supported: bool):
        self['smart_selling_supported'] = smart_selling_supported

    @property
    def stats_supported(self) -> bool:
        return self.get('stats_supported')

    @stats_supported.setter
    def stats_supported(self, stats_supported: bool):
        self['stats_supported'] = stats_supported

    @property
    def trading_supported(self) -> bool:
        return self.get('trading_supported')

    @trading_supported.setter
    def trading_supported(self, trading_supported: bool):
        self['trading_supported'] = trading_supported

    @property
    def market_buy_supported(self) -> bool:
        return self.get('market_buy_supported')

    @market_buy_supported.setter
    def market_buy_supported(self, market_buy_supported: bool):
        self['market_buy_supported'] = market_buy_supported

    @property
    def market_sell_supported(self) -> bool:
        return self.get('market_sell_supported')

    @market_sell_supported.setter
    def market_sell_supported(self, market_sell_supported: bool):
        self['market_sell_supported'] = market_sell_supported

    @property
    def conditional_buy_supported(self) -> bool:
        return self.get('conditional_buy_supported')

    @conditional_buy_supported.setter
    def conditional_buy_supported(self, conditional_buy_supported: bool):
        self['conditional_buy_supported'] = conditional_buy_supported

    @property
    def bots_allowed(self) -> bool:
        return self.get('bots_allowed')

    @bots_allowed.setter
    def bots_allowed(self, bots_allowed: bool):
        self['bots_allowed'] = bots_allowed

    @property
    def bots_ttp_allowed(self) -> bool:
        return self.get('bots_ttp_allowed')

    @bots_ttp_allowed.setter
    def bots_ttp_allowed(self, bots_ttp_allowed: bool):
        self['bots_ttp_allowed'] = bots_ttp_allowed

    @property
    def bots_tsl_allowed(self) -> bool:
        return self.get('bots_tsl_allowed')

    @bots_tsl_allowed.setter
    def bots_tsl_allowed(self, bots_tsl_allowed: bool):
        self['bots_tsl_allowed'] = bots_tsl_allowed

    @property
    def gordon_bots_available(self) -> bool:
        return self.get('gordon_bots_available')

    @gordon_bots_available.setter
    def gordon_bots_available(self, gordon_bots_available: bool):
        self['gordon_bots_available'] = gordon_bots_available

    @property
    def multi_bots_allowed(self) -> bool:
        return self.get('multi_bots_allowed')

    @multi_bots_allowed.setter
    def multi_bots_allowed(self, multi_bots_allowed: bool):
        self['multi_bots_allowed'] = multi_bots_allowed

    @property
    @ThreeCommasParser.parsed_timestamp
    def created_at(self) -> Union[str, datetime.datetime]:
        return self.get('created_at')

    @created_at.setter
    def created_at(self, created_at: str):
        self['created_at'] = created_at

    @property
    @ThreeCommasParser.parsed_timestamp
    def updated_at(self) -> Union[str, datetime.datetime]:
        return self.get('updated_at')

    @updated_at.setter
    def updated_at(self, updated_at: str):
        self['updated_at'] = updated_at

    @property
    def fast_convert_available(self) -> bool:
        return self.get('fast_convert_available')

    @fast_convert_available.setter
    def fast_convert_available(self, fast_convert_available: bool):
        self['fast_convert_available'] = fast_convert_available

    @property
    def grid_bots_allowed(self) -> bool:
        return self.get('grid_bots_allowed')

    @grid_bots_allowed.setter
    def grid_bots_allowed(self, grid_bots_allowed: bool):
        self['grid_bots_allowed'] = grid_bots_allowed

    @property
    def api_key_invalid(self) -> bool:
        return self.get('api_key_invalid')

    @api_key_invalid.setter
    def api_key_invalid(self, api_key_invalid: bool):
        self['api_key_invalid'] = api_key_invalid

    @property
    def nomics_id(self) -> str:
        return self.get('nomics_id')

    @nomics_id.setter
    def nomics_id(self, nomics_id: str):
        self['nomics_id'] = nomics_id

    @property
    def market_icon(self) -> str:
        return self.get('market_icon')

    @market_icon.setter
    def market_icon(self, market_icon: str):
        self['market_icon'] = market_icon

    @property
    def deposit_enabled(self) -> bool:
        return self.get('deposit_enabled')

    @deposit_enabled.setter
    def deposit_enabled(self, deposit_enabled: bool):
        self['deposit_enabled'] = deposit_enabled

    @property
    def supported_market_types(self) -> List[str]:
        return self.get('supported_market_types')

    @supported_market_types.setter
    def supported_market_types(self, supported_market_types: List[str]):
        self['supported_market_types'] = supported_market_types

    @property
    def api_key(self) -> str:
        return self.get('api_key')

    @api_key.setter
    def api_key(self, api_key: str):
        self['api_key'] = api_key

    @property
    def name(self) -> str:
        return self.get('name')

    @name.setter
    def name(self, name: str):
        self['name'] = name

    @property
    @ThreeCommasParser.parsed(float)
    def btc_amount(self) -> Union[str, float]:
        return self.get('btc_amount')

    @btc_amount.setter
    def btc_amount(self, btc_amount: Union[str, float]):
        self['btc_amount'] = btc_amount

    @property
    @ThreeCommasParser.parsed(float)
    def usd_amount(self) -> Union[str, float]:
        return self.get('usd_amount')

    @usd_amount.setter
    def usd_amount(self, usd_amount: Union[str, float]):
        self['usd_amount'] = usd_amount

    @property
    @ThreeCommasParser.parsed(float)
    def day_profit_btc(self) -> Union[str, float]:
        return self.get('day_profit_btc')

    @day_profit_btc.setter
    def day_profit_btc(self, day_profit_btc: Union[str, float]):
        self['day_profit_btc'] = day_profit_btc

    @property
    @ThreeCommasParser.parsed(float)
    def day_profit_usd(self) -> Union[str, float]:
        return self.get('day_profit_usd')

    @day_profit_usd.setter
    def day_profit_usd(self, day_profit_usd: Union[str, float]):
        self['day_profit_usd'] = day_profit_usd

    @property
    @ThreeCommasParser.parsed(float)
    def day_profit_btc_percentage(self) -> Union[str, float]:
        return self.get('day_profit_btc_percentage')

    @day_profit_btc_percentage.setter
    def day_profit_btc_percentage(self, day_profit_btc_percentage: Union[str, float]):
        self['day_profit_btc_percentage'] = day_profit_btc_percentage

    @property
    @ThreeCommasParser.parsed(float)
    def day_profit_usd_percentage(self) -> Union[str, float]:
        return self.get('day_profit_usd_percentage')

    @day_profit_usd_percentage.setter
    def day_profit_usd_percentage(self, day_profit_usd_percentage: Union[str, float]):
        self['day_profit_usd_percentage'] = day_profit_usd_percentage

    @property
    @ThreeCommasParser.parsed(float)
    def btc_profit(self) -> Union[str, float]:
        return self.get('btc_profit')

    @btc_profit.setter
    def btc_profit(self, btc_profit: Union[str, float]):
        self['btc_profit'] = btc_profit

    @property
    @ThreeCommasParser.parsed(float)
    def usd_profit(self) -> Union[str, float]:
        return self.get('usd_profit')

    @usd_profit.setter
    def usd_profit(self, usd_profit: Union[str, float]):
        self['usd_profit'] = usd_profit

    @property
    @ThreeCommasParser.parsed(float)
    def usd_profit_percentage(self) -> Union[str, float]:
        return self.get('usd_profit_percentage')

    @usd_profit_percentage.setter
    def usd_profit_percentage(self, usd_profit_percentage: Union[str, float]):
        self['usd_profit_percentage'] = usd_profit_percentage

    @property
    @ThreeCommasParser.parsed(float)
    def btc_profit_percentage(self) -> Union[str, float]:
        return self.get('btc_profit_percentage')

    @btc_profit_percentage.setter
    def btc_profit_percentage(self, btc_profit_percentage: Union[str, float]):
        self['btc_profit_percentage'] = btc_profit_percentage

    @property
    @ThreeCommasParser.parsed(float)
    def total_btc_profit(self) -> Union[str, float]:
        return self.get('total_btc_profit')

    @total_btc_profit.setter
    def total_btc_profit(self, total_btc_profit: Union[str, float]):
        self['total_btc_profit'] = total_btc_profit

    @property
    @ThreeCommasParser.parsed(float)
    def total_usd_profit(self) -> Union[str, float]:
        return self.get('total_usd_profit')

    @total_usd_profit.setter
    def total_usd_profit(self, total_usd_profit: Union[str, float]):
        self['total_usd_profit'] = total_usd_profit

    @property
    def pretty_display_type(self) -> str:
        return self.get('pretty_display_type')

    @pretty_display_type.setter
    def pretty_display_type(self, pretty_display_type: str):
        self['pretty_display_type'] = pretty_display_type

    @property
    def exchange_name(self) -> str:
        return self.get('exchange_name')

    @exchange_name.setter
    def exchange_name(self, exchange_name: str):
        self['exchange_name'] = exchange_name

    @property
    @ThreeCommasParser.parsed(AccountMarketCode)
    def market_code(self) -> Union[str, AccountMarketCode]:
        return self.get('market_code')

    @market_code.setter
    def market_code(self, market_code: Union[str, AccountMarketCode]):
        self['market_code'] = market_code


class PairsBlackList(OfDictClass):

    @property
    def pairs(self) -> List[str]:
        return self.get('pairs')

    @pairs.setter
    def pairs(self, pairs: List[str]):
        self['pairs'] = pairs
