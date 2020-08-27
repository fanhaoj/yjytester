from string import Template

import requests
import yaml


class BaseApi():

    def send(self,data):
        self.env = yaml.safe_load(open("../data/env.yaml", "r"))
        data["url"]=str(data["url"]).replace("yjy.zhiyousx.com:8765",self.env["test-env"][self.env["default"]])
        return requests.request(**data).json()

    def template(self,file,data):
        with open(file,"r",encoding='utf-8') as f:
            re=Template(f.read()).safe_substitute(data)
            return yaml.safe_load(re)
