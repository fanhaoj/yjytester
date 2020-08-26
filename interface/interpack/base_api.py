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
import yaml


class BaseApi():
    env = yaml.safe_load(open("env.yaml"))

    def send(self, data):
        data["url"] = str(data["url"]).replace("yjy.zhiyousx.com:8765", self.env["test-env"][self.env["default"]])
        print(data["url"])
        print(data)
        return requests.request(**data).json()

    # def send(self,data):
    #     return requests.request(**data).json()