import asyncio
import websockets
import json
from .sys_utils import create_signature
import logging
from enum import Enum
import functools
import threading
from .model import Deal, SmartTradeV2

logger = logging.getLogger(__name__)


BASE_URL = 'wss://ws.3commas.io/websocket'


class StreamType(Enum):
    class StreamTypeConfig:
        def __init__(self, endpoint: str, channel: str, parse_type: type = None):
            self.endpoint = endpoint
            self.channel = channel
            self.parse_type = parse_type


    SMART_TRADES = StreamTypeConfig(endpoint='/smart_trades', channel='SmartTradesChannel', parse_type=SmartTradeV2)
    DEALS = StreamTypeConfig(endpoint='/deals', channel='DealsChannel', parse_type=Deal)

    def get_endpoint(self):
        return self.value.endpoint

    def get_channel(self):
        return self.value.channel

    def get_parse_type(self):
        return self.value.parse_type

    def has_parse_type(self):
        return self.value.parse_type is not None


class WebSocketMessageType(str, Enum):
    WELCOME = 'welcome'
    PING = 'ping'
    CONFIRM_SUBSCRIPTION = 'confirm_subscription'


class WebSocketMessage(dict):

    def _has_type(self) -> bool:
        return 'type' in self

    def _has_identifier(self) -> bool:
        return 'identifier' in self

    def _is_type(self, t) -> bool:
        return self._has_type() and self.get_type() == t

    def get_type(self) -> str:
        return self.get('type')

    def get_identifier(self) -> str:
        return self.get('identifier')

    def get_message(self) -> dict:
        return self.get('message')

    def is_welcome(self) -> bool:
        return self._is_type(WebSocketMessageType.WELCOME)

    def is_ping(self) -> bool:
        return self._is_type(WebSocketMessageType.PING)

    def is_confirm_subscription(self) -> bool:
        return self._is_type(WebSocketMessageType.CONFIRM_SUBSCRIPTION)

    def is_stream_type(self, stream_type: StreamType):
        if not self._has_identifier():
            return False
        identifier_dict = json.loads(self.get_identifier())
        channel = identifier_dict.get('channel')
        return channel and channel == stream_type.get_channel()


def smart_trades_stream_decorator(api_key, api_secret):
    return create_runner_for_stream_type(StreamType.SMART_TRADES, api_key, api_secret)


def deals_stream_decorator(api_key, api_secret):
    return create_runner_for_stream_type(StreamType.DEALS, api_key, api_secret)


def create_runner_for_stream_type(stream_type: StreamType, api_key, api_secret):
    initial_message = get_message_for(stream_type, api_key, api_secret)

    def inner(function_to_wrap):
        logger.debug(f'Initializing a {stream_type.get_channel()} for function {function_to_wrap.__name__}')

        @functools.wraps(function_to_wrap)
        async def stream_decorator():
            full_url = f'{BASE_URL}{stream_type.get_endpoint()}'
            async with websockets.connect(full_url) as ws:
                msg = await ws.send(json.dumps(initial_message))
                async for ws_message in ws:
                    ws_dict_message = WebSocketMessage(json.loads(ws_message))
                    logger.debug(f'Received message {json.dumps(ws_dict_message)}')
                    if ws_dict_message.is_stream_type(stream_type) and ws_dict_message.is_confirm_subscription():
                        logger.debug(f'Confirmed subscription to {stream_type.get_channel()}')
                        break

                async for ws_message in ws:
                    ws_dict_message = WebSocketMessage(json.loads(ws_message))
                    logger.debug(f'Received message {json.dumps(ws_dict_message)}')
                    if ws_dict_message.is_stream_type(stream_type):
                        tc_message = ws_dict_message.get_message()
                        if stream_type.has_parse_type():
                            tc_message = stream_type.get_parse_type()(tc_message)
                        function_to_wrap(tc_message)

        # loop = asyncio.get_event_loop()
        # asyncio.set_event_loop(loop)
        # t = threading.Thread(target=loop.run_until_complete, args=(stream_decorator,))
        # t.start()
        # asyncio.create_task(stream_decorator())
        loop = asyncio.get_event_loop()
        task = loop.create_task(stream_decorator())
        if not loop.is_running():
            t = threading.Thread(target=loop.run_forever)
            t.start()
        return stream_decorator

    return inner


def get_message_for(stream_type: StreamType, api_key, api_secret):
    signature = create_signature(stream_type.get_endpoint(), api_secret)
    identifier = {
        'channel': stream_type.get_channel(),
        'users': [
            {
                'api_key': api_key,
                'signature': signature
            }
        ],
    }
    message = {
        'identifier': json.dumps(identifier),
        "command": "subscribe"
    }
    return message



