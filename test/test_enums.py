from src.three_commas.model.enums import *


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
