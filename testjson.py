#coding=utf-8

# Name:         testjson
# Description:  
# Author:       hao.fan
# Date:         2020/5/13
import json

json1={"code":0,"data":{"id":308566},"msg":"success","desc":"null"}
f=json.dumps(json1)
c=json.loads(f)
print(json1["data"]["id"])
print(f[2])
print(c["msg"])
