import logging
import time

import allure
import pytest
import yaml

from interface.interpack.api.api_order import ApiOrder
date = time.strftime("%Y-%m-%d", time.localtime())
dataparm=yaml.safe_load(open("../data/buyproduce.yaml"))

class TestOrder:

    def setup(self):
        self.api=ApiOrder()

    @allure.story("下单")
    @pytest.mark.parametrize("date,productid", [date, dataparm["productid"]])
    def test_buyandpay(self, date, productid):
        with allure.step("下单"):
            orderid = self.api.buyprocedure(date, productid)['data']['id']
            json = self.api.payprocedure(orderid)
            assert json["msg"] == "success"

    @allure.story("下单支付")
    @pytest.mark.parametrize("date,productid", [(date, dataparm["productid"])])
    def test_buyandpay(self, date, productid):
        with allure.step("下单"):
            orderid = self.api.buyprocedure(date, productid)['data']['id']
            json = self.api.payprocedure(orderid)
            assert json["msg"] == "success"

    @allure.link("http://www.baidu.com", name="小百")
    @allure.story("支付退款")
    @pytest.mark.parametrize("date,productid", [(date, dataparm["productid"])])
    def test_refund(self, date, productid):
        orderid = self.api.buyprocedure(date, productid)['data']['id']
        self.api.payprocedure(orderid)
        json = self.api.refund(orderid)
        assert json["msg"] == "success"

    @allure.story("取消订单")
    @pytest.mark.parametrize("date,productid", [(date, dataparm["productid"])])
    def test_cancel(self, date, productid):
        orderid = self.api.buyprocedure(date, productid)['data']['id']
        logging.info("下单生成订单id：" + str(orderid))
        print(orderid)
        ordersn = self.api.ticketdetail(orderid)['data']['orderSn']
        print(ordersn)
        json = self.api.cancel(ordersn)
        assert json["msg"] == "success"

    @allure.story("核销订单")
    @pytest.mark.parametrize("date,productid", [(date, dataparm["productid"])])
    def test_verify(self, date, productid):
        orderid = self.api.buyprocedure(date, productid)['data']['id']
        print(orderid)
        self.api.payprocedure(orderid)
        json = self.api.verify(orderid)
        assert json["msg"] == "success"

    @allure.story("小程序核销")
    @pytest.mark.parametrize("date,productid,scenicSpotId", [(date, dataparm["productid"], dataparm["scenicSpotId"])])
    def test_miniverify(self, date, productid, scenicSpotId):
        orderid = self.api.buyprocedure(date, productid)['data']['id']
        self.api.payprocedure(orderid)
        verifycode = self.api.ticketdetail(orderid)['data']['verifyCode']
        print(verifycode)
        json = self.api.miniverify(scenicSpotId, verifycode)
        assert json["msg"] == "success"
