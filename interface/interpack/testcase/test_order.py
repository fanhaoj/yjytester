import logging
import time

import allure
import pytest
import yaml
import pytest_assume

from interface.interpack.api.api_order import ApiOrder
from interface.interpack.until.until import Until


class TestOrder:

    def setup(self):
        self.api=ApiOrder()

    def teardown(self):
        pass


    @allure.story("下单")
    @pytest.mark.parametrize("productid", [Until().makedatatest("../data/trip-order/order_data.yaml","proqmp","productid")])
    def test_buyandpay(self, productid):
        print(productid)
        with allure.step("下单"):
            orderid = self.api.buyprocedure(productid)['data']['id']
            json = self.api.payprocedure(orderid)
            assert json["msg"] == "success"

    @allure.story("下单支付")
    @pytest.mark.parametrize("productid", [Until().makedatatest("../data/trip-order/order_data.yaml","proyjy","productid")])
    def test_buyandpay(self, productid):
        with allure.step("下单"):
            orderid = self.api.buyprocedure(productid)['data']['id']
            json = self.api.payprocedure(orderid)
            assert json["msg"] == "success"

    @allure.link("http://www.baidu.com", name="小百")
    @allure.story("支付退款")
    @pytest.mark.parametrize("productid", [Until().makedatatest("../data/trip-order/order_data.yaml","proyjy","productid")])
    def test_refund(self, productid):
        orderid = self.api.buyprocedure(productid)['data']['id']
        self.api.payprocedure(orderid)
        json = self.api.refund(orderid)
        assert json["msg"] == "success"

    @allure.story("取消订单")
    @pytest.mark.parametrize("productid", [Until().makedatatest("../data/trip-order/order_data.yaml","proyjy","productid")])
    def test_cancel(self, productid):
        orderid = self.api.buyprocedure(productid)['data']['id']
        logging.info("下单生成订单id：" + str(orderid))
        print(orderid)
        ordersn = self.api.ticketdetail(orderid)['data']['orderSn']
        print(ordersn)
        json = self.api.cancel(ordersn)
        assert json["msg"] == "success"

    @allure.story("核销订单")
    @pytest.mark.parametrize("productid", [Until().makedatatest("../data/trip-order/order_data.yaml","proyjy","productid")])
    def test_verify(self, productid):
        orderid = self.api.buyprocedure(productid)['data']['id']
        print(orderid)
        self.api.payprocedure(orderid)
        try:
            orderstatus = self.api.ticketdetail(orderid)["data"]["orderStatus"]
            assert orderstatus == 3
        except:
            bool = True
            while (bool):
                orderstatus = self.api.ticketdetail(orderid)["data"]["orderStatus"]
                if orderstatus == 3:
                    bool = False
        json = self.api.verify(orderid)
        assert json["msg"] == "success"

    @allure.story("小程序核销")
    @pytest.mark.parametrize("productid,scenicSpotId", [(Until().makedatatest("../data/trip-order/order_data.yaml","proyjy","productid"),"1")])
    def test_miniverify(self, productid, scenicSpotId):
        orderid = self.api.buyprocedure(productid)['data']['id']
        self.api.payprocedure(orderid)
        try:
            orderstatus=self.api.ticketdetail(orderid)["data"]["orderStatus"]
            assert orderstatus == 3
        except:
            bool=True
            while(bool):
                orderstatus = self.api.ticketdetail(orderid)["data"]["orderStatus"]
                if orderstatus == 3:
                    bool=False
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

