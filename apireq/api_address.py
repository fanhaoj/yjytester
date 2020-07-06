import requests

from apireq.base_api import BaseApi


class Address(BaseApi):
    def get_token(self):
        res = None
        # 获取 token
        # while FileLock("session.lock"):
        corpid = "wwa26dee94d70aa6e7"
        corpsecret = "TM-PNqujpmiAo46PQGBiikCWEYFXWzD8RYjmi0d--EU"
        data={
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "param": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }
        self.send(**data)["access_token"]

    def get(self,get_token,userid):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "param": {
                     "access_token":get_token,
                     "userid": userid
        }
        }
        self.send(**data)

    def create(self,get_token,userid,name,mobile):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "param": {"access_token":get_token},
            "json":{
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": [1],
            }
        }
        self.send(**data)

    def update(self,get_token,userid,name,mobile):
        data={
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "param": {"access_token": get_token},
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile,
            }
        }
        self.send(**data)

    def delete(self,get_token,userid):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "param": {
                     "access_token":get_token,
                     "userid": userid
        }
        }
        self.send(**data)

