#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/4/19 16:51 
# @Author : huxiaoliang
# @Description : 
# @See：https://blog.csdn.net/weixin_43997319/article/details/126106871

# 关闭警告
import warnings

warnings.filterwarnings("ignore")

import platform

print(platform.system())
print(platform.system().lower())

# for filePath in fileList:
#     global fileSplit
#     if platform.system().lower() == 'windows':
#         fileSplit = filePath.split("\\",maxsplit=-1)
#     elif platform.system().lower() == 'linux':
#         fileSplit = filePath.split(r"/",maxsplit=-1)