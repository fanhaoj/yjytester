import pytest

from interface.interpack.api.api_orderfenxiao import ApiOrderfx
from interface.interpack.until.until import Until


class TestOrderFenxiao:
    date=Until()
    api=ApiOrderfx()

    # def setup(self):
    #     self.api=ApiOrder()

    def teardown(self):
        Until().delete_order()

    @pytest.mark.parametrize("product",date.makedatatest("../data/trip-order/order_data.yaml","test_buy"))
    def test_buyprocedure_fx(self,product):
        sellerordersn=self.api.sellerordercreate()["sellerOrderSn"]
        json=self.api.buyprocedure_fx(product,sellerordersn)
        assert json["msg"] == "success"
