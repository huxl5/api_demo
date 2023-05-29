#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/5/22 15:53 
# @Author : huxiaoliang@citicbank.com
# @Description : 
# @See：https://blog.csdn.net/AI_Clay/article/details/128466307


import warnings

# 关闭警告
warnings.filterwarnings("ignore")

import pandas as pd

# 设置测试数据
Database = pd.DataFrame()
Database['test'] = [['1', '3', '4'], ['2', '3', '5'], ['1', '2', '3', '5'], ['2', '5']]

print('原数据格式类型之列表：', type(Database['test'].iloc[0]))
# 原数据格式类型之列表： <class 'list'>

# 写入excel
Database.to_csv('./Database_str.csv', index=False)

# 再读取出来，问题就出现了，list变成了str
Database = pd.read_csv('./Database_str.csv')
print('读入后数据格式类型之列表：', type(Database['test'].iloc[0]))
# 读入后数据格式类型之列表： <class 'str'>