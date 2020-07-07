from apireq.base_api import BaseApi


class Wework(BaseApi):
    def get_token(self,corpsecret):
        # 获取 token
        # while FileLock("session.lock"):
        corpid = "wwa26dee94d70aa6e7"
        data={
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }
        print(self.send(data)["access_token"])
        return self.send(data)["access_token"]

    def create_data(self):
        data=[("wu123fff" + str(x), "zhangsan"+ str(x), "138%08d" % x) for x in range(20)]
        print(data)
        return data

if __name__ == '__main__':
    Wework().create_data()