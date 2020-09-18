from interface.interpack.api.api_alarmsystem import ApiAlarmsystem


class TestAlarmsystem:

    def setup(self):
        self.api=ApiAlarmsystem()

    def test_getErrorType(self):
        json=self.api.getErrorType()
        assert json["msg"] == "success"
        assert json["code"] == 0

