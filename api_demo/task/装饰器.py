#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/5/7 11:08 
# @Author : huxiaoliang
# @Description : 
# @See：https://mp.weixin.qq.com/s?__biz=MzA5NjgzODM3Ng==&mid=2650534086&idx=2&sn=0a9db486758dd803c45506bd8dafff77&chksm=88a6a741bfd12e57accf3001c306a2790c10b5063aed6d1fb03680b052bca906f203a09cb500&scene=27

# 关闭警告
import warnings

warnings.filterwarnings("ignore")

import time

def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        exec_time = time.time() - start_time
        print(func.__name__,"函数运行耗时：{exec_time:.6f}s".format(exec_time=exec_time))
        return res
    return wrapper

@timer
def add(a,b):
    return a+b
@timer
def sub(a,b):
    return a-b


print(add(6,9))
print(sub(7,8))
