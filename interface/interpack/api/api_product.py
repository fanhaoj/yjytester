from interface.interpack.api.base_api import BaseApi
from interface.interpack.until.until import Until


class ApiProduct(BaseApi):

    def __init__(self):
        u=Until()
        self.fxtoken=u.fxtoken()
        self.gytoken=u.gytoken()

    def create_product(self):
        data={
            "gytoken":self.gytoken
        }
        data=self.template("../data/product.yaml", data)
        return self.send(data)
