#coding=utf-8
import json

import pytest
import requests
import  time

# class Test_Interyjy():
#     # def setup(self):
#     global date,list
#     date=time.strftime("%Y-%m-%d",time.localtime())
#     list={}
#     print(list)

#下单

url="http://yjy.zhiyousx.com:8765"
def send():
    req={"method":"post",
         "url":url+"/api/auth/jwt/token",
         "headers":{"Authorization": "token", "Content-Type": "application/x-www-form-urlencoded"}
         }
    requests.request()