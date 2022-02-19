from src.three_commas.model import BotEntity, StrIntProxy, StrFloatProxy, StrDatetimeProxy
import json
import datetime


def test_fields_are_parsed():
    with open('test/sample_data/bots/usdt/bot_show_with_events_usdt.json') as f:
        bot_show: BotEntity = BotEntity(json.loads(f.read()))
        assert bot_show.base_order_volume == 10.0
        assert bot_show.base_order_volume.parsed(parsed=False) == "10.0"

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
        assert isinstance(bot_show.created_at, StrDatetimeProxy)
        assert isinstance(bot_show.created_at.parsed(parsed=True), datetime.datetime)


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
    assert isinstance(bot.finished_deals_count, StrIntProxy)
    assert bot.finished_deals_count == 123
    assert isinstance(bot.finished_deals_count.parsed(True), int)
    assert bot.finished_deals_count.parsed(False) == '123'
    assert bot.finished_deals_count.parsed(True) == 123
    bot.finished_deals_count = '456'
    assert bot.finished_deals_count == 456
    assert isinstance(bot.finished_deals_count, StrIntProxy)
    assert bot.finished_deals_count.parsed(False) == '456'
    bot.finished_deals_count = "dsadas"
    assert bot.finished_deals_count == "dsadas"

    assert bot.take_profit is None

    assert isinstance(bot.base_order_volume, float)
    assert isinstance(bot.base_order_volume, StrFloatProxy)
    assert bot.base_order_volume == 1.0
    assert isinstance(bot.base_order_volume.parsed(True), float)
    assert bot.base_order_volume.parsed(False) == '1.0'
    assert bot.base_order_volume.parsed(True) == 1.0

    assert isinstance(bot.created_at, str)
    assert isinstance(bot.created_at, StrDatetimeProxy)
    assert bot.created_at == '2019-01-01T00:00:00.000Z'
    assert isinstance(bot.created_at.parsed(True), datetime.datetime)
    assert bot.created_at.parsed(False) == '2019-01-01T00:00:00.000Z'
    assert bot.created_at.parsed(True) == datetime.datetime(2019, 1, 1, 0, 0, 0, 0)


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
