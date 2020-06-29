#coding=utf-8

# Name:         conftest
# Description:  
# Author:       hao.fan
# Date:         2020/5/12
import json
from time import sleep

import pytest
import requests


@pytest.fixture(scope="module")
def gyLogin():
    url = "http://yjy.zhiyousx.com:8765/api/auth/jwt/token"
    data = {"username": "ziyuan", "password": "123456", "platformType": "NORMAL"}
    headers = {"Content-Type": "application/json"}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    gytoken = r.json()['data']
    yield gytoken
    assert r.status_code == 200


@pytest.fixture(autouse=True)
def fxLogin():
    url = "http://yjy.zhiyousx.com:8765/api/auth/jwt/token"
    data = {"username": "haofanfx", "password": "123456", "platformType": "NORMAL"}
    headers = {"Content-Type": "application/json"}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    fxtoken = r.json()["data"]
    yield fxtoken
    assert r.status_code == 200

#下单
@pytest.fixture(autouse=True)
def buyprocedure(fxLogin):
    url = "http://yjy.zhiyousx.com:8765//api/order/order/ticket/create"
    data = {"departDate":"2020-06-29","productId":"1878","productNum":"1","touristInfo":[{"name":"测试","mobile":"15009253686"}]}
    headers = {"Authorization":fxLogin,"Content-Type": "application/json"}
    r=requests.post(url,data=json.dumps(data),headers=headers)
    orderid = r.json()['data']['id']
    print(orderid)
    return  orderid
    assert r.status_code == 200

#支付
@pytest.fixture(autouse=True)
def payprocedure(self,fxLogin,buyprocedure):
    url = "http://yjy.zhiyousx.com:8765//api/order/order/ticket/pay/credit?orderId="+str(buyprocedure)
    data = {}
    headers = {"Authorization":fxLogin,"Content-Type": "application/json"}
    r=requests.post(url,data=json.dumps(data),headers=headers)
    assert  r.status_code==200

if __name__ == '__main__':
    fxLogin()
