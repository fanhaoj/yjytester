

import re

import pytest
import requests
from filelock import FileLock

from apireq.api_address import Address
from apireq.base_api import BaseApi
from apireq.wework import Wework


class TestRequest(BaseApi):
    def setup(self):
        self.address=Address()
        print(self.address)



    def test_get(self,userid):
        # 根据 user-id查询成员
        return self.address.get(userid)
        # res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token}&userid={userid}")
        # return res.json()

    # @pytest.mark.parametrize("userid, name, mobile",[("ffas","asdfaww","13965896325")])
    def test_create(self,userid, name, mobile):
        # 添加成员
        return self.address.create(userid,name, mobile)
        # data = {
        #     "userid": userid,
        #     "name": name,
        #     "mobile": mobile,
        #     "department": [1],
        # }
        # res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token}",
        #                     json=data
        #                     )
        # return res.json()


    def test_update(self,userid, name, mobile):
        # 更新成员
        return self.address.update(userid, name, mobile)
        # data = {
        #     "userid": userid,
        #     "name": name,
        #     "mobile": mobile,
        # }
        # res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token}",
        #                     json=data)
        # return res.json()


    def test_delete(self,userid):
        # 删除成员
        return self.address.delete(userid)
        # res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token}&userid={userid}")
        # return res.json()
    #


    @pytest.mark.parametrize("userid, name, mobile", Wework().create_data())
    def test_all(self, userid, name, mobile):
        #可能发生创建失败
        try:
            assert "created" == self.test_create(userid, name, mobile)["errmsg"]
        except AssertionError as e:
            if "mobile existed" in e.__str__():
                # 如果手机号被使用了，找出使用手机号的 userid ，进行删除
                re_userid = re.findall(":(.*)", e.__str__())[0]
                if re_userid.endswith("'") or re_userid.endswith('"'):
                    re_userid = re_userid[:-1]
                assert "deleted" == self.test_delete(userid)['errmsg']
                assert 60111 == self.test_get(re_userid)['errcode']
                assert "created" == self.test_create(userid, name, mobile)["errmsg"]
        # 可能发生userid不存在异常
        assert name == self.test_get(userid)['name']
        assert "updated" == self.test_update(userid, "xxxxxxx", mobile)['errmsg']
        assert "xxxxxxx" == self.test_get(userid)['name']
        assert "deleted" == self.test_delete(userid)['errmsg']
        assert 60111 == self.test_get(userid)['errcode']

# if __name__ == '__main__':
#     pytest.main("-v -s test_request.py::TestRequest::test_create_data")
