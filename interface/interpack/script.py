from mitmproxy import ctx


def request(flow):
    # flow.request.headers['User-Agent'] = 'MitmProxy'
    flow.request.url="http://yapi.devdemo.trs.net.cn/mock/510/yjy/qumaip/createfalse"
    # flow.request.method='post'
    ctx.log.info(repr("url: "+flow.request.url))
    ctx.log.info(repr("method: "+flow.request.method))


def response(flow):
    response=flow.response
    ctx.log.info(str(response.text))


if __name__ == '__main__':
    request()