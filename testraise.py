#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 定义函数
import pytest


def test_mye( level ):
    if level < 1:
        raise Exception("Invalid level!")
        # 触发异常后，后面的代码就不会再执行
try:
    test_mye(0)
except Exception as err:
    print(1,err)
else:
    print(2)
