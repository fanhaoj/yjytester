
from interface.interpack.api.base_api import BaseApi
from interface.interpack.until.until import Until


class ApiOrderfx(BaseApi):

    def __init__(self):
        u=Until()
        self.sign=u.getsign('6310931416','264V35g1xl3623777Q4yCEj02k4MY663','123456')
        self.begindate=u.begindate()

    def buyprocedure_fx(self,productId,sellerOrderSn):
        """
        分销商下单
        :param productId:产品id
        :return:
        """
        data={
            "curTime": self.sign[0],
            "sign": self.sign[1],
            "date":self.begindate,
            "productId": productId,
            "sellerOrderSn":sellerOrderSn
        }
        data=self.reqtemplate("../data/trip-order/order_fenxiao.yaml",data,'buyprocedure_fx')
        return self.send(data)

    def payprocedure_fx(self,orderSn):
        """
        分销商支付
        :param orderSn:
        """
        data={
            "curTime": self.sign[0],
            "sign": self.sign[1],
            "orderSn": orderSn
        }
        data=self.reqtemplate("../data/trip-order/order_fenxiao.yaml",data,'payprocedure_fx')
        return self.send(data)

    def refund_fx(self,orderSn):
        """
        分销商退款
        :param orderSn:
        """
        data={
            "curTime": self.sign[0],
            "sign": self.sign[1],
            "orderSn": orderSn
        }
        data=self.reqtemplate("../data/trip-order/order_fenxiao.yaml",data,'refund_fx')
        return self.send(data)

    def getpricecalendar_fx(self,productId):
        """
        获取价格日历
        :param productId:
        """
        data={
            "curTime": self.sign[0],
            "sign": self.sign[1],
            "productId": productId
        }
        data=self.reqtemplate("../data/trip-order/order_fenxiao.yaml",data,'getpricecalendar_fx')
        return self.send(data)

    def selectorder_fx(self,orderSn):
        """
        分销商订单查询
        :param productId:
        """
        data={
            "curTime": self.sign[0],
            "sign": self.sign[1],
            "productId": orderSn
        }
        data=self.reqtemplate("../data/trip-order/order_fenxiao.yaml",data,'selectorder_fx')
        return self.send(data)

    def selectproduct_fx(self,productId):
        """
        查询门票信息
        :param productId:
        """
        data={
            "curTime": self.sign[0],
            "sign": self.sign[1],
            "productId": productId
        }
        data=self.reqtemplate("../data/trip-order/order_fenxiao.yaml",data,'selectproduct_fx')
        return self.send(data)

    def sellerordercreate(self):
        """
        下游创建订单
        """
        data={
            "url":"http://yapi.devdemo.trs.net.cn/mock/510/yjy/sellerorder/create",
            "method":"post"
        }
        return self.send(data)




