#coding=utf-8

# Name:         testdemo2
# Description:  
# Author:       hao.fan
# Date:         2020/6/28
import time


# def timethis(func):
#     def inner(*args,**kwargs):
#         print('start timer:')
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print('end timer:%fs.'%(end - start))
#         return result
#     return inner
#
# @timethis
# def sleeps(seconds):
#     print('  sleeps begin:')
#     time.sleep(seconds)
#     print('    sleep %d seconds.\n  sleeps over.'%seconds)
#     return seconds
#
# print(sleeps(3))
from audioop import reverse


def res():
    a='asdf3'
    print(list(reversed(a)))
    print(a[::-1])

    cars = ['Honda', 'toyota', 'hyundai', 'byd', 'ford', 'suzuki', 'peuguot', 'nissan', 'citroen', 'kia', 'vw', 'gm','audi', 'bmw', 'beniz']
    cars.reverse()
    print(cars)
    # print(sorted(cars, key=reverse))


if __name__ == '__main__':
    res()
