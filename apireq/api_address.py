from interface.interpack.api.base_api import BaseApi
from apireq.wework import Wework


class Address(BaseApi):
    def __init__(self):
        corpsecret = "TM-PNqujpmiAo46PQGBiivxvYdT0X9qJ6XroMHt8QUA"
        self.token=Wework().get_token(corpsecret)

    def get(self,userid):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {
                     "access_token":self.token,
                     "userid": userid
        }
        }
        return self.send(data)

    def create(self,userid,name,mobile):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {"access_token":self.token},
            "json":{
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": [1],
            }
        }
        return self.send(data)

    def update(self,userid,name,mobile):
        data={
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params": {"access_token": self.token},
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile,
            }
        }
        return self.send(data)

    def delete(self,userid):
        data = {
            "method":"get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": {
                     "access_token":self.token,
                     "userid": userid
        }
        }
        return self.send(data)

if __name__ == '__main__':
    print(Address().delete("wu123fff2"))