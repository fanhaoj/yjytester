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

class BaseApi():
    def send(self,data):
        return requests.request(**data).json()