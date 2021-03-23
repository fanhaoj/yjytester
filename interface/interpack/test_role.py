# -*- coding: utf-8 -*-

import requests
import yaml


class TestRole:

    def test_rolecre(self):
        data={
            "url":"http://yjy.zhiyousx.com:8765/api/user/role/child/create",
            "method":"post",
            "headers":{
                'Authorization': 'eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJ6aXl1YW4iLCJ1c2VySWQiOiIxOTIiLCJwaG9uZSI6IjE1MDA5MjUzNjg2IiwiY2VydGlmaWNhdGlvblR5cGUiOiIyIiwicm9sZUlkIjoiMiIsIkRhdGFBdXRoSWQiOiIiLCJwYXJlbnRJZCI6IjE5MiIsImRhdGFBdXRoVHlwZSI6IjEiLCJ1c2VySG9zdCI6IjEyNC4xMTQuMTUxLjgyIiwiZXhwIjoxNjAxMTYxMzgyfQ.FPeBmHnNcCjoQsk6xtH0g_7-zUZB6KmQlajsySu-hsrqGKMu744eVBmZjY-1qcFXUmcpx0NLUvxQGedmx9lDcPgcCkxA_72B4F3DqGTLAXnUWnb7a__mIpZEBdY7EVqvfcdVSD6uFSgCd0IrHrQOq3HA7lvvf3rOAuZCWZmtCT4',
                'Content-Type': 'application/json; charset=UTF-8'
            },
            "json": "法国发生"

        }
        requests.request(**data)


    def  test_yaml(self):
        with open("../ccencode.yaml") as f:
            yy=yaml.safe_load(f)
        print(yy)