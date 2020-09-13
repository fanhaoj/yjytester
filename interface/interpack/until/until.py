import time

import yaml

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
                "username": "ziyuan",
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

    def makedatatest(self,file,proname,key):
        """

        :param file:添加数据驱动文件
        :param proname:数据类型名称
        :param key:数据key值
        :return:
        """
        with open(file,"r",encoding='utf-8') as f:
            re=str(yaml.safe_load(f)[proname][key])
            print(re)
            return re







if __name__ == '__main__':
    # Until().convent_yaml()
    Until().makedatatest("../data/trip-order/order_data.yaml","proqmp","productid")
