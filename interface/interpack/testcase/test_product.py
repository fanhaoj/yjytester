import allure

from interface.interpack.api.api_product import ApiProduct


@allure.feature("产品相关")
class TestProduct:
#allure执行：pytest test_product.py --allure-features "产品相关"
    def setup(self):
        self.a=ApiProduct()

    @allure.story("发布产品")
    def test_createproduct(self):
        with allure.step("创建产品"):
            re=self.a.create_product()
            assert re["msg"] == "success"
