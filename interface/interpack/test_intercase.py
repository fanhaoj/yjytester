import time

import pytest

from interface.interpack.api_meth import ApiMeth
from interface.interpack.base_api import BaseApi
from interface.interpack.unitl import Unitl


date = time.strftime("%Y-%m-%d", time.localtime())
productid=1317
scenicSpotId=287

class TestYjy(BaseApi):
    def setup(self):
        self.api=ApiMeth()


    @pytest.mark.parametrize("date,productid",[(date,productid)])
    def test_buyandpay(self,date,productid):
        orderid=self.api.buyprocedure(date,productid)['data']['id']
        json=self.api.payprocedure(orderid)
        assert json["msg"] == "success"

    def test_refund(self,data,productid):
        orderid=self.api.buyprocedure(date,productid)['data']['id']
        self.api.payprocedure(orderid)
        json=self.api.refund(orderid)
        assert json["msg"] == "success"

    def test_cancel(self):
        orderid = self.api.buyprocedure(date, productid)['data']['id']
        ordersn=self.api.ticketdetail(orderid)['data']['orderSn']
        json=self.api.cancel(ordersn)
        assert json["msg"] == "success"

    def test_verify(self):
        orderid=self.api.buyprocedure(date,productid)['data']['id']
        self.api.payprocedure(orderid)
        json=self.api.verify(orderid)
        assert json["msg"] == "success"

    def test_miniverify(self):
        orderid=self.api.buyprocedure(date,productid)['data']['id']
        self.api.payprocedure(orderid)
        verifyCode=self.api.ticketdetail(orderid)['data']['verifyCode']
        json=self.api.miniverify(scenicSpotId,verifyCode)
        assert json["msg"] == "success"




