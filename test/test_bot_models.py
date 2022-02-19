from src.three_commas.model.generated_models import DealEntity, BotEntity
import json


def test_bot_events_are_parsed():
    filepath = 'test/sample_data/bots/btc/bot_show_with_events_btc.json'
    #filepath = './sample_data/bots/btc/bot_show_with_events_btc.json'
    with open(filepath, 'r+') as f:
        bot_show: BotEntity = BotEntity(json.loads(f.read()))
        # TODO
        # assert isinstance(bot_show.get_bot_events()[0], BotEvent)
        # assert isinstance(bot_show.get_active_deals()[0], Deal)
