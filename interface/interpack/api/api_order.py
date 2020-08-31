import datetime
import time

from interface.interpack.api.base_api import BaseApi
from interface.interpack.until.until import Until


class ApiOrder(BaseApi):

    def __init__(self):
        self.date = time.strftime("%Y-%m-%d", time.localtime())
        u=Until()
        self.gytoken=u.gytoken()
        self.fxtoken=u.fxtoken()

    def createticket(self):
        data={
            "gytoken":self.fxtoken,
            "date": "2018-08-29"
        }
        print(data)
        data=self.reqtemplate("../data/order.yaml",data)
        print(data)
        return self.send(data)

#下单
    def buyprocedure(self,date,productid):
        data = {
            "method": "post",
            "url": "http://yjy.zhiyousx.com:8765/api/order/order/ticket/create",
            "headers": {"Authorization": self.fxtoken, "Content-Type": "application/json"},
            "json": {
                "departDate": date,
                "productId": productid,
                "productNum": "1",
                "touristInfo": [{"name": "测试", "mobile": "15009253686"}]
            }
        }
        return self.send(data)

    #支付
    def payprocedure(self,buyorderid):
        data = {
            "method": "post",
            "url": "http://yjy.zhiyousx.com:8765/api/order/order/ticket/pay/credit",
            "headers": {"Authorization": self.fxtoken},
            "params": {
                "orderId":buyorderid
            }
        }
        return self.send(data)

    #退款
    def refund(self,buyorderid):
        data = {
            "method": "post",
            "url": "http://yjy.zhiyousx.com:8765/api/order/order/ticket/refund",
            "headers": {"Authorization": self.fxtoken, "Content-Type": "application/json"},
            "json": {
                "orderId":buyorderid,
                "reason":"拍错退款",
                "refundNum":1
            }
        }
        return self.send(data)

    #核销
    def verify(self,buyorderid):
        data={
            "method": "post",
            "url": "http://yjy.zhiyousx.com:8765/api/order/order/ticket/verify",
            "headers": {"Authorization": self.gytoken, "Content-Type": "application/json"},
            "json":{
                "num":1,"orderId":buyorderid
            }
        }
        return self.send(data)

    # 查询订单详情
    def ticketdetail(self,buyorderid):
        data = {
            "method": "get",
            "url": "http://yjy.zhiyousx.com:8765/api/order/order/ticket/" + str(buyorderid) + "/detail",
            "headers": {"Authorization": self.fxtoken},
        }
        return self.send(data)

    # h5页面订单详情查询
    def verify_h5(self,buyorderid):
        data = {
            "method": "post",
            "url": "http://yjy.zhiyousx.com:8765/api/order/external/orderDetail",
            "headers": {"Authorization": self.fxtoken, "Content-Type": "application/json"},
            "json": {
                "orderId":buyorderid,
            }
        }
        return self.send(data)

    #取消订单
    def cancel(self,ordersn):
        data = {
            "method": "post",
            "url": "http://yjy.zhiyousx.com:8765/api/order/order/ticket/cancel",
            "headers": {"Authorization": self.fxtoken, "Content-Type": "application/x-www-form-urlencoded"},
            "data": {
                "orderSn":ordersn
            }
        }
        return  self.send(data)

    # 查询订单详情
    def ticketdetail(self, buyorderid):
        data={
            "method":"get",
            'url':f"http://yjy.zhiyousx.com:8765/api/order/order/ticket/{buyorderid}/detail",
            "headers":{"Authorization": self.gytoken}
        }
        return self.send(data)


    #重发短信
    def remessage(self,contactsMobile,ordersn):
        data={
            "method": "post",
            'url': "http://yjy.zhiyousx.com:8765/api/order/order/ticket/resendMessage",
            "headers": {"Authorization": self.gytoken},
            "json":{
                "contactsMobile": contactsMobile,
                "orderSn": ordersn
            }
        }
        return self.send(data)

    #小程序核销
    def miniverify(self,scenicSpotId,verifyCode):
        data={
            "method": "post",
            'url': "http://yjy.zhiyousx.com:8765/api/order/order/ticket/app/verify",
            "headers": {"Authorization": self.gytoken, "Content-Type": "application/json"},
            "json": {
                "scenicSpotId": scenicSpotId,
                "verifyCode": verifyCode
            }
        }
        return self.send(data)

if __name__ == '__main__':
    a=ApiOrder()
    id=a.buyprocedure('2020-08-21','1317')


if __name__ == '__main__':
    ApiOrder()