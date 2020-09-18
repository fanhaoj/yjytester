import datetime
import hashlib
import json
from datetime import time
import time

import requests


class GetSign:
    #sha1加密生成sign签名
    def getsign(self,apiKey,apiSecret,nonce):
        """

        :param apiKey:
        :param apiSecret:
        :param nonce:
        :return:
        """
        self.time=int(time.time())
        data='apiKey='+str(apiKey)+'&'+'apiSecret='+str(apiSecret)+'&'+'curTime='+str(self.time)+'&'+'nonce='+str(nonce)
        print(data)
        sha1 = hashlib.sha1()
        sha1.update(data.encode('utf-8'))
        sha1_data=sha1.hexdigest()
        print(sha1_data)
        a=[]
        a.append(self.time)
        a.append(sha1_data)
        return a



    def test_create(self,time,sign):
        header={
            "Content-Type":"application/json",
            "apiKey":"6310931416",
            "curTime":time,
            "nonce":"123456",
            "sign":sign
        }
        data={
    "contactsIdCard": "610403199805203012",
    "contactsMobile": "15009253686",
    "contactsName": "测试",
    "departDate": "2020-08-14",
    "productId": 1335,
    "productNum": 1,
    "sellerOrderSn": "12345896547954",
    "touristInfo": [
        {
            "email": "286305896@qq.com",
            "idCard": "610525199802050819",
            "mobile": "15009253658",
            "name": "测试"
        }
    ]
}

        r=requests.request('post','http://yjy.zhiyousx.com:8765/api/openApi/order/ticket/create',headers=header,data=json.dumps(data))
        print(r.json())
if __name__ == '__main__':
    gt=GetSign()
    dd=gt.getsign('emhhamkxZDQwNzYzYjQ=','emhhamkxNTJkZTFkMThjNmEyNDZjMQ==','123456')
    print(dd)
    gt.test_create(str(dd[0]),dd[1])




    # time=int(time.time())
    # print(time)
    #
    # sha1=hashlib.sha1()
    # data='apiKey=0180512853&apiSecret=PO7W7il6Bk1X1Pd9nUO00bk4x5b36Jfu&curTime=1597387126&nonce=123456'
    # sha1.update(data.encode('utf-8'))
    # sha1_data=sha1.hexdigest()
    # print(sha1_data)