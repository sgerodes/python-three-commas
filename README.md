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
    api.ver1.deals # deals endpoint
    api.ver1.users # users endpoint
    api.v2.smart_trades # v2 smart_trades endpoint

The endpoints are mirrored from the paths too.
    
    # GET /ver1/bots/pairs_black_list
    black_list_pairs = api.ver1.bots.get_pairs_black_list()

    # GET /v2/smart_trades/{id}
    smart_trades_list = api.v2.smart_trades.get_by_id(id=<your_smart_trade_id>)


You can get all bots with: 

    bots_list = api.ver1.bots.get()

Or a single bot with:

    bot = api.ver1.bots.get_show_by_id(bot_id=<your_bot_id>)

Or a smart trade

    smart_trade = api.v2.smart_trades.get_by_id(id=9993000)

The endpoints return a dict object with added functionality. You can use the object like a normal dictionary 
(exactly how you receive from py3cw), or use the added functions. 
For example if you want to get the bot max_active_deals you can do both:

    bot = api.ver1.bots.get_show_by_id(bot_id=9999999)
    max_active_deals = bot['max_active_deals']
    max_active_deals = bot.max_active_deals

### Websocket Streams

You can easily connect to the websockets 
You can use annotations.

    import three_commas
    from three_commas.model import DealEntity, SmartTradeV2Entity

    @three_commas.streams.smart_trades
    def handle_smart_trades(smart_trade: SmartTradeV2Entity):
        # Do here something with the smart trade
        # Every new smart trade is passed to this function
        print(smart_trade)

    @three_commas.streams.deals
    def handle_deals(deal: DealEntity):
        # do your awesome stuff with the deal
        print(deal)  #  {'id': 1311811868, 'type': 'Deal', 'bot_id': 6313165, 'max_safety_orders': 6, 'deal_has_error': False ....
        print(deal.account_id)  #  99648312
        print(deal.created_at)  #  string object '2022-02-18T05:26:06.803Z'
        print(deal.parsed(True).created_at)  #  datetime.datetime object 


In order to use the websocket streams you need to set the api key and secret in your environment.
[Later in the document you can find how to set up the environment variables](#Set the api key and secret)

Or you can pass the keys to the decorator:

    @three_commas.streams.deals(api_key='<your_api_key>', secret='<your_secret>')
    def handle_deals(deal):
        ...


For debugging you can turn on debug level

    import logging

    logging.getLogger('three_commas.streams').setLevel(level=logging.DEBUG)

You will see a lot of websocket messages including pings:

    > DEBUG:three_commas.streams.streams: {"type": "welcome"}
    > DEBUG:three_commas.streams.streams: {"type": "ping", "message": 1645286932}
    > DEBUG:three_commas.streams.streams: {"type": "ping", "message": 1645286935}
    > DEBUG:three_commas.streams.streams: {"type": "ping", "message": 1645286938}

You can also set up the level to info for less verbose loging
    logging.getLogger('three_commas.streams').setLevel(level=logging.INFO)


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

    bot = api.ver1.bots.get_show(9999999)
    # base_order_volume is a float
    base_order_volume = bot.get_base_order_volume() 

    
Parsing (except datetime fields) is done by default. 
If you do not want the field to be parsed, and you want the original string to be returned use parsed=False

    bot = api.ver1.bots.get_show(9999999)
    # base_order_volume is a str
    base_order_volume = bot.parsed(False).base_order_volume 


Some fields like "created_at" are timestamps. You can parse these fields to a python datetime object. 
Timestamp fields are NOT parsed by default, only on demand:

    account = api.ver1.accounts.get_by_id(8888888)

    # the original string returned by the api
    created_at_str = account.created_at

    # parsed into a datetime.datetime object
    created_at_datetime = account.parsed(True).created_at


### Api keys

In order to use the api you need to set the api key and secret. This could be done globally or per request.
To set it globally you need to set the environment variables THREE_COMMAS_API_KEY and THREE_COMMAS_API_SECRET.
To do it per request just pass them into the function:

    account = api.ver1.accounts.get_by_id(8888888, api_key='my_key', api_secret='my_secret')

Request keys have priority. If both global and request keys are set, then the request keys will be used.

### Forced mode

You can set the forced mode globally or also per request.
To set it globally set the environment variable THREE_COMMAS_FORCED_MODE to either paper or real.
To use the forced mode per request pass it as an argument:

    paper_deals = api.ver1.deals.get(forced_mode='paper')
    real_deals = api.ver1.deals.get(forced_mode='real')


### Enums

Some enum fields have functionality. 

    accounts_list = api_v1.accounts.get_accounts()
    for account in accounts_list:
        if account.get_market_code().is_binance():
            # do stuff with the binance account.

You can check what enums are available in the three_commas.model.generated_enums package

### Set the api key and secret

You can set key and secret as an environment variables. The preferred way is to use a .env file:

create a file called .env with the following content:

    THREE_COMMAS_API_KEY=<your_api_key>
    THREE_COMMAS_API_SECRET=<your_api_secret>

Use a .env loader as python-dotenv. Install it on your machine with pip: "pip install python-dotenv".
If your project is a git project make sure you gitignore the .env file.
Then in your code

    from dotenv import load_dotenv
    load_dotenv()

Now your variables are loaded. Enjoy using the library.


You can also set the api key and secret directly in the code. This method is less secure and not recommended.
    
    import os

    os.environ["THREE_COMMAS_API_KEY"] = <your_api_key>
    os.environ["THREE_COMMAS_API_SECRET"] = <your_api_secret>



### Examples
#### Posting a new smart trade
    smart_trade = {
        'account_id': 99999999,
        'pair': 'USDT_FUN',
        'position': {
            'type': 'buy',
            'order_type': 'market',
            'units': {
                'value': "30526.0",
            },
            "total": {
                "value": "600.61907506"
            }
        },
        'take_profit': {
            'enabled': False,
        },
        'stop_loss': {
            'enabled': False,
        }

    }

    error, smart_trade_response = api.v2.smart_trades.post(smart_trade)
#### Retrieving a smart trade

    error, smart_trade = api.v2.smart_trades.get_by_id(13819196)
    if not error:
        # Do your awesome stuff with the smart trade
        print(smart_trade.profit)
