#coding=utf-8
import json

import pytest
import requests
import  time
from interface.api import Login

class Test_Interyjy():
    # def setup(self):
    global date,list
    date=time.strftime("%Y-%m-%d",time.localtime())
    list={}
    print(list)

    def setup(self):
        lo=Login()
        self.fxlogin=lo.fxLogin()
        self.gyLogin=lo.gyLogin()

    #下单
    @pytest.fixture(autouse=True)
    def test_buyprocedure(self):
        url = "http://yjy.zhiyousx.com:8765//api/order/order/ticket/create"
        data = {"departDate":"2020-06-29","productId":"1317","productNum":"1","touristInfo":[{"name":"测试","mobile":"15009253686"}]}
        headers = {"Authorization":self.fxlogin,"Content-Type": "application/json"}
        r=requests.post(url,data=json.dumps(data),headers=headers)
        orderid = r.json()['data']['id']
        print(orderid)
        return  orderid
        assert r.status_code == 200

    #支付
    # @pytest.fixture()
    def test_payprocedure(self,test_buyprocedure):
        url = "http://yjy.zhiyousx.com:8765//api/order/order/ticket/pay/credit?orderId="+str(test_buyprocedure)
        data = {}
        headers = {"Authorization":self.fxlogin,"Content-Type": "application/json"}
        print(fxLogin)
        r=requests.post(url,data=json.dumps(data),headers=headers)
        print(r.text)
        assert  r.status_code==200

    #退款
    def test_refund(self,fxLogin,test_buyprocedure,test_payprocedure):
        url = "http://yjy.zhiyousx.com:8765/api/order/order/ticket/refund"
        data = {"orderId":test_buyprocedure,"reason":"拍错退款","refundNum":1}
        headers = {"Authorization":fxLogin,"Content-Type": "application/json"}
        r=requests.post(url,data=json.dumps(data),headers=headers)
        print(r.text)
        assert r.status_code==200

    #取消订单
    def test_cancel(self,fxLogin,test_buyprocedure):
        url = "http://yjy.zhiyousx.com:8765/api/order/order/ticket/cancel"
        data = {"orderSn": test_buyprocedure}
        headers = {"Authorization": fxLogin, "Content-Type": "application/x-www-form-urlencoded"}
        r = requests.post(url, data, headers)
        print(r.text)
        assert r.status_code==200