#coding=utf-8
import json

import pytest
import requests
import  time
# from interface.api import Test_Interyjy

class Test_Interyjy():
    # def setup(self):
    global date,list
    date=time.strftime("%Y-%m-%d",time.localtime())
    list={}
    print(list)

    #下单支付
    def test_buyandpay(self,fxLogin,buyprocedure):
        url = "http://yjy.zhiyousx.com:8765//api/order/order/ticket/pay/credit?orderId="+str(buyprocedure)
        data = {}
        headers = {"Authorization":fxLogin,"Content-Type": "application/json"}
        r=requests.post(url,data=json.dumps(data),headers=headers)
        assert  r.status_code==200

    #下单退款
    def test_refund(self,fxLogin,buyprocedure):
        url = "http://yjy.zhiyousx.com:8765/api/order/order/ticket/refund"
        data = {"orderId":buyprocedure,"reason":"拍错退款","refundNum":1}
        headers = {"Authorization":fxLogin,"Content-Type": "application/json"}
        r=requests.post(url,data=json.dumps(data),headers=headers)
        print(r.text)
        assert r.status_code==200

    #取消订单
    def test_cancel(self,fxLogin,buyprocedure):
        url = "http://yjy.zhiyousx.com:8765/api/order/order/ticket/cancel"
        data = {"orderSn": buyprocedure}
        headers = {"Authorization": fxLogin, "Content-Type": "application/x-www-form-urlencoded"}
        r = requests.post(url, data, headers)
        print(r.text)
        assert r.status_code==200