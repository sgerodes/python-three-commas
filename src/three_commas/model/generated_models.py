from .models import ThreeCommasModel, StrFloatProxy, StrIntProxy, StrDatetimeProxy, QuestionMarkProxy
import datetime
from typing import Any


class IndexEntity(ThreeCommasModel):
    def __init__(self, d: dict = None):
        super().__init__(d)
        self.bots: list
        self.total: int
        self.page: int
    parsing_map = {
    }


class MarketplaceBotEntity(ThreeCommasModel):
    def __init__(self, d: dict = None):
        super().__init__(d)
        self.id: int
        self.type: str
        self.name: str
        self.strategy: str
        self.secret: str
        self.marketplace_item: None
        self.profit: None
        self.currencies: list
        self.copies: int
        self.is_favorite: bool
    parsing_map = {
    }


class MarketplaceItem(ThreeCommasModel):
    def __init__(self, d: dict = None):
        super().__init__(d)
        self.id: int
        self.name: str
        self.icon_url: str
    parsing_map = {
    }


class Profit(ThreeCommasModel):
    def __init__(self, d: dict = None):
        super().__init__(d)
        self.period: str
        self.amount: float
        self.chart_data: list
    parsing_map = {
    }


class PongEntity(ThreeCommasModel):
    def __init__(self, d: dict = None):
        super().__init__(d)
        self.pong: str
    parsing_map = {
    }


class TimeEntity(ThreeCommasModel):
    def __init__(self, d: dict = None):
        super().__init__(d)
        self.server_time: int
    parsing_map = {
    }


class BotEntity(ThreeCommasModel):
    def __init__(self, d: dict = None):
        super().__init__(d)
        self.id: int
        self.account_id: int
        self.is_enabled: bool
        self.max_safety_orders: int
        self.active_safety_orders_count: int
        self.pairs: str
        self.strategy_list: str
        self.max_active_deals: int
        self.active_deals_count: int
        self.deletable: bool
        self.created_at: StrDatetimeProxy
        self.updated_at: StrDatetimeProxy
        self.trailing_enabled: bool
        self.tsl_enabled: bool
        self.deal_start_delay_seconds: int
        self.stop_loss_timeout_enabled: bool
        self.stop_loss_timeout_in_seconds: int
        self.disable_after_deals_count: int
        self.deals_counter: int
        self.allowed_deals_on_same_pair: int
        self.easy_form_supported: bool
        self.close_deals_timeout: int
        self.url_secret: str
        self.name: str
        self.take_profit: StrFloatProxy
        self.base_order_volume: StrFloatProxy
        self.safety_order_volume: StrFloatProxy
        self.safety_order_step_percentage: StrFloatProxy
        self.take_profit_type: str
        self.type: str
        self.martingale_volume_coefficient: StrFloatProxy
        self.martingale_step_coefficient: StrFloatProxy
        self.stop_loss_percentage: StrFloatProxy
        self.cooldown: str
        self.btc_price_limit: StrFloatProxy
        self.strategy: str
        self.min_volume_btc_24h: StrFloatProxy
        self.profit_currency: str
        self.min_price: str
        self.max_price: str
        self.stop_loss_type: str
        self.safety_order_volume_type: str
        self.base_order_volume_type: str
        self.account_name: str
        self.trailing_deviation: StrFloatProxy
        self.finished_deals_profit_usd: StrFloatProxy
        self.finished_deals_count: StrIntProxy
        self.leverage_type: str
        self.leverage_custom_value: str
        self.start_order_type: str
        self.active_deals_usd_profit: StrFloatProxy
    parsing_map = {
        'deletable': QuestionMarkProxy,
        'created_at': StrDatetimeProxy,
        'updated_at': StrDatetimeProxy,
        'take_profit': StrFloatProxy,
        'base_order_volume': StrFloatProxy,
        'safety_order_volume': StrFloatProxy,
        'safety_order_step_percentage': StrFloatProxy,
        'martingale_volume_coefficient': StrFloatProxy,
        'martingale_step_coefficient': StrFloatProxy,
        'stop_loss_percentage': StrFloatProxy,
        'btc_price_limit': StrFloatProxy,
        'min_volume_btc_24h': StrFloatProxy,
        'trailing_deviation': StrFloatProxy,
        'finished_deals_profit_usd': StrFloatProxy,
        'finished_deals_count': StrIntProxy,
        'active_deals_usd_profit': StrFloatProxy,
    }


class AccountEntity(ThreeCommasModel):
    def __init__(self, d: dict = None):
        super().__init__(d)
        self.id: int
        self.auto_balance_period: int
        self.auto_balance_portfolio_id: int
        self.auto_balance_currency_change_limit: int
        self.autobalance_enabled: bool
        self.hedge_mode_available: bool
        self.hedge_mode_enabled: bool
        self.is_locked: bool
        self.smart_trading_supported: bool
        self.smart_selling_supported: bool
        self.available_for_trading: bool
        self.stats_supported: bool
        self.trading_supported: bool
        self.market_buy_supported: bool
        self.market_sell_supported: bool
        self.conditional_buy_supported: bool
        self.bots_allowed: bool
        self.bots_ttp_allowed: bool
        self.bots_tsl_allowed: bool
        self.gordon_bots_available: bool
        self.multi_bots_allowed: bool
        self.created_at: StrDatetimeProxy
        self.updated_at: StrDatetimeProxy
        self.last_auto_balance: str
        self.fast_convert_available: bool
        self.grid_bots_allowed: bool
        self.api_key_invalid: bool
        self.deposit_enabled: bool
        self.supported_market_types: str
        self.api_key: str
        self.name: str
        self.auto_balance_method: int
        self.auto_balance_error: str
        self.customer_id: str
        self.subaccount_name: str
        self.lock_reason: str
        self.btc_amount: StrFloatProxy
        self.usd_amount: StrFloatProxy
        self.day_profit_btc: StrFloatProxy
        self.day_profit_usd: StrFloatProxy
        self.day_profit_btc_percentage: StrFloatProxy
        self.day_profit_usd_percentage: StrFloatProxy
        self.btc_profit: StrFloatProxy
        self.usd_profit: StrFloatProxy
        self.usd_profit_percentage: StrFloatProxy
        self.btc_profit_percentage: StrFloatProxy
        self.total_btc_profit: StrFloatProxy
        self.total_usd_profit: StrFloatProxy
        self.pretty_display_type: str
        self.exchange_name: str
        self.market_code: str
        self.address: str
    parsing_map = {
        'created_at': StrDatetimeProxy,
        'updated_at': StrDatetimeProxy,
        'btc_amount': StrFloatProxy,
        'usd_amount': StrFloatProxy,
        'day_profit_btc': StrFloatProxy,
        'day_profit_usd': StrFloatProxy,
        'day_profit_btc_percentage': StrFloatProxy,
        'day_profit_usd_percentage': StrFloatProxy,
        'btc_profit': StrFloatProxy,
        'usd_profit': StrFloatProxy,
        'usd_profit_percentage': StrFloatProxy,
        'btc_profit_percentage': StrFloatProxy,
        'total_btc_profit': StrFloatProxy,
        'total_usd_profit': StrFloatProxy,
    }


class GridBotEntity(ThreeCommasModel):
    def __init__(self, d: dict = None):
        super().__init__(d)
        self.id: int
        self.account_id: int
        self.account_name: str
        self.is_enabled: bool
        self.grids_quantity: str
        self.created_at: str
        self.updated_at: str
        self.strategy_type: str
        self.lower_price: str
        self.upper_price: str
        self.quantity_per_grid: str
        self.leverage_type: str
        self.leverage_custom_value: str
        self.name: str
        self.pair: str
        self.start_price: str
        self.grid_price_step: str
        self.current_profit: str
        self.current_profit_usd: str
        self.total_profits_count: str
        self.bought_volume: str
        self.sold_volume: str
        self.profit_percentage: str
        self.current_price: str
        self.investment_base_currency: str
        self.investment_quote_currency: str
        self.grid_lines: None
    parsing_map = {
    }


class GridLineEntity(ThreeCommasModel):
    def __init__(self, d: dict = None):
        super().__init__(d)
        self.price: str
        self.side: str
        self.order_placed: bool
    parsing_map = {
    }


class GridBotProfitsEntity(ThreeCommasModel):
    def __init__(self, d: dict = None):
        super().__init__(d)
        self.grid_line_id: int
        self.profit: str
        self.usd_profit: str
        self.created_at: str
    parsing_map = {
    }


class DealEntity(ThreeCommasModel):
    def __init__(self, d: dict = None):
        super().__init__(d)
        self.id: int
        self.type: str
        self.bot_id: int
        self.max_safety_orders: int
        self.deal_has_error: bool
        self.from_currency_id: int
        self.to_currency_id: int
        self.account_id: int
        self.active_safety_orders_count: int
        self.created_at: StrDatetimeProxy
        self.updated_at: StrDatetimeProxy
        self.closed_at: StrDatetimeProxy
        self.finished: bool
        self.current_active_safety_orders_count: int
        self.current_active_safety_orders: int
        self.completed_safety_orders_count: int
        self.completed_manual_safety_orders_count: int
        self.cancellable: bool
        self.panic_sellable: bool
        self.trailing_enabled: bool
        self.tsl_enabled: bool
        self.stop_loss_timeout_enabled: bool
        self.stop_loss_timeout_in_seconds: int
        self.active_manual_safety_orders: int
        self.pair: str
        self.status: str
        self.localized_status: str
        self.take_profit: StrFloatProxy
        self.base_order_volume: StrFloatProxy
        self.safety_order_volume: StrFloatProxy
        self.safety_order_step_percentage: StrFloatProxy
        self.leverage_type: str
        self.leverage_custom_value: str
        self.bought_amount: StrFloatProxy
        self.bought_volume: StrFloatProxy
        self.bought_average_price: StrFloatProxy
        self.base_order_average_price: StrFloatProxy
        self.sold_amount: StrFloatProxy
        self.sold_volume: StrFloatProxy
        self.sold_average_price: StrFloatProxy
        self.take_profit_type: str
        self.final_profit: StrFloatProxy
        self.martingale_coefficient: StrFloatProxy
        self.martingale_volume_coefficient: StrFloatProxy
        self.martingale_step_coefficient: StrFloatProxy
        self.stop_loss_percentage: StrFloatProxy
        self.error_message: str
        self.profit_currency: str
        self.stop_loss_type: str
        self.safety_order_volume_type: str
        self.base_order_volume_type: str
        self.from_currency: str
        self.to_currency: str
        self.current_price: StrFloatProxy
        self.take_profit_price: StrFloatProxy
        self.stop_loss_price: str
        self.final_profit_percentage: StrFloatProxy
        self.actual_profit_percentage: StrFloatProxy
        self.bot_name: str
        self.account_name: str
        self.usd_final_profit: StrFloatProxy
        self.actual_profit: StrFloatProxy
        self.actual_usd_profit: StrFloatProxy
        self.failed_message: str
        self.reserved_base_coin: StrFloatProxy
        self.reserved_second_coin: StrFloatProxy
        self.trailing_deviation: StrFloatProxy
        self.trailing_max_price: StrFloatProxy
        self.tsl_max_price: str
        self.strategy: str
        self.reserved_quote_funds: StrFloatProxy
        self.reserved_base_funds: float
    parsing_map = {
        'created_at': StrDatetimeProxy,
        'updated_at': StrDatetimeProxy,
        'closed_at': StrDatetimeProxy,
        'finished': QuestionMarkProxy,
        'cancellable': QuestionMarkProxy,
        'panic_sellable': QuestionMarkProxy,
        'take_profit': StrFloatProxy,
        'base_order_volume': StrFloatProxy,
        'safety_order_volume': StrFloatProxy,
        'safety_order_step_percentage': StrFloatProxy,
        'bought_amount': StrFloatProxy,
        'bought_volume': StrFloatProxy,
        'bought_average_price': StrFloatProxy,
        'base_order_average_price': StrFloatProxy,
        'sold_amount': StrFloatProxy,
        'sold_volume': StrFloatProxy,
        'sold_average_price': StrFloatProxy,
        'final_profit': StrFloatProxy,
        'martingale_coefficient': StrFloatProxy,
        'martingale_volume_coefficient': StrFloatProxy,
        'martingale_step_coefficient': StrFloatProxy,
        'stop_loss_percentage': StrFloatProxy,
        'current_price': StrFloatProxy,
        'take_profit_price': StrFloatProxy,
        'final_profit_percentage': StrFloatProxy,
        'actual_profit_percentage': StrFloatProxy,
        'usd_final_profit': StrFloatProxy,
        'actual_profit': StrFloatProxy,
        'actual_usd_profit': StrFloatProxy,
        'reserved_base_coin': StrFloatProxy,
        'reserved_second_coin': StrFloatProxy,
        'trailing_deviation': StrFloatProxy,
        'trailing_max_price': StrFloatProxy,
        'reserved_quote_funds': StrFloatProxy,
    }


class SmartTradeV2Entity(ThreeCommasModel):
    def __init__(self, d: dict = None):
        super().__init__(d)
        self.id: int
        self.version: int
        self.account: dict
        self.pair: str
        self.instant: bool
        self.status: dict
        self.leverage: dict
        self.position: dict
        self.take_profit: dict
        self.stop_loss: dict
        self.note: str
        self.skip_enter_step: bool
        self.data: dict
        self.profit: dict
        self.margin: dict
        self.is_position_not_filled: bool
    parsing_map = {
    }


class TakeProfitStep(ThreeCommasModel):
    def __init__(self, d: dict = None):
        super().__init__(d)
        self.id: int
        self.version: int
        self.account: dict
        self.pair: str
        self.instant: bool
        self.status: dict
        self.leverage: dict
        self.position: dict
        self.take_profit: dict
        self.stop_loss: dict
        self.note: str
        self.skip_enter_step: bool
        self.data: dict
        self.profit: dict
        self.margin: dict
        self.is_position_not_filled: bool
    parsing_map = {
    }


class BotDealsStatsEntity(ThreeCommasModel):
    def __init__(self, d: dict = None):
        super().__init__(d)
        self.completed: int
        self.panic_sold: int
        self.active: int
        self.completed_deals_usd_profit: str
        self.from_currency_is_dollars: bool
        self.completed_deals_btc_profit: str
        self.funds_locked_in_active_deals: str
        self.btc_funds_locked_in_active_deals: str
        self.active_deals_usd_profit: str
        self.active_deals_btc_profit: str
    parsing_map = {
    }


class LooseAccountEntity(ThreeCommasModel):
    def __init__(self, d: dict = None):
        super().__init__(d)
        self.id: int
        self.name: str
        self.created_at: str
        self.updated_at: str
        self.type: str
        self.is_deleted: bool
        self.is_locked: bool
    parsing_map = {
    }

