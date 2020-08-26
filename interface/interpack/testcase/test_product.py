from interface.interpack.api.api_product import ApiProduct


class TestProduct:
    def setup(self):
        self.api=ApiProduct()

    def test_createproduct(self):
        res=self.api.create_ticket()
        print(res)
        assert res["msg"] == "success"