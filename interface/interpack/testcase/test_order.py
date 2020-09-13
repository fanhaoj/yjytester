import logging
import time

import allure
import pytest
import yaml
import pytest_assume

from interface.interpack.api.api_order import ApiOrder
from interface.interpack.until.until import Until

# pytest  -v test_order.py --allure-stories "核销订单"
class TestOrder:
    date = Until()

    def setup(self):
        self.api=ApiOrder()


    # def teardown(self):
    #     Until().delete_order()


    @allure.story("下单")
    @pytest.mark.parametrize("productid", date.makedatatest("../data/trip-order/order_data.yaml","test_buy"))
    def test_buy(self, productid):
        with allure.step("下单"):
            json = self.api.buyprocedure(productid)
            assert json["msg"] == "success"

    @allure.story("下单支付")
    @pytest.mark.parametrize("productid", date.makedatatest("../data/trip-order/order_data.yaml","test_buy"))
    def test_buyandpay(self, productid):
        with allure.step("下单"):
            orderid = self.api.buyprocedure(productid)['data']['id']
            json = self.api.payprocedure(orderid)
            assert json["msg"] == "success"

    @allure.link("http://www.baidu.com", name="小百")
    @allure.story("支付退款")
    @pytest.mark.parametrize("productid", date.makedatatest("../data/trip-order/order_data.yaml","test_buy"))
    def test_refund(self, productid):
        orderid = self.api.buyprocedure(productid)['data']['id']
        print(orderid)
        self.api.payprocedure(orderid)
        self.api.waitorderstatus(orderid,3)
        json = self.api.refund(orderid)
        assert json["msg"] == "success"

    @allure.story("取消订单")
    @pytest.mark.parametrize("productid", date.makedatatest("../data/trip-order/order_data.yaml","test_buy"))
    def test_cancel(self, productid):
        orderid = self.api.buyprocedure(productid)['data']['id']
        logging.info("下单生成订单id：" + str(orderid))
        print(orderid)
        ordersn = self.api.ticketdetail(orderid)['data']['orderSn']
        print(ordersn)
        json = self.api.cancel(ordersn)
        assert json["msg"] == "success"

    @allure.story("核销订单")
    @pytest.mark.parametrize("productid", date.makedatatest("../data/trip-order/order_data.yaml","test_buy"))
    def test_verify(self, productid):
        orderid = self.api.buyprocedure(productid)['data']['id']
        self.api.payprocedure(orderid)
        self.api.waitorderstatus(orderid,3)
        json = self.api.verify(orderid)
        assert json["msg"] == "success"

    @allure.story("小程序核销")
    @pytest.mark.parametrize("productid,scenicSpotId", date.makedatatest("../data/trip-order/order_data.yaml","test_miniverify"))
    def test_miniverify(self, productid, scenicSpotId):
        print(productid,scenicSpotId)
        orderid = self.api.buyprocedure(productid)['data']['id']
        self.api.payprocedure(orderid)
        self.api.waitorderstatus(orderid, 3)
        verifycode = self.api.ticketdetail(orderid)["data"]["ticketInfo"][0]['verifyCode']
        json = self.api.miniverify(scenicSpotId, verifycode)
        assert json["msg"] == "success"

    @allure.story("分销用户常用旅客")
    def test_TopContactsList(self):
        json=self.api.TopContactsList()
        assert json["msg"] == "success"

    @allure.story("消息队列测试接口")
    def test_mqTest(self):
        json=self.api.mqTest()
        assert json["msg"] == "success"

    @allure.story("手动处理出票中订单到出票失败")
    def test_ManualProcessing(self):
        json=self.api.ManualProcessing()
        assert json["msg"] == "success"

    @allure.story("手动处理退款中订单")
    @pytest.mark.parametrize("buyorderid", [])
    def test_manuallyProcessRefundOrders(self,buyorderid):
        orderid = self.api.buyprocedure()
        json=self.api.manuallyProcessRefundOrders(buyorderid)
        assert json["msg"] == "success"

