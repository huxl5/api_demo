#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/4/12 16:21 
# @Author : huxiaoliang
# @Description : TODO:1、还需要安装东西
# @See：

# 关闭警告
import warnings
warnings.filterwarnings("ignore")
# 使用自己的日志模块


from pyhanlp import *
sample='又是快乐（悲伤）写（ctrlcv）代码的一天呢！'
seg = HanLP.segment(sample)
print(seg)