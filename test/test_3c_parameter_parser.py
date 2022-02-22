from src.three_commas.model import BotEntity
import json
import datetime


def test_attribute_with_question_mark():
    bot = BotEntity({
        'deletable?': False
    })

    assert bot.deletable is False

    bot.deletable = True

    assert bot.deletable is True
    assert bot.get('deletable?') is True


def test_parsed_is_accepting_all_values():
    bot = BotEntity({
        'base_order_volume': '1.1'
    })

    assert bot.base_order_volume == 1.1
    assert bot.parsed(None).base_order_volume == 1.1
    assert bot.parsed(True).base_order_volume == 1.1
    assert bot.parsed(False).base_order_volume == "1.1"


def test_missing_attributes():
    bot = BotEntity()

    assert bot.take_profit is None
    assert bot.parsed(True).take_profit is None
    assert bot.parsed(False).take_profit is None
    assert bot.parsed(None).take_profit is None


def test_parsing():
    bot = BotEntity({
        'finished_deals_count': '123',
        'base_order_volume': '1.0',
        'created_at': '2019-01-01T00:00:00.000Z',
    })

    # Int parsing. By default is parsed
    assert bot.finished_deals_count == 123
    assert bot.parsed(True).finished_deals_count == 123
    assert bot.parsed(False).finished_deals_count == '123'

    # Float parsing. By default is parsed
    assert bot.parsed(True).base_order_volume == 1.0
    assert bot.base_order_volume == 1.0
    assert bot.parsed(False).base_order_volume == '1.0'

    # Date parsing. By default is not parsed
    assert bot.created_at == '2019-01-01T00:00:00.000Z'
    assert bot.parsed(True).created_at == datetime.datetime(2019, 1, 1, 0, 0, 0, 0)
    assert bot.parsed(False).created_at == '2019-01-01T00:00:00.000Z'


def test_set_attributes():
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

    bot.finished_deals_count = '456'
    assert bot.finished_deals_count == 456

    bot.base_order_volume = '3.2'
    assert bot.base_order_volume == 3.2

    bot.created_at = '2022-01-01T00:00:00.000Z'
    assert bot.created_at == '2022-01-01T00:00:00.000Z'
    assert bot.parsed(True).created_at == datetime.datetime(2022, 1, 1, 0, 0, 0, 0)

    bot.pairs = ['BTC_ETH']
    assert bot.pairs == ['BTC_ETH']

    bot.deletable = True
    assert bot.deletable is True


def model_equals_dict():
    d = {'finished_deals_count': '123'}
    bot = BotEntity({'finished_deals_count': '123'})

    assert bot == d
    assert bot != {'finished_deals_count': '456'}


def test_json_equality_after_parsing():
    bot = BotEntity({
        'finished_deals_count': '123',
        'base_order_volume': '1.0',
        'deletable?': False
    })

    str_bot = json.dumps(bot)
    recreated_bot = BotEntity(json.loads(str_bot))

    assert recreated_bot == bot

