# -*- coding: utf-8 -*-

from httpfaker.utils.faker_tool import Provider

class MyProvider(Provider):
    def verify_accounts(self, userE, tradeNum):
        users = {
            'user001': 'xiaoming',
            'user002': '654321',
            'xiaoming': '123456'
        }
        if userE in users and users.get(userE) == tradeNum:
            return {"code": 200, "msg": "请求成功"}
        elif userE not in users:
            return {'code': 1002, 'msg': "用户不存在"}
        else:
            return {"code": 1001, "msg": "密码不正确"}

    def gen_token(self, username):
        return {"token": self.uuid()}