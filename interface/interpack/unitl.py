from interface.interpack.base_api import BaseApi


class Unitl(BaseApi):
    def gyLogin(self):
        data={
            "method":"post",
            "url":"http://yjy.zhiyousx.com:8765/api/auth/jwt/token",
            "headers":{"Content-Type": "application/json"},
            "json":{
                "username": "ziyuan",
                "password": "123456",
                "platformType": "NORMAL"
            }
        }
        r=self.send(data)
        gytoken=r['data']
        return gytoken

    def fxLogin(self):
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
        r=self.send(data)
        fxtoken=r['data']
        return fxtoken

if __name__ == '__main__':
    u=Unitl()
    u.fxLogin()