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
            "departDate": "2020-08-19",
            "productId": "1317",
            "productNum": "1",
            "touristInfo": [
                {
                    "name": "测试",
                    "mobile": "15009253686"
                }
            ]
        }
        with open("../data/trip-order/order_data.yaml", "w", encoding='utf-8') as f:
            yaml.safe_dump(data=data,stream=f,allow_unicode=True)

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
    # Until().convent_yaml()
    Until().makedatatest("../data/trip-order/order_data.yaml","test_miniverify")
    # Until().delete_order()