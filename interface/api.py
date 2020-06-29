import json

import requests


class Login:
    def gyLogin(self):
        url = "http://yjy.zhiyousx.com:8765/api/auth/jwt/token"
        data = {"username": "ziyuan", "password": "123456", "platformType": "NORMAL"}
        headers = {"Content-Type": "application/json"}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        gytoken=r.json()['data']
        return gytoken
        assert r.status_code == 200


    def fxLogin(self):
        url = "http://yjy.zhiyousx.com:8765/api/auth/jwt/token"
        data = {"username": "haofanfx", "password": "123456", "platformType": "NORMAL"}
        headers = {"Content-Type": "application/json"}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        fxtoken=r.json()['data']
        return fxtoken
        assert r.status_code == 200

if __name__ == '__main__':
    l=Login()
    l.fxLogin()