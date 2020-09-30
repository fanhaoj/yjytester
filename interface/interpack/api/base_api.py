import json
import time
from string import Template
import logging
import requests
import yaml


class BaseApi():
    logging.basicConfig(level=logging.INFO)

    def send(self,data):
        date = time.strftime("%H-%M-%S", time.localtime())
        self.env = yaml.safe_load(open("../data/env.yaml", "r"))
        data["url"]=str(data["url"]).replace("yjy.zhiyousx.com:8765",self.env["test-env"][self.env["default"]])
        logging.info(date+" 请求数据: " +repr(data)+ "\n")
        json=requests.request(**data).json()
        logging.info("响应数据: " +repr(json)+ "\n")
        return json

    def reqtemplate(self,file,data,name):
        with open(file,"r",encoding='utf-8') as f:
            steps=yaml.safe_load(f)[name]
            re=Template(str(steps)).safe_substitute(data)
            # print(re)
            return yaml.safe_load(re)
