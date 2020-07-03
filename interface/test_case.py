#coding=utf-8
import json

import pytest
import requests
import  time
# from interface.api import Test_Interyjy

class Test_Interyjy():
    # def setup(self):

    #下单支付
    def test_buyandpay(self,fxLogin,buyprocedure):
        url = "http://yjy.zhiyousx.com:8765//api/order/order/ticket/pay/credit?orderId="+str(buyprocedure)
        data = {}
        headers = {"Authorization":fxLogin,"Content-Type": "application/json"}
        print(f"3:{fxLogin}")
        r=requests.post(url,data=json.dumps(data),headers=headers)
        assert  r.status_code==200

    #下单退款
    def test_refund(self,fxLogin,buyprocedure):
        url = "http://yjy.zhiyousx.com:8765/api/order/order/ticket/refund"
        data = {"orderId":buyprocedure,"reason":"拍错退款","refundNum":1}
        headers = {"Authorization":fxLogin,"Content-Type": "application/json"}
        print(f"4:{fxLogin}")
        r=requests.post(url,data=json.dumps(data),headers=headers)
        print(r.text)
        assert r.status_code==200

    #取消订单
    def test_cancel(self,fxLogin,ticketdetail):
        url = "http://yjy.zhiyousx.com:8765/api/order/order/ticket/cancel"
        data = {"orderSn": ticketdetail}
        headers = {"Authorization": fxLogin, "Content-Type": "application/x-www-form-urlencoded"}
        r = requests.post(url, data=data, headers=headers)
        print(r.text+"cancel")
        assert r.status_code==200

    #核销订单
    def test_verify(self,gyLogin, buyprocedure,payprocedure):
        url = "http://yjy.zhiyousx.com:8765//api/order/order/ticket/verify"
        data = {"num": 1, "orderId": buyprocedure}
        headers = {"Authorization": gyLogin, "Content-Type": "application/json"}
        r = requests.post(url,data=json.dumps(data),headers=headers)
        print(r.json())
        assert r.status_code == 200

    #小程序核销
    def test_miniverify(self,gyLogin,verify_h5):
        url="http://yjy.zhiyousx.com:8765/api/order/order/ticket/app/verify"
        data={{"scenicSpotId": 282,"verifyCode": verify_h5}}
        headers = {"Authorization": gyLogin, "Content-Type": "application/json"}
        r=requests.post(url,data=data,headers=headers)

    def test_

if __name__ == '__main__':
    pytest.main()