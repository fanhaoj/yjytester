import time

from interface.interpack.api.base_api import BaseApi
from interface.interpack.until.until import Until


class ApiAlarmsystem(BaseApi):

    def __init__(self):
        self.date = time.strftime("%Y-%m-%d", time.localtime())
        u=Until()
        self.gytoken=u.gytoken()
        self.fxtoken=u.fxtoken()

    def getErrorType(self):
        data={
            "fxtoken":self.fxtoken
        }
        data=self.reqtemplate("../data/trip-order/Alarmsystem.yaml", data, "getErrorType")
        return self.send(data)

