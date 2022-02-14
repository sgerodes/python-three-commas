# Title

This library provides tools that help develop code that access the 
[3commas api](https://github.com/3commas-io/3commas-official-api-docs) very fast and easy. 
The library is built on top of the py3cw library.
Main features are prebuilt functions for the api, models for easier access of the returned data, 
automatic attribute parsing of the returned data, built in error parsing. 

WIP: this library is still in construction. Some endpoints implementations are missing. Feel free to create a PR in github 
if you desire a particular endpoint implementation https://github.com/badass-blockchain/python-three-commas

## Installation

    pip install three-commas

## Usage

The package is built mirroring the names of the api paths. For example:

    from three_commas import api

    api.ver1.bots # bots endpoint
    api.ver1.accounts # account endpoint
    api.v2.smart_trades # v2 smart_trades endpoint

You can get all bots with: 

    bots_list = api_v1.bots.get_bots()

Or a single bot with:

    bot = api_v1.bots.get_show(bot_id=<your_bot_id>)

Or a smart trade

    smart_trade = api.v2.smart_trades.get_by_id(smart_trade_id=9993000)

The endpoints return a dict object with added functionality. You can use the object like a normal dictionary 
(exactly how you receive from py3cw), or use the added functions. 
For example if you want to get the bot max_active_deals you can do both:

    bot = api_v1.bots.get_show(bot_id=9999999)
    max_active_deals = bot['max_active_deals']
    max_active_deals = bot.get_max_active_deals()

### Parsing
One of the features of this library is the automatic parsing of the returned data. 
Some numeric data fetched from the api is returned as string. For example in the bot object:

    ...
    "base_order_volume": "0.003",
    "safety_order_volume": "0.003",
    "safety_order_step_percentage": "1.0",
    ...

Now you do not need to bother checking the type of the field and parsing it into the desired type.
This library auto parses these fields:

    bot = api_v1.bots.get_show(bot_id=9999999)
    # base_order_volume is a float
    base_order_volume = bot.get_base_order_volume() 

    
Parsing (except datetime fields) is done by default. 
If you do not want the field to be parsed, and you want the original string to be returned use parsed=False

    bot = api_v1.bots.get_show(bot_id=9999999)
    # base_order_volume is a str
    base_order_volume = bot.get_base_order_volume(parsed=False) 


Some fields like "created_at" are timestamps. You can parse these fields to a python datetime object. 
Timestamp fields are NOT parsed by default, only on demand:

    account = api_v1.accounts.get_account(account_id=8888888)

    # the original string returned by the api
    created_at_str = account.get_created_at() 

    # parsed into a datetime.datetime object
    created_at_datetime = account.get_created_at(parsed=True) 


### Api keys

In order to use the api you need to set the api key and secret. This could be done globally or per request.
To set it globally you need to set the environment variables THREE_COMMAS_API_KEY and THREE_COMMAS_API_SECRET.
To do it per request just pass them into the function:

    account = api_v1.accounts.get_account(account_id=8888888, api_key='my_key', api_secret='my_secret')

Request keys have priority. If both global and request keys are set, then the request keys will be used.

### Forced mode

You can set the forced mode globally or also per request.
To set it globally set the environment variable THREE_COMMAS_FORCED_MODE to either paper or real.
To use the forced mode per request pass it as an argument:

    paper_deals = api_v1.deals.get_deals(forced_mode='paper')
    real_deals = api_v1.deals.get_deals(forced_mode='real')


### Enums

Some enum fields have functionality. 

    accounts_list = api_v1.accounts.get_accounts()
    for account in accounts_list:
        if account.get_market_code().is_binance():
            # do stuff with the binance account.

You can check what enums are available in the three_commas.model.generated_enums package


