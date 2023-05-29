#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/5/7 11:46 
# @Author : huxiaoliang
# @Description : 
# @See：https://blog.csdn.net/zywvvd/article/details/113753295
# 进度条嵌套使用
# https://www.it1352.com/2783979.html

# 关闭警告
import warnings

warnings.filterwarnings("ignore")
import  time

from tqdm import tqdm

for i in tqdm(range(100),desc='test tqdm'):
    time.sleep(0.01)
    pass

with tqdm(range(50)) as pbar:
    for i in pbar:
        pbar.set_description(str(i))
        # 手动控制进度
        pbar.update(2)
        time.sleep(0.01)
        pass