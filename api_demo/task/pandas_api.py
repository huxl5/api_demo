#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/5/24 18:17 
# @Author : huxiaoliang@citicbank.com
# @Description : 
# @See：
# 基本操作https://blog.csdn.net/DaGongJiGuoMaLu09/article/details/107703139
# map apply mapapply np.where# ：https://zhuanlan.zhihu.com/p/100064394
# https://blog.csdn.net/m0_69435474/article/details/124327108


import warnings

# 关闭警告
warnings.filterwarnings("ignore")

from pandas import Series,DataFrame
import numpy as np


# 1、Series 的创建
# 通过列表创建，此时会默认从 0 开始创建索引
sel1 = Series([1, 2, 3, 4])
print(sel1)

# 通过指定数据和索引创建
sel2 = Series(data=[1, 2, 3, 4], index=list('abcd'))
print(sel2)

# 通过字典创建，字典的键是索引，值是数据
d3 = {'red': 120, 'blue': 30, 'green': 80}
sel3 = Series(d3)
print(sel3)
# 2、Series 基本属性
print(sel2.index.tolist(),sel2.values.tolist(),sel2[2],sel2['b'],sel2[[0,1]],sel2[['a','b']],sel2[1:3],sel2['b':'d'],sep='\n')

sel4 = sel2.drop(['a','b'])
print(sel2,sel4,'\n')

# Series 的索引值可以重新设置：
sel1.index = list('bdca')
print(sel1)
# 这种方式会直接改变 Series 本身的索引，如果不想改变原始 Series，可以使用 reindex：
# 这种方式返回一个新的 Series，缺失值用 NaN 填补。
sel5 = sel1.reindex(list('abcdr'))
print(sel5)



# 通过二维数组创建
df1 = DataFrame(np.random.randint(0,10,(4,4)), index=[1,2,3,4], columns=list('abcd'))

# 通过字典创建，字典的键是列索引，行索引需另行指定
d2 = {'language':['python', 'C++', 'java', 'PHP'],
      'rank':[1,2,3,4],
      'score':[90, 60, 100, 65]}
df2 = DataFrame(d2)		# index可以省略（有默认值）

# 字典的值也可以是 Series 对象，相同的索引会一一对应，缺少的值会用NaN填充
d3 = {'a':sel1, 'b':sel2, 'c':sel3}
df3 = DataFrame(d3)

print(df3.ndim,df3.shape,type(df3.values),df3.values)
print(df2.info,type(df2['rank']),type(df2[['rank']]))
print(df3)
print('='*30)
print(df3.loc['a'])
print(df3.loc['a', 'b'])
print(df3.loc['a', ['b', 'c']])
print(df3.loc[['a', 'b'], ['a', 'b']])

print(df3.iloc[1])
print(df3.iloc[1, 2])
print(df3.iloc[1, 2:4])
print(df3.iloc[1:3, 2:4])


df['result'].map(lambda x: x.split('邮箱')[0])				# result 列的所有元素，以"邮箱"为分隔符，提取分隔后的第一个值，删除后面的



