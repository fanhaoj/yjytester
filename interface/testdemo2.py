#coding=utf-8

# Name:         testdemo2
# Description:  
# Author:       hao.fan
# Date:         2020/6/28

class TestDemo():
    def __init__(self,t):
        self.t=t

    def test1(self):
        ss=self.t+1
        print(ss)
        return ss

    def test2(self,cc):
        tt=cc+2
        print(tt)
        return tt

if __name__ == '__main__':
    te=TestDemo(1)
    te.test1().test2()