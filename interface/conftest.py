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
    result = r.text
    jsr = json.loads(result)
    gytoken = jsr['data']
    yield gytoken
    assert r.status_code == 200


@pytest.fixture(autouse=True)
def fxLogin():
    url = "http://yjy.zhiyousx.com:8765/api/auth/jwt/token"
    data = {"username": "haofanfx", "password": "123456", "platformType": "NORMAL"}
    headers = {"Content-Type": "application/json"}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    result = r.text
    print(result)
    jsr = json.loads(result)
    fxtoken = jsr['data']
    assert r.status_code == 200
    yield fxtoken