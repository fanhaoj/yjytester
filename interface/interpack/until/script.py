"""Send a reply from the proxy without sending any data to the remote server."""
from mitmproxy import http, ctx


def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url == "http://yapi.devdemo.trs.net.cn/mock/510/yjy/qumaip/create":
        flow.request.url = "http://yapi.devdemo.trs.net.cn/mock/510/yjy/qumaip/create"
        ctx.log.info(repr("url: "+flow.request.url))
        ctx.log.info(repr("method: "+flow.request.method))
    if flow.request.pretty_url == "http://yapi.devdemo.trs.net.cn/mock/510/yjy/qumaip/createfalse":
        flow.request.url = "http://yapi.devdemo.trs.net.cn/mock/510/yjy/qumaip/create"
        ctx.log.info(repr("url: " + flow.request.url))
        ctx.log.info(repr("method: " + flow.request.method))


# if __name__ == '__main__':
#     request()