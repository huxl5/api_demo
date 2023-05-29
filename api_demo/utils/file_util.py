#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/5/6 9:36 
# @Author : huxiaoliang
# @Description : 
# @See：

# 关闭警告
import warnings

warnings.filterwarnings("ignore")
import csv
import os
import pandas as pd

# see：https://blog.csdn.net/qq_52200688/article/details/122324456
['标题',
 '新闻来源',
 '发布时间',
 '摘要',
 '第n页',
 '第n条',
 '链接',
 '正文']


def get_dictwriter(file_path, fieldnames, file_name):
    '''
    :param file_path: 文件存储路径
    :param fieldnames: 文件名
    :param file_name: 字段名 list
    :return: dictwriter
    '''
    # 打开文件
    f = open(os.path.join(file_path, '{file_name}.csv'.format(file_name=file_name)), mode='w', encoding='utf-8',
             newline='',buffering=1)
    # 文件列名
    dictwriter = csv.DictWriter(f, fieldnames=fieldnames, delimiter='`')
    # 输入文件列名
    dictwriter.writeheader()
    return dictwriter






if __name__ == '__main__':
    dic = {
        '标题': "title",
        '摘要': "abstract",
    }

    get_dictwriter('../data', ['标题', '摘要', ], '测试writer2csv').writerow(dic)

    csv_file_read()
