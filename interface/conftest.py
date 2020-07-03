#coding=utf-8

# Name:         conftest
# Description:  
# Author:       hao.fan
# Date:         2020/5/12
import json
import time
from time import sleep

import pytest
import requests

global date, list,productid
date = time.strftime("%Y-%m-%d", time.localtime())
productid=1317
scenicSpotId=71
list = {}
print(date)


@pytest.fixture(scope="session")
def gyLogin():
    url = "http://yjy.zhiyousx.com:8765/api/auth/jwt/token"
    data = {"username": "ziyuan", "password": "123456", "platformType": "NORMAL"}
    headers = {"Content-Type": "application/json"}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    gytoken = r.json()['data']
    yield gytoken
    assert r.status_code == 200


@pytest.fixture(scope="session")
def fxLogin():
    url = "http://yjy.zhiyousx.com:8765/api/auth/jwt/token"
    data = {"username": "haofanfx", "password": "123456", "platformType": "NORMAL"}
    headers = {"Content-Type": "application/json"}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    fxtoken = r.json()["data"]
    print(f"1:{fxtoken}")
    yield fxtoken
    assert r.status_code == 200

#下单
@pytest.fixture()
def buyprocedure(fxLogin):
    url = "http://yjy.zhiyousx.com:8765//api/order/order/ticket/create"
    data = {"departDate":date,"productId":productid,"productNum":"1","touristInfo":[{"name":"测试","mobile":"15009253686"}]}
    headers = {"Authorization":fxLogin,"Content-Type": "application/json"}
    print(f"2:{fxLogin}")
    r=requests.post(url,data=json.dumps(data),headers=headers)
    orderid = r.json()['data']['id']
    return orderid
    assert r.status_code == 200

#支付
@pytest.fixture()
def payprocedure(fxLogin,buyprocedure):
    url = "http://yjy.zhiyousx.com:8765//api/order/order/ticket/pay/credit?orderId="+str(buyprocedure)
    data = {}
    headers = {"Authorization":fxLogin,"Content-Type": "application/json"}
    r=requests.post(url,data=json.dumps(data),headers=headers)
    assert r.status_code==200

#查询订单详情
@pytest.fixture()
def ticketdetail(fxLogin,buyprocedure):
    url="http://yjy.zhiyousx.com:8765//api/order/order/ticket/"+str(buyprocedure)+"/detail"
    data={}
    headers={"Authorization": fxLogin}
    r = requests.get(url, headers=headers)
    print(r.json()['data']['orderSn'])
    ordersn=r.json()['data']['orderSn']
    return ordersn
    assert r.status_code == 200

#h5页面订单详情查询
def verify_h5():
    url="http://yjy.zhiyousx.com:8765/api/order/external/orderDetail"
    data={"orderId":buyprocedure}
    headers={"Authorization":gyLogin,"Content-Type": "application/json"}
    r=requests.post(url,data=data,headers=headers)

if __name__ == '__main__':
    buyprocedure()
