import datetime
import time

from interface.interpack.api.base_api import BaseApi
from interface.interpack.until.until import Until


class ApiOrder(BaseApi):

    def __init__(self):
        u=Until()
        self.gytoken=u.gytoken()
        self.fxtoken=u.fxtoken()
        self.begindate=u.begindate()

    #下单
    def buyprocedure(self,productid):
        data={
            "fxtoken":self.fxtoken,
            "date":self.begindate,
            "productId": productid
        }
        data=self.reqtemplate('../data/trip-order/order.yaml', data, "buyprocedure")
        return self.send(data)

    #支付
    def payprocedure(self,buyorderid):
        data={
            "fxtoken":self.fxtoken,
            "buyorderid":buyorderid
        }
        data=self.reqtemplate("../data/trip-order/order.yaml", data, "payprocedure")
        return self.send(data)

    #退款
    def refund(self,buyorderid):
        data={
            "fxtoken":self.fxtoken,
            "buyorderid":buyorderid
        }
        data=self.reqtemplate("../data/trip-order/order.yaml", data, "refund")
        return self.send(data)

    #核销
    def verify(self,buyorderid):
        data={
            "fxtoken":self.gytoken,
            "buyorderid":buyorderid
        }
        data=self.reqtemplate("../data/trip-order/order.yaml", data, "verify")
        return self.send(data)

    # 查询订单详情
    def ticketdetail(self,buyorderid):
        data={
            "gytoken":self.gytoken,
            "buyorderid":buyorderid
        }
        data=self.reqtemplate("../data/trip-order/order.yaml", data, "ticketdetail")
        return self.send(data)

    def waitorderstatus(self, orderid,status):
        """

        :param orderid: 订单id
        :param status: 状态
        """
        try:
            orderstatus = self.ticketdetail(orderid)["data"]["orderStatus"]
            assert orderstatus == status
        except Exception as e:
            bool = True
            while (bool):
                orderstatus = self.ticketdetail(orderid)["data"]["orderStatus"]
                if orderstatus == status:
                    bool = False


    # h5页面订单详情查询
    def verify_h5(self,buyorderid):
        data={
            "fxtoken":self.fxtoken,
            "buyorderid":buyorderid
        }
        data=self.reqtemplate("../data/trip-order/order.yaml", data, "verify_h5")
        return self.send(data)

    #取消订单
    def cancel(self,ordersn):
        data={
            "fxtoken":self.fxtoken,
            "ordersn":ordersn
        }
        data=self.reqtemplate("../data/trip-order/order.yaml", data, "cancel")
        return self.send(data)

    #重发短信
    def remessage(self,contactsMobile,ordersn):
        data={
            "gytoken":self.gytoken,
            "contactsMobile": contactsMobile,
            "orderSn": ordersn
        }
        data=self.reqtemplate("../data/trip-order/order.yaml", data, "remessage")
        return self.send(data)

    #小程序核销
    def miniverify(self,scenicSpotId,verifyCode):
        data= {
            "gytoken": self.gytoken,
            "scenicSpotId": scenicSpotId,
            "verifyCode": verifyCode
            }
        data=self.reqtemplate("../data/trip-order/order.yaml", data, "miniverify")
        return self.send(data)

    # 分销用户常用旅客
    def TopContactsList(self):
        data={
            "fxtoken": self.fxtoken
        }
        data=self.reqtemplate("../data/trip-order/order.yaml", data, "TopContactsList")
        return self.send(data)

    # 消息队列测试接口
    def mqTest(self):
        data={
            "fxtoken": self.fxtoken
        }
        data=self.reqtemplate("../data/trip-order/order.yaml", data, "mqTest")
        return self.send(data)

    #手动处理出票中订单到出票失败
    def ManualProcessing(self,buyorderid):
        data={
            "fxtoken": self.fxtoken,
            "buyorderid": buyorderid
        }
        data=self.reqtemplate("../data/trip-order/order.yaml", data, "ManualProcessing")
        return self.send(data)

    #手动处理退款中订单
    def manuallyProcessRefundOrders(self,buyorderid):
        data={
            "fxtoken": self.fxtoken,
            "buyorderid": buyorderid,
            "status":0
        }
        data=self.reqtemplate("../data/trip-order/order.yaml", data, "ManualProcessing")
        return self.send(data)


if __name__ == '__main__':
    a=ApiOrder()
    a.waitorderstatus(117283,3)
