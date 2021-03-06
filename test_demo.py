#coding=utf-8

# Name:         test_demo
# Description:  
# Author:       hao.fan
# Date:         2020/5/11
import json
from datetime import time
from time import sleep

import pytest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_interyjy():
    # def setup(self):
    #     self.t=globals()
    #     print("变量："+ str(self.t))



    @pytest.fixture()
    def test_buyprocedure(self,fxLogin):
        url = "http://yjy.zhiyousx.com:8765//api/order/order/ticket/create"
        data = {"departDate": "2020-05-14", "productId": "1878", "productNum": "1",
                "touristInfo": [{"name": "测试", "mobile": "15009253686"}]}
        headers = {"Authorization": fxLogin, "Content-Type": "application/json"}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        result = r.text
        print(result)
        jsr = json.loads(result)
        orderid = jsr['data']['id']
        assert r.status_code == 200
        yield orderid

    def test_payprocedure(self,fxLogin,test_buyprocedure):
        url = "http://yjy.zhiyousx.com:8765//api/order/order/ticket/pay/credit?orderId=" + str(test_buyprocedure)
        data = {"departDate": "2020-05-14", "productId": "1878", "productNum": "1",
                "touristInfo": [{"name": "测试", "mobile": "15009253686"}]}
        headers = {"Authorization": fxLogin, "Content-Type": "application/json"}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        result=r.text
        print(result)
        assert r.status_code == 200

    @pytest.mark.parametrize('data',[1,2,3,4])
    def test_demo2(self,data):
        print(data)

    def test_ecwait(self):
        WebDriverWait.until(expected_conditions.element_has_css_class(By.XPATH,'ssd'))
        WebDriverWait.until(wait)