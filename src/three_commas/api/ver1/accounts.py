from py3cw.request import Py3CW
from models import *


wrapper = Py3CW('', '')


def post_transfer():
    """
    /ver1/accounts/transfer
    Transfer coins between accounts (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    :param currency: REQUIRED, string, Currency code(example: USDT)
    :param amount: REQUIRED, number
    :param to_account_id: REQUIRED, integer, Recipient account ID (possible values in /transfer_data)
    :param from_account_id: REQUIRED, integer, Sender account ID (possible values in /transfer_data)
    """
    error, data = wrapper.request(
        entity='accounts',
        action='transfer',
    )
    return ThreeCommasError(error), data


def get_transfer_history():
    """
    /ver1/accounts/transfer_history
    Transfers history (Permission: ACCOUNTS_READ, Security: SIGNED)

    :param account_id: REQUIRED, integer, Sender or Recipient account ID (possible values in /transfer_data)
    :param currency: REQUIRED, string, Currency code(example: USDT)
    :param page: integer, Page number
    :param per_page: integer, Elements per page
    """
    error, data = wrapper.request(
        entity='accounts',
        action='transfer_history',
    )
    return ThreeCommasError(error), data


def get_transfer_data():
    """
    /ver1/accounts/transfer_data
    Data for transfer between accounts (Permission: ACCOUNTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='transfer_data',
    )
    return ThreeCommasError(error), data


def post_new():
    """
    /ver1/accounts/new
    Add exchange account  (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    :param type: REQUIRED, string, check market_code in market_list method
    :param name: REQUIRED, string, Account name (any string)
    :param api_key: string, Requires unless type = binance_dex
    :param secret: string, Requires unless type = binance_dex
    :param address: string, Requires if type = ethereumwallet
    :param customer_id: string, For Bitstamp
    :param passphrase: string, For Coinbase Pro (GDAX)
    :param how_connect: string, values: ['mnemonic_phrase', 'keystore']
    :param keystore: json, keystore file content. Requires if type = binance_dex and how_connect = keystore
    :param wallet_password: string, Requires if type = binance_dex and how_connect = keystore
    :param mnemonic_phrase: string, Requires if type = binance_dex and how_connect = mnemonic_phrase
    """
    error, data = wrapper.request(
        entity='accounts',
        action='new',
    )
    return ThreeCommasError(error), data


def post_update():
    """
    /ver1/accounts/update
    Edit exchange account

    :param account_id: REQUIRED, integer
    :param name: string, Account name (any string)
    :param api_key: string
    :param secret: string
    :param customer_id: string, For Bitstamp
    :param passphrase: string, For Coinbase Pro (GDAX)
    :param address: string, For accounts with type = ethereumwallet
    :param how_connect: string, values: ['mnemonic_phrase', 'keystore']
    :param keystore: json
    :param wallet_password: string
    :param mnemonic_phrase: string
    """
    error, data = wrapper.request(
        entity='accounts',
        action='update',
    )
    return ThreeCommasError(error), data


def get():
    """
    /ver1/accounts
    User connected exchanges(and EthereumWallet) list (Permission: ACCOUNTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='',
    )
    return ThreeCommasError(error), data


def get_market_list():
    """
    /ver1/accounts/market_list
    Supported markets list (Permission: NONE, Security: NONE)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='market_list',
    )
    return ThreeCommasError(error), data


def get_market_pairs():
    """
    /ver1/accounts/market_pairs
    All market pairs (Permission: NONE, Security: NONE)

    :param pretty_display_type: string, deprecated. mandatory use market_code instead
    :param market_code: string, market_code from account model
    """
    error, data = wrapper.request(
        entity='accounts',
        action='market_pairs',
    )
    return ThreeCommasError(error), data


''' This endpoint was not present in the py3cw module
def get_currency_rates_with_leverage_data():
    """
    /ver1/accounts/currency_rates_with_leverage_data
    Currency rates and limits with leverage data (Permission: NONE, Security: NONE)

    :param market_code: REQUIRED, string, market_code from account model
    :param pair: REQUIRED, string, Pair
    """
    error, data = wrapper.request(
        entity='accounts',
        action='<py3cw_action>',
    )
    return ThreeCommasError(error), data
'''


def get_currency_rates():
    """
    /ver1/accounts/currency_rates
    Currency rates and limits (Permission: NONE, Security: NONE)

    :param pair: REQUIRED, string, Pair
    :param pretty_display_type: string, deprecated. use market_code instead
    :param market_code: string, market_code from account model. If you are retrieving data for pairs, you must also include market_code
    """
    error, data = wrapper.request(
        entity='accounts',
        action='currency_rates',
    )
    return ThreeCommasError(error), data


''' This endpoint was not present in the py3cw module
def get_deposit_data_by_account_id(account_id):
    """
    /ver1/accounts/{account_id}/deposit_data
    User Deposit Data (Permission: ACCOUNTS_READ, Security: SIGNED)

    :param currency: REQUIRED, string
    :param network: REQUIRED, string
    :param account_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='accounts',
        action='<py3cw_action>',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def get_networks_info_by_account_id(account_id):
    """
    /ver1/accounts/{account_id}/networks_info
    Deposit/withdraw networks info (Permission: ACCOUNTS_READ, Security: SIGNED)

    :param account_id: REQUIRED, integer
    :param purpose: string, values: ['deposit', 'withdraw'], Filter currencies with deposit/withdraw enabled
    """
    error, data = wrapper.request(
        entity='accounts',
        action='<py3cw_action>',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_convert_dust_to_bnb_by_account_id(account_id):
    """
    /ver1/accounts/{account_id}/convert_dust_to_bnb
    Convert dust coins to BNB (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    :param account_id: REQUIRED, integer
    :param codes: array, Array of currency codes
    """
    error, data = wrapper.request(
        entity='accounts',
        action='<py3cw_action>',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def get_active_trading_entities_by_account_id(account_id):
    """
    /ver1/accounts/{account_id}/active_trading_entities
    Active trade entities (Permission: ACCOUNTS_READ, Security: SIGNED)

    :param account_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='accounts',
        action='<py3cw_action>',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_sell_all_to_usd_by_account_id(account_id):
    """
    /ver1/accounts/{account_id}/sell_all_to_usd
    Sell all to USD  (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    :param account_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='accounts',
        action='<py3cw_action>',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_sell_all_to_btc_by_account_id(account_id):
    """
    /ver1/accounts/{account_id}/sell_all_to_btc
    Sell all to BTC  (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    :param account_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='accounts',
        action='<py3cw_action>',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def get_balance_chart_data_by_account_id(account_id):
    """
    /ver1/accounts/{account_id}/balance_chart_data
    balance history data (Permission: ACCOUNTS_READ, Security: SIGNED)

    :param date_from: REQUIRED, string
    :param account_id: REQUIRED, integer
    :param date_to: string
    """
    error, data = wrapper.request(
        entity='accounts',
        action='<py3cw_action>',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_load_balances_by_account_id(account_id):
    """
    /ver1/accounts/{account_id}/load_balances
    Load balances for specified exchange  (Permission: ACCOUNTS_READ, Security: SIGNED)

    :param account_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='accounts',
        action='<py3cw_action>',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_rename_by_account_id(account_id):
    """
    /ver1/accounts/{account_id}/rename
    Rename exchange connection  (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    :param name: REQUIRED, string
    :param account_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='accounts',
        action='<py3cw_action>',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_pie_chart_data_by_account_id(account_id):
    """
    /ver1/accounts/{account_id}/pie_chart_data
    Information about all user balances on specified exchange in pretty for pie chart format (Permission: ACCOUNTS_READ, Security: SIGNED)

    :param account_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='accounts',
        action='<py3cw_action>',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_account_table_data_by_account_id(account_id):
    """
    /ver1/accounts/{account_id}/account_table_data
    Information about all user balances on specified exchange  (Permission: ACCOUNTS_READ, Security: SIGNED)

    :param account_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='accounts',
        action='<py3cw_action>',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def post_remove_by_account_id(account_id):
    """
    /ver1/accounts/{account_id}/remove
    Remove exchange connection  (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    :param account_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='accounts',
        action='<py3cw_action>',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def get_leverage_data_by_account_id(account_id):
    """
    /ver1/accounts/{account_id}/leverage_data
    Information about account leverage (Permission: ACCOUNTS_READ, Security: SIGNED)

    :param pair: REQUIRED, string
    :param account_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='accounts',
        action='<py3cw_action>',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data
'''


''' This endpoint was not present in the py3cw module
def get_by_account_id(account_id):
    """
    /ver1/accounts/{account_id}
    Single Account Info (Permission: ACCOUNTS_READ, Security: SIGNED)
You can send 'summary' instead of {account_id} to get summary account info

    :param account_id: REQUIRED, integer
    """
    error, data = wrapper.request(
        entity='accounts',
        action='<py3cw_action>',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data
'''


