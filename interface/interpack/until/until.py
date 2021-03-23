import hashlib
import time

import yaml
import pymysql
from interface.interpack.api.base_api import BaseApi


class Until(BaseApi):
    def fxtoken(self):
        data={
            "method":"post",
            "url":"http://yjy.zhiyousx.com:8765/api/auth/jwt/token",
            "headers":{"Content-Type": "application/json"},
            "json":{
                "username": "haofanfx",
                "password": "123456",
                "platformType": "NORMAL"
            }
        }
        return self.send(data)["data"]

    def gytoken(self):
        data={
            "method": "post",
            "url": "http://yjy.zhiyousx.com:8765/api/auth/jwt/token",
            "headers": {"Content-Type": "application/json"},
              "json":{
                "username": "haofanyjy",
                "password": "123456",
                "platformType": "NORMAL"
            }
        }
        return self.send(data)["data"]

    def convent_yaml(self):
        """
        生成yaml文件
        """
        data={
    "dateType": "2",
    "stockLimit": 1,
    "ticketName": "autotest",
    "sceneryName": "云创科技",
    "scenicSpotId": "1",
    "scenicSpotName": "云创科技",
    "sceneryId": "71",
    "sellType": "ALL",
    "sellDate": [
        {
            "beginSellDate": "2021-03-17",
            "endSellDate": "2022-03-31",
            "setWeeks": [
                "7",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6"
            ],
            "dailyStock": "-1",
            "costAmount": "0.01",
            "agentAmount": "0.01",
            "storeAmount": "0.01",
            "marketAmount": "0.01"
        }
    ],
    "bookDayLimit": "0",
    "bookTimeLimit": "23:59",
    "minBookNum": "1",
    "maxBookNum": "999",
    "validityPeriod": {
        "type": 1
    },
    "checkMode": "0",
    "refundCheckMode": "1",
    "refundRuleType": "3",
    "expiringOperation": "1",
    "isPartialRefund": "0",
    "isRefund": 0,
    "touristInfoType": "1",
    "verifyType": "1",
    "printState": "0",
    "isSendSms": "1",
    "feeIncludes": "<p>fe</p>",
    "feeNotIncludes": "<p>few</p>",
    "reachWay": "<p>we</p>",
    "refundNote": "<p>qwer</p>",
    "bookNote": "<p>wqerqwer</p>",
    "thirdPlatformId": "0",
    "thirdProductId": 0,
    "thirdSceneryId": 0,
    "thirdSupplierId": "",
    "status": 1
}
        with open("../data/trip-order/order_fenxiaotstswesetse.yaml", "w", encoding='utf-8') as f:
            yaml.safe_dump(data=data,stream=f,allow_unicode=True)

    def getsign(self,apiKey,apiSecret,nonce):
        """

        :param apiKey:
        :param apiSecret:
        :param nonce:随机数
        :return:密钥列表
        """
        self.time=int(time.time())
        # data='apiKey='+str(apiKey)+'&'+'apiSecret='+str(apiSecret)+'&'+'curTime='+str(self.time)+'&'+'nonce='+str(nonce)
        data = str(apiKey) + str(nonce)+ str(self.time)+str(apiSecret)  #曲文旅靠谱小程序芙蓉园sign
        sha1 = hashlib.sha1()
        sha1.update(data.encode('utf-8'))
        sha1_data=sha1.hexdigest()
        list=[]
        list.append(self.time)
        list.append(sha1_data)
        print(list)
        return list

    def begindate(self):
        """

        :return:开始日期
        """
        date = time.strftime("%Y-%m-%d", time.localtime())
        return date

    def enddate(self):
        """

        :return:结束日期
        """
        date = "2022-12-31"
        return date

    def makedatatest(self,file,proname):
        """

        :param file:添加数据驱动文件
        :param proname:数据类型名称
        :param key:数据key值
        :return:
        """
        with open(file,"r",encoding='utf-8') as f:
            re=yaml.safe_load(f)[proname]
            print(re)
            print(type(re))
            return re

    def delete_order(self):
        """
            teardown 创建订单后删除创建的订单
        """
        conn = pymysql.connect(host="mysql-cn-north-1-05454410e59740b2.public.jcloud.com", port=3306, user="yjy_mysql", passwd="Zz36952751",database="introtec_trip_cloud",charset="utf8")
        cursor=conn.cursor()
        sql1="""
            DELETE from trip_order_info ORDER BY id desc limit 2;
            """
        sql2 = """
            DELETE from trip_order_ticket ORDER BY id desc limit 2;
               """
        sql3 = """
            DELETE from trip_order ORDER BY id desc limit 2;
               """
        try:
            cursor.execute(sql1)
            cursor.execute(sql2)
            cursor.execute(sql3)
            conn.commit()
        except pymysql.Error as e:
            error = 'MySQL execute failed! ERROR (%s): %s' % (e.args[0], e.args[1])
            print(error)
        conn.close()






if __name__ == '__main__':
    Until().convent_yaml()
    # a=Until().getsign('6310931416','264V35g1xl3623777Q4yCEj02k4MY663','123456')
    # print(a[0],a[1])
    # Until().makedatatest("../data/trip-order/order_data.yaml","test_miniverify")
    # Until().delete_order()