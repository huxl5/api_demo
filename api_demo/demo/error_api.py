#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/5/17 19:38 
# @Author : huxiaoliang@citicbank.com
# @Description : 
# @See：


import warnings

# 关闭警告
warnings.filterwarnings("ignore")
try:
    try:
        520 + "FishC"
    except:
        print("内部异常！")
    # 1 / 0
except:
    print("外部异常！")
finally:
    print("收尾工作~")
