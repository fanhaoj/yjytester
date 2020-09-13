from interface.interpack.api.base_api import BaseApi
from interface.interpack.until.until import Until


class ApiProduct(BaseApi):

    def __init__(self):
        u=Until()
        self.fxtoken=u.fxtoken()
        self.gytoken=u.gytoken()
        self.begindate=u.begindate()
        self.enddate=u.enddate()

    def create_product(self):
        data={
            "gytoken":self.gytoken,
            "begindate":self.begindate,
            "enddate":self.enddate
        }
        data=self.reqtemplate("../data/trip-product/product.yaml", data, "createproduct")
        return self.send(data)

    def modify_product(self):
        data={
            "gytoken":self.gytoken
        }
        data=self.reqtemplate("../data/trip-product/product.yaml", data, "modify")
        return self.send(data)