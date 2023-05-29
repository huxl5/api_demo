#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/5/8 15:40 
# @Author : huxiaoliang
# @Description : 
# @See：

# 关闭警告
import warnings

warnings.filterwarnings("ignore")
import toml
import os
from pprint import pprint
cfg = toml.load(os.path.expanduser("../data/config.toml"))
pprint(cfg)
# {'mysql': {'database': 'test',
#           'fields': {'pandas_cols': ['id', 'name', 'age', 'date']},
#           'host': '127.0.0.1',
#           'parameters': {'charset': 'utf8', 'pool_size': 5},
#           'port': 3306,
#           'user': 'root'}}
