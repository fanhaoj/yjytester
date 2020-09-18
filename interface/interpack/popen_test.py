#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

# 使用 mkdir 命令
import time

def startproxy():
    a = 'mitmdump -s E:/GIT/yjytester/interface/interpack/until/script.py'
    os.popen(a, 'r')

def quitproxy():
    b = 'taskkill /f /t /im mitmdump.exe'
    os.popen(b, 'r')



if __name__ == '__main__':
    quitproxy()