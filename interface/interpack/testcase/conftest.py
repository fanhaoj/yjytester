import logging
import os

import pytest

def startproxy():
    logging.info("代理开始...")
    a = 'mitmdump -s E:/GIT/yjytester/interface/interpack/until/script.py'
    os.popen(a, 'r')

def quitproxy():
    b = 'taskkill /f /t /im mitmdump.exe'
    os.popen(b, 'r')
    logging.info("代理结束end...")

# @pytest.fixture(scope="session",autouse=True)
# def proxy():
#     startproxy()
#     yield
#     quitproxy()

if __name__ == '__main__':
    # startproxy()
    quitproxy()