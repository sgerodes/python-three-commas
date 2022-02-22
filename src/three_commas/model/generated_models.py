from __future__ import annotations
from .models import ThreeCommasModel, FloatParser, IntParser, DatetimeParser, ParsedProxy
import datetime
from typing import Union


class IndexEntity(ThreeCommasModel):
    bots: list
    total: int
    page: int

    _parse_map = {
    }
    _name_proxy = {
    }


class MarketplaceBotEntity(ThreeCommasModel):
    id: int
    type: str
    name: str
    strategy: str
    secret: str
    marketplace_item: None
    profit: None
    currencies: list
    copies: int
    is_favorite: bool

    _parse_map = {
    }
    _name_proxy = {
    }


class MarketplaceItem(ThreeCommasModel):
    id: int
    name: str
    icon_url: str

    _parse_map = {
    }
    _name_proxy = {
    }


class Profit(ThreeCommasModel):
    period: str
    amount: float
    chart_data: list

    _parse_map = {
    }
    _name_proxy = {
    }


class PongEntity(ThreeCommasModel):
    pong: str

    _parse_map = {
    }
    _name_proxy = {
    }


class TimeEntity(ThreeCommasModel):
    server_time: int

    _parse_map = {
    }
    _name_proxy = {
    }


class BotEntity(ThreeCommasModel):
    id: int
    account_id: int
    is_enabled: bool
    max_safety_orders: int
    active_safety_orders_count: int
    pairs: str
    strategy_list: str
    max_active_deals: int
    active_deals_count: int
    deletable: bool
    created_at: Union[str, datetime]
    updated_at: Union[str, datetime]
    trailing_enabled: bool
    tsl_enabled: bool
    deal_start_delay_seconds: int
    stop_loss_timeout_enabled: bool
    stop_loss_timeout_in_seconds: int
    disable_after_deals_count: int
    deals_counter: int
    allowed_deals_on_same_pair: int
    easy_form_supported: bool
    close_deals_timeout: int
    url_secret: str
    name: str
    take_profit: Union[str, float]
    base_order_volume: Union[str, float]
    safety_order_volume: Union[str, float]
    safety_order_step_percentage: Union[str, float]
    take_profit_type: str
    type: str
    martingale_volume_coefficient: Union[str, float]
    martingale_step_coefficient: Union[str, float]
    stop_loss_percentage: Union[str, float]
    cooldown: str
    btc_price_limit: Union[str, float]
    strategy: str
    min_volume_btc_24h: Union[str, float]
    profit_currency: str
    min_price: str
    max_price: str
    stop_loss_type: str
    safety_order_volume_type: str
    base_order_volume_type: str
    account_name: str
    trailing_deviation: Union[str, float]
    finished_deals_profit_usd: Union[str, float]
    finished_deals_count: Union[str, int]
    leverage_type: str
    leverage_custom_value: str
    start_order_type: str
    active_deals_usd_profit: Union[str, float]

    _parse_map = {
        'created_at': DatetimeParser,
        'updated_at': DatetimeParser,
        'take_profit': FloatParser,
        'base_order_volume': FloatParser,
        'safety_order_volume': FloatParser,
        'safety_order_step_percentage': FloatParser,
        'martingale_volume_coefficient': FloatParser,
        'martingale_step_coefficient': FloatParser,
        'stop_loss_percentage': FloatParser,
        'btc_price_limit': FloatParser,
        'min_volume_btc_24h': FloatParser,
        'trailing_deviation': FloatParser,
        'finished_deals_profit_usd': FloatParser,
        'finished_deals_count': IntParser,
        'active_deals_usd_profit': FloatParser,
    }
    _name_proxy = {
        'deletable': 'deletable?',
    }


class AccountEntity(ThreeCommasModel):
    id: int
    auto_balance_period: int
    auto_balance_portfolio_id: int
    auto_balance_currency_change_limit: int
    autobalance_enabled: bool
    hedge_mode_available: bool
    hedge_mode_enabled: bool
    is_locked: bool
    smart_trading_supported: bool
    smart_selling_supported: bool
    available_for_trading: bool
    stats_supported: bool
    trading_supported: bool
    market_buy_supported: bool
    market_sell_supported: bool
    conditional_buy_supported: bool
    bots_allowed: bool
    bots_ttp_allowed: bool
    bots_tsl_allowed: bool
    gordon_bots_available: bool
    multi_bots_allowed: bool
    created_at: Union[str, datetime]
    updated_at: Union[str, datetime]
    last_auto_balance: str
    fast_convert_available: bool
    grid_bots_allowed: bool
    api_key_invalid: bool
    deposit_enabled: bool
    supported_market_types: str
    api_key: str
    name: str
    auto_balance_method: int
    auto_balance_error: str
    customer_id: str
    subaccount_name: str
    lock_reason: str
    btc_amount: Union[str, float]
    usd_amount: Union[str, float]
    day_profit_btc: Union[str, float]
    day_profit_usd: Union[str, float]
    day_profit_btc_percentage: Union[str, float]
    day_profit_usd_percentage: Union[str, float]
    btc_profit: Union[str, float]
    usd_profit: Union[str, float]
    usd_profit_percentage: Union[str, float]
    btc_profit_percentage: Union[str, float]
    total_btc_profit: Union[str, float]
    total_usd_profit: Union[str, float]
    pretty_display_type: str
    exchange_name: str
    market_code: str
    address: str

    _parse_map = {
        'created_at': DatetimeParser,
        'updated_at': DatetimeParser,
        'btc_amount': FloatParser,
        'usd_amount': FloatParser,
        'day_profit_btc': FloatParser,
        'day_profit_usd': FloatParser,
        'day_profit_btc_percentage': FloatParser,
        'day_profit_usd_percentage': FloatParser,
        'btc_profit': FloatParser,
        'usd_profit': FloatParser,
        'usd_profit_percentage': FloatParser,
        'btc_profit_percentage': FloatParser,
        'total_btc_profit': FloatParser,
        'total_usd_profit': FloatParser,
    }
    _name_proxy = {
    }


class GridBotEntity(ThreeCommasModel):
    id: int
    account_id: int
    account_name: str
    is_enabled: bool
    grids_quantity: str
    created_at: str
    updated_at: str
    strategy_type: str
    lower_price: str
    upper_price: str
    quantity_per_grid: str
    leverage_type: str
    leverage_custom_value: str
    name: str
    pair: str
    start_price: str
    grid_price_step: str
    current_profit: str
    current_profit_usd: str
    total_profits_count: str
    bought_volume: str
    sold_volume: str
    profit_percentage: str
    current_price: str
    investment_base_currency: str
    investment_quote_currency: str
    grid_lines: None

    _parse_map = {
    }
    _name_proxy = {
    }


class GridLineEntity(ThreeCommasModel):
    price: str
    side: str
    order_placed: bool

    _parse_map = {
    }
    _name_proxy = {
    }


class GridBotProfitsEntity(ThreeCommasModel):
    grid_line_id: int
    profit: str
    usd_profit: str
    created_at: str

    _parse_map = {
    }
    _name_proxy = {
    }


class DealEntity(ThreeCommasModel):
    id: int
    type: str
    bot_id: int
    max_safety_orders: int
    deal_has_error: bool
    from_currency_id: int
    to_currency_id: int
    account_id: int
    active_safety_orders_count: int
    created_at: Union[str, datetime]
    updated_at: Union[str, datetime]
    closed_at: Union[str, datetime]
    finished: bool
    current_active_safety_orders_count: int
    current_active_safety_orders: int
    completed_safety_orders_count: int
    completed_manual_safety_orders_count: int
    cancellable: bool
    panic_sellable: bool
    trailing_enabled: bool
    tsl_enabled: bool
    stop_loss_timeout_enabled: bool
    stop_loss_timeout_in_seconds: int
    active_manual_safety_orders: int
    pair: str
    status: str
    localized_status: str
    take_profit: Union[str, float]
    base_order_volume: Union[str, float]
    safety_order_volume: Union[str, float]
    safety_order_step_percentage: Union[str, float]
    leverage_type: str
    leverage_custom_value: str
    bought_amount: Union[str, float]
    bought_volume: Union[str, float]
    bought_average_price: Union[str, float]
    base_order_average_price: Union[str, float]
    sold_amount: Union[str, float]
    sold_volume: Union[str, float]
    sold_average_price: Union[str, float]
    take_profit_type: str
    final_profit: Union[str, float]
    martingale_coefficient: Union[str, float]
    martingale_volume_coefficient: Union[str, float]
    martingale_step_coefficient: Union[str, float]
    stop_loss_percentage: Union[str, float]
    error_message: str
    profit_currency: str
    stop_loss_type: str
    safety_order_volume_type: str
    base_order_volume_type: str
    from_currency: str
    to_currency: str
    current_price: Union[str, float]
    take_profit_price: Union[str, float]
    stop_loss_price: str
    final_profit_percentage: Union[str, float]
    actual_profit_percentage: Union[str, float]
    bot_name: str
    account_name: str
    usd_final_profit: Union[str, float]
    actual_profit: Union[str, float]
    actual_usd_profit: Union[str, float]
    failed_message: str
    reserved_base_coin: Union[str, float]
    reserved_second_coin: Union[str, float]
    trailing_deviation: Union[str, float]
    trailing_max_price: Union[str, float]
    tsl_max_price: str
    strategy: str
    reserved_quote_funds: Union[float, float]
    reserved_base_funds: float

    _parse_map = {
        'created_at': DatetimeParser,
        'updated_at': DatetimeParser,
        'closed_at': DatetimeParser,
        'take_profit': FloatParser,
        'base_order_volume': FloatParser,
        'safety_order_volume': FloatParser,
        'safety_order_step_percentage': FloatParser,
        'bought_amount': FloatParser,
        'bought_volume': FloatParser,
        'bought_average_price': FloatParser,
        'base_order_average_price': FloatParser,
        'sold_amount': FloatParser,
        'sold_volume': FloatParser,
        'sold_average_price': FloatParser,
        'final_profit': FloatParser,
        'martingale_coefficient': FloatParser,
        'martingale_volume_coefficient': FloatParser,
        'martingale_step_coefficient': FloatParser,
        'stop_loss_percentage': FloatParser,
        'current_price': FloatParser,
        'take_profit_price': FloatParser,
        'final_profit_percentage': FloatParser,
        'actual_profit_percentage': FloatParser,
        'usd_final_profit': FloatParser,
        'actual_profit': FloatParser,
        'actual_usd_profit': FloatParser,
        'reserved_base_coin': FloatParser,
        'reserved_second_coin': FloatParser,
        'trailing_deviation': FloatParser,
        'trailing_max_price': FloatParser,
        'reserved_quote_funds': FloatParser,
    }
    _name_proxy = {
        'finished': 'finished?',
        'cancellable': 'cancellable?',
        'panic_sellable': 'panic_sellable?',
    }


class SmartTradeV2Entity(ThreeCommasModel):
    id: int
    version: int
    account: dict
    pair: str
    instant: bool
    status: dict
    leverage: dict
    position: dict
    take_profit: dict
    stop_loss: dict
    note: str
    skip_enter_step: bool
    data: dict
    profit: dict
    margin: dict
    is_position_not_filled: bool

    _parse_map = {
    }
    _name_proxy = {
    }


class TakeProfitStep(ThreeCommasModel):
    id: int
    version: int
    account: dict
    pair: str
    instant: bool
    status: dict
    leverage: dict
    position: dict
    take_profit: dict
    stop_loss: dict
    note: str
    skip_enter_step: bool
    data: dict
    profit: dict
    margin: dict
    is_position_not_filled: bool

    _parse_map = {
    }
    _name_proxy = {
    }


class BotDealsStatsEntity(ThreeCommasModel):
    completed: int
    panic_sold: int
    active: int
    completed_deals_usd_profit: str
    from_currency_is_dollars: bool
    completed_deals_btc_profit: str
    funds_locked_in_active_deals: str
    btc_funds_locked_in_active_deals: str
    active_deals_usd_profit: str
    active_deals_btc_profit: str

    _parse_map = {
    }
    _name_proxy = {
    }


class LooseAccountEntity(ThreeCommasModel):
    id: int
    name: str
    created_at: str
    updated_at: str
    type: str
    is_deleted: bool
    is_locked: bool

    _parse_map = {
    }
    _name_proxy = {
    }

