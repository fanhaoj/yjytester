
import yaml

from interface.interpack.api.base_api import BaseApi


class Until(BaseApi):
    def fxtoken(self):
        data={
            "method":"post",
            "url":"http://yjy.zhiyousx.com:8765/api/auth/jwt/token",
            "headers":{"Content-Type": "application/json"},
            "json":{
                "username": "haofanfx",
                "password": "123456",
                "platformType": "NORMAL"
            }
        }
        return self.send(data)["data"]

    def gytoken(self):
        data={
            "method": "post",
            "url": "http://yjy.zhiyousx.com:8765/api/auth/jwt/token",
            "headers": {"Content-Type": "application/json"},
              "json":{
                "username": "ziyuan",
                "password": "123456",
                "platformType": "NORMAL"
            }
        }
        return self.send(data)["data"]

    #生成yaml文件
    def convent_yaml(self):
        data={
            "departDate": "2020-08-19",
            "productId": "1317",
            "productNum": "1",
            "touristInfo": [
                {
                    "name": "测试",
                    "mobile": "15009253686"
                }
            ]
        }
        with open("../data/order.yaml","w",encoding='utf-8') as f:
            yaml.safe_dump(data=data,stream=f,allow_unicode=True)






if __name__ == '__main__':
    Until().convent_yaml()
