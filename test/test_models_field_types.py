from src.three_commas.model import DealMarketOrder
import json
import datetime


def test_deal_market_orders():
    with open('test/sample_data/deals/usdt/deals_market_orders_usdt.json', 'r') as f:
        j = json.loads(f.read())
        dmo_list = DealMarketOrder.of_list(j)
        dmo: DealMarketOrder = dmo_list[0]
        assert isinstance(dmo.get_order_id(), int)
        assert isinstance(dmo.get_created_at(parsed=True), datetime.datetime)
        assert isinstance(dmo.get_updated_at(parsed=True), datetime.datetime)
        assert isinstance(dmo.get_quantity(), float)
        assert isinstance(dmo.get_quantity_remaining(), float)
        assert isinstance(dmo.get_total(), float)
        assert isinstance(dmo.get_rate(), float)
        assert isinstance(dmo.get_average_price(), float)
