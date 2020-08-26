#coding=utf-8
import json
from string import Template

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
    env = yaml.safe_load(open("../data/env.yaml"))

    def send(self,data):
        data["url"]=str(data["url"]).replace("yjy.zhiyousx.com:8765",self.env["test-env"][self.env["default"]])
        return requests.request(**data).json()

    def template(self,file,data):
        with open(file,"r",encoding="utf-8") as f:
            print(file)
            print(data)
            re=Template(f.read()).safe_substitute(data)
            print(yaml.safe_load(re))
            return yaml.safe_load(re)

