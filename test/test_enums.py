from src.three_commas.model.enums import *
from src.three_commas.model import Deal
import json


def test_enum_equality():
    assert BotScope.ENABLED == BotScope.ENABLED
    assert BotScope.ENABLED != BotScope.DISABLED

    assert BotScope.ENABLED == 'enabled'
    assert BotScope.ENABLED != 'disabled'

    assert BotScope.ENABLED == BotScope.ENABLED.value
    assert BotScope.ENABLED != BotScope.DISABLED.value

    assert BotScope.ENABLED != 'random_string'

    assert 'enabled' == BotScope.ENABLED
    assert 'disabled' != BotScope.ENABLED


def test_enum_parsing():
    filepath = 'test/sample_data/deals/usdt/deal_show_usdt.json'
    #filepath = './sample_data/deals/usdt/deal_show_usdt.json'
    with open(filepath, 'r+') as f:
        j: dict = json.loads(f.read())
        deal: Deal = Deal.of(j)
        status = deal.get_status()
        assert isinstance(status, DealStatus)
        assert isinstance(deal.get_status(parsed=False), str)
        assert not status.is_active()
        assert status.is_completed()
