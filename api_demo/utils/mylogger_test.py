#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/4/12 9:28 
# @Author : huxiaoliang
# @Description : 
# @See：

# 关闭警告
import warnings

warnings.filterwarnings("ignore")
# 导入同路径包
import sys
import os

cur_path = os.getcwd()
print(cur_path)
# print(sys.path)
# sys.path.append(cur_path)
print(sys.path)
# 导入报错，可Mark Directory as source root
from mylogger import Logger

log = Logger('../data/all.log', level='debug')
log.logger.debug('debug')
log.logger.info('info')
log.logger.info('info{}'.format(False))
log.logger.warning('警告')
log.logger.error('报错')
log.logger.critical('严重')
Logger('../data/error.log', level='error').logger.error('error')
