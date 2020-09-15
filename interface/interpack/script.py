"""Send a reply from the proxy without sending any data to the remote server."""
from mitmproxy import http, ctx


def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url == "http://yapi.devdemo.trs.net.cn/mock/510/yjy/qumaip/create":
        flow.request.url = "http://yapi.devdemo.trs.net.cn/mock/510/yjy/qumaip/create"
        ctx.log.info(repr("url: "+flow.request.url))
        ctx.log.info(repr("method: "+flow.request.method))
    if flow.request.pretty_url == "http://yapi.devdemo.trs.net.cn/mock/510/yjy/qumaip/createfalse":
        flow.request.url = "http://yapi.devdemo.trs.net.cn/mock/510/yjy/qumaip/createfalse"
        ctx.log.info(repr("url: " + flow.request.url))
        ctx.log.info(repr("method: " + flow.request.method))
        # flow.response = http.HTTPResponse.make(
        #     200,  # (optional) status code
        #     b"Hello World",  # (optional) content
        #     {"Content-Type": "text/html"}  # (optional) headers
        # )

# class Count:
#     def request(self,flow):
#         # flow.request.headers['User-Agent'] = 'MitmProxy'
#         flow.request.url="http://yapi.devdemo.trs.net.cn/mock/510/yjy/qumaip/create"
#         # flow.request.method='post'
#         ctx.log.info(repr("url: "+flow.request.url))
#         ctx.log.info(repr("method: "+flow.request.method))
#
#
# addons=[
#     Count()
# ]
# def response(flow):
#     response=flow.response
#     ctx.log.info(str(response.text))


# if __name__ == '__main__':
#     request()