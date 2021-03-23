# -*- coding: utf-8 -*-
import logging
import time


class Testpra:
    def test_sanjiao(self):
        str=input("input:")
        print(str)
        a,b,c=eval(str)
        if a+b>c and a+c>b and b+c>a:
            print(a+b,c)
            print('可构成')
        else:
            print('不可组成')
            return False
        if a==b==c:
            print('等边')
        elif a==b or a==c or b==c:
            print('等腰')
        else:
            print(a==b | a==c | b==c)
            print('全三角')

class timethis:

    def timethis(func):
        def inner(*args, **kwargs):
            print('start timer:')
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print('end timer:%fs.' % (end - start))
            return result

        return inner

    @timethis
    def sleeps(seconds):
        print('  sleeps begin:')
        time.sleep(seconds)
        print('    sleep %d seconds.\n  sleeps over.' % seconds)
        return seconds


if __name__ == '__main__':
    print(timethis().sleeps(3))



