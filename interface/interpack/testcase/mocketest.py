
import requests


def test_reqmeituan():
    data={
        "url":"http://rap2.taobao.org:38080/app/mock/266076/order/create",
        "method":"post",

    }
    print(requests.request(**data).json())

def invoke_mock_request():
    return test_reqmeituan()


"""
This example shows how to send a reply from the proxy immediately
without sending any data to the remote server.
"""
from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    # pretty_url takes the "Host" header of the request into account, which
    # is useful in transparent mode where we usually only have the IP otherwise.

    if flow.request.pretty_url == "https://www.baidu.com/":
        flow.response = http.HTTPResponse.make(
            200,  # (optional) status code
            b"Hello World12345",  # (optional) content
            {"Content-Type": "text/html"}  # (optional) headers
        )

if __name__ == '__main__':
    request()