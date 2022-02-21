from src.three_commas.model import *
import json
import datetime


def test_fields_are_parsed():
    with open('test/sample_data/bots/usdt/bot_show_with_events_usdt.json') as f:
        bot_show: BotEntity = BotEntity(json.loads(f.read()))
        assert bot_show.base_order_volume == 10.0
        assert bot_show.parsed(parsed=False).base_order_volume == "10.0"

        bot_show.base_order_volume = None
        assert bot_show.base_order_volume is None
        # assert bot_show.base_order_volume.parsed(parsed=False) is None

        del bot_show['base_order_volume']
        assert bot_show.base_order_volume is None
        # assert bot_show.base_order_volume.parsed(parsed=False) is None


def test_ts_are_parsed():
    with open('test/sample_data/bots/usdt/bot_show_with_events_usdt.json') as f:
        bot_show: BotEntity = BotEntity(json.loads(f.read()))
        assert isinstance(bot_show.created_at, str)
        assert isinstance(bot_show.parsed(True).created_at, datetime.datetime)


def test_attributes_v3():
    bot = BotEntity({
        'finished_deals_count': '123',
        'base_order_volume': '1.0',
        'created_at': '2019-01-01T00:00:00.000Z',
        "pairs": [
            "BTC_1INCH",
            "BTC_AAVE"
        ],
        'deletable?': False
    })

    assert isinstance(bot.pairs, list)

    assert isinstance(bot.finished_deals_count, int)
    assert bot.finished_deals_count == 123
    assert isinstance(bot.parsed(True).finished_deals_count, int)
    assert bot.parsed(False).finished_deals_count == '123'
    assert bot.parsed(True).finished_deals_count == 123
    bot.finished_deals_count = '456'
    assert bot.finished_deals_count == 456
    assert bot.parsed(False).finished_deals_count == '456'
    bot.finished_deals_count = "dsadas"
    assert bot.finished_deals_count == "dsadas"

    assert bot.take_profit is None

    assert isinstance(bot.base_order_volume, float)
    assert bot.base_order_volume == 1.0
    assert isinstance(bot.parsed(True).base_order_volume, float)
    assert bot.parsed(False).base_order_volume == '1.0'
    assert bot.parsed(True).base_order_volume == 1.0

    assert isinstance(bot.created_at, str)
    assert bot.created_at == '2019-01-01T00:00:00.000Z'
    assert isinstance(bot.parsed(True).created_at, datetime.datetime)
    assert bot.parsed(False).created_at == '2019-01-01T00:00:00.000Z'
    assert bot.parsed(True).created_at == datetime.datetime(2019, 1, 1, 0, 0, 0, 0)


def test_json_parse_models_v3():
    bot = BotEntity({
        'finished_deals_count': '123',
        'base_order_volume': '1.0',
        'created_at': '2019-01-01T00:00:00.000Z',
        "pairs": [
            "BTC_1INCH",
            "BTC_AAVE"
        ],
        'deletable?': False
    })

    str_bot = json.dumps(bot)
    recreated_bot = BotEntity(json.loads(str_bot))

    assert recreated_bot == bot


def test_models_v4():
    d = DealEntity({
        'id': 123,
        'type': 'long',
        'deal_has_error': False,
        'created_at': '2022-02-01T10:11:12.987Z',  # %Y-%m-%dT%H:%M:%S.%fZ
        'take_profit': '2.5',
        'reserved_base_funds': 1.132,
        'finished?': False
    })

    assert d.id == 123
    assert d.type == 'long'
    assert d.deal_has_error is False
    assert d.created_at == '2022-02-01T10:11:12.987Z'
    assert d.take_profit == 2.5
    assert d.reserved_base_funds == 1.132

    assert d.parsed(False).take_profit == '2.5'
    assert isinstance(d.parsed(False).take_profit, str)
    assert d.parsed(True).take_profit == 2.5
    assert isinstance(d.parsed(True).take_profit, float)
    assert d.sold_amount is None
    assert d.parsed(True).sold_amount is None
    assert d.parsed(False).sold_amount is None
    assert d.parsed(None).sold_amount is None

    assert isinstance(d.created_at, str)
    assert d.created_at == '2022-02-01T10:11:12.987Z'
    assert isinstance(d.parsed(False).created_at, str)
    assert isinstance(d.parsed(True).created_at, datetime.datetime)
    assert d.parsed(False).created_at == '2022-02-01T10:11:12.987Z'
    assert d.parsed(True).created_at == datetime.datetime(2022, 2, 1, 10, 11, 12, 987000)

    assert d.finished is not None
    assert d.finished is False

    d.finished = True
    d.take_profit = '4.52'

    assert d.finished is True
    assert d.take_profit == 4.52
    assert d.parsed(False).take_profit == '4.52'
    assert d.parsed(True).take_profit == 4.52
