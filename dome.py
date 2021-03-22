#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 0024 20:24
# @Author  : XYY
def f():
    a=10
    b=0
    try:
        c=a/b
        print(c)
    except ZeroDivisionError as e:
        print(e)
        # raise e
print("ss")

h = f()
print(h)
