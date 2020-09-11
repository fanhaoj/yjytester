import requests

def test_reqmeituan():
    data={
        "url":"http://rap2.taobao.org:38080/app/mock/266076/order/create",
        "method":"post",

    }
    print(requests.request(**data).json())

def invoke_mock_request():
    return test_reqmeituan()

