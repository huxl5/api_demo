#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/5/22 17:17 
# @Author : huxiaoliang@citicbank.com
# @Description : 
# @See：


import warnings

# 关闭警告
warnings.filterwarnings("ignore")

s = "Hello"
if s.isalpha():
    print("The string is all letters")
else:
    print("The string contains non-letters")
# import re
# if re.match(r'\w+', s):
#     print("The string is all letters")
# else:
#     print("The string contains non-letters")
#
# # 匹配字符串中的字母
# string = "hello world"
# match = re.match(r"[a-zA-Z]+", string)
#
# if match:
#     print("匹配到字母:", match.group())
# else:
#     print("没有匹配到字母")


print('1.9'.isdigit())
print('1.9'.isdecimal())

print(type(eval('我')))

