import yaml

from interface.interpack.api.base_api import BaseApi
from interface.interpack.api.base_gettoken import Unitl


class ApiProduct(BaseApi):
    def __init__(self):
        u = Unitl()
        self.gytoken = u.gyLogin()
        self.fxtoken = u.fxLogin()


    def create_ticket(self):
        # data={
        #     "method":"post",
        #     "url":"http://yjy.zhiyousx.com:8765/api/product/ticket/push",
        #     "headers":{"Authorization": self.gytoken, "Content-Type": "application/json"},
        #     "json":{
        #             "dateType": 2,
        #             "stockLimit": 1,
        #             "ticketName": "autotest",
        #             "sceneryName": "云创科技",
        #             "scenicSpotId": "1",
        #             "scenicSpotName": "云创科技",
        #             "sceneryId": "71",
        #             "sellType": "ALL",
        #             "sellDate": [],
        #             "homePageStatus": "",
        #             "selldirectImgPath": "[]",
        #             "bookDayLimit": "0",
        #             "bookTimeLimit": "23:59",
        #             "reserveBeforeTime": 0,
        #             "minBookNum": "1",
        #             "maxBookNum": "999",
        #             "validityPeriod": {
        #                 "type": 1
        #             },
        #             "checkMode": "0",
        #             "refundCheckMode": "1",
        #             "refundRuleType": "3",
        #             "isPartialRefund": "0",
        #             "isRefund": 0,
        #             "touristInfoType": "1",
        #             "verifyType": "1",
        #             "printState": "0",
        #             "isSendSms": "0",
        #             "smsContent": "尊敬的游客，您的订单$code$已预约成功，游玩日期$day$，验证码为$password$，$qrcode$表示二维码，$thirdOrderSn$表示订单号祝您旅途愉快！咨询电话029-89663510。",
        #             "feeIncludes": "<p>特殊阿斯顿发生ff</p>",
        #             "feeNotIncludes": "<p>特殊阿斯顿发生ff2333</p>",
        #             "reachWay": "<p>撒飞洒地方a&#39;f</p>",
        #             "refundNote": "<p>af 请3撒旦发射点发</p>",
        #             "bookNote": "<p>阿斯蒂芬撒旦发顺丰打赏33改好发给的</p>",
        #             "thirdPlatformId": "0",
        #             "thirdProductId": 0,
        #             "thirdSceneryId": 0,
        #             "thirdSupplierId": "",
        #             "status": 1,
        #             "id": "1341"
        #         }
        # }
        data={
            "Authorization":self.gytoken
        }
        data=self.template("../data/data.yaml",data)
        return self.send(data)