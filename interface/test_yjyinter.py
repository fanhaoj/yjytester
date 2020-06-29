#coding=utf-8

# Name:         test_yjyinter
# Description:  
# Author:       hao.fan
# Date:         2020/5/11

# coding=utf-8
import json

import pytest
import requests


class Test_inter:

    def setup(self):
        self.t = globals()

    def test_gyLogin(self):
        url = "http://yjy.zhiyousx.com:8765/api/auth/jwt/token"
        data = {"username": "ziyuan", "password": "123456", "platformType": "NORMAL"}
        headers = {"Content-Type": "application/json"}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        result = r.text
        # print(result)
        jsr = json.loads(result)
        gytoken = jsr['data']
        self.t['gy'] = gytoken
        assert r.status_code == 200

    def test_fxLogin(self):
        url = "http://yjy.zhiyousx.com:8765/api/auth/jwt/token"
        data = {"username": "haofanfx", "password": "123456", "platformType": "NORMAL"}
        headers = {"Content-Type": "application/json"}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        result = r.text
        # print(result)
        jsr = json.loads(result)
        fxtoken = jsr['data']
        self.t['fx'] = fxtoken
        assert r.status_code == 200

    # 下单
    @pytest.mark.parametrize('buypay')
    def test_buyprocedure(self):
        url = "http://yjy.zhiyousx.com:8765//api/order/order/ticket/create"
        data = {"departDate": "2020-05-08", "productId": "1878", "productNum": "1",
                "touristInfo": [{"name": "测试", "mobile": "15009253686"}]}
        headers = {"Authorization": self.t['fx'], "Content-Type": "application/json"}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        result = r.text
        print(result)
        jsr = json.loads(result)
        orderid = jsr[data][id]
        self.t['orderids'] = orderid
        assert r.status_code == 200

    # 支付
    @pytest.mark.parametrize('buypay')
    def test_payprocedure(self):
        url = "http://yjy.zhiyousx.com:8765//api/order/order/ticket/pay/credit?orderId=" + self.t['orderids']
        data = {"departDate": "2020-05-08", "productId": "1878", "productNum": "1",
                "touristInfo": [{"name": "测试", "mobile": "15009253686"}]}
        headers = {"Authorization": self.t['fx'], "Content-Type": "application/json"}
        r = requests.post(url, data, headers)
        print(r.text)
        assert r.status_code == 200

    # 退款
    def test_refund(self):
        url = "http://yjy.zhiyousx.com:8765/api/order/order/ticket/refund"
        data = {"orderId": self.t['orderids'], "reason": "拍错退款", "refundNum": 1}
        headers = {"Authorization": self.t['fx'], "Content-Type": "application/json"}
        r = requests.post(url, data, headers)
        print(r.text)
        assert r.status_code == 200

    # 取消订单
    def test_cancel(self):
        url = "http://yjy.zhiyousx.com:8765/api/order/order/ticket/cancel"
        data = {"orderId": self.t['orderids'], "reason": "拍错退款", "refundNum": 1}

        headers = {"Authorization": self.t['fx'], "Content-Type": "application/x-www-form-urlencoded"}
        r = requests.post(url, data, headers)