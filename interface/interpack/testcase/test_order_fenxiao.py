import time

import allure
import pytest

from interface.interpack.api.api_orderfenxiao import ApiOrderfx
from interface.interpack.until.until import Until


class TestOrderFenxiao:
    date=Until()
    # api=ApiOrderfx()

    def setup_class(self):
        self.api=ApiOrderfx()

    # def teardown(self):
    #     Until().delete_order()

    @allure.story("下游下单")
    @pytest.mark.parametrize("product",date.makedatatest("../data/trip-order/order_data.yaml","test_buy"))
    def test_buyprocedure_fx(self,product):
        sellerordersn=self.api.sellerordercreate()["sellerOrderSn"]
        print(sellerordersn)
        json=self.api.buyprocedure_fx(product,sellerordersn)
        assert json["msg"] == "success"

    @allure.story("下游下单支付")
    @pytest.mark.parametrize("product",date.makedatatest("../data/trip-order/order_data.yaml","test_buy"))
    def test_payprocedure_fx(self,product):
        sellerordersn=self.api.sellerordercreate()["sellerOrderSn"]
        ordersn=self.api.buyprocedure_fx(product,sellerordersn)
        json=self.api.payprocedure_fx(ordersn['data']['orderSn'])
        assert json["msg"] == "success"

    @allure.story("下游下单退款")
    @pytest.mark.parametrize("product",date.makedatatest("../data/trip-order/order_data.yaml","test_buy"))
    def test_refund_fx(self,product):
        sellerordersn=self.api.sellerordercreate()["sellerOrderSn"]
        ordersn=self.api.buyprocedure_fx(product,sellerordersn)
        self.api.payprocedure_fx(ordersn['data']['orderSn'])
        time.sleep(5)
        json=self.api.refund_fx(ordersn['data']['orderSn'])
        assert json["msg"] == "success"

    @allure.story("下游获取价格日历")
    @pytest.mark.parametrize("product",date.makedatatest("../data/trip-order/order_data.yaml","test_buy"))
    def test_getpricecalendar_fx(self,product):
        json=self.api.getpricecalendar_fx(product)
        assert json["msg"] == "success"

    @allure.story("下游分销商订单查询")
    @pytest.mark.parametrize("product",date.makedatatest("../data/trip-order/order_data.yaml","test_buy"))
    def test_selectorder_fx(self,product):
        sellerordersn = self.api.sellerordercreate()["sellerOrderSn"]
        ordersn = self.api.buyprocedure_fx(product, sellerordersn)
        json=self.api.selectorder_fx(ordersn['data']['orderSn'])
        assert json["msg"] == "success"


    @allure.story("下游查询门票信息")
    @pytest.mark.parametrize("product",date.makedatatest("../data/trip-order/order_data.yaml","test_buy"))
    def test_selectproduct_fx(self,product):
        json=self.api.selectproduct_fx(product)
        assert json["msg"] == "success"
