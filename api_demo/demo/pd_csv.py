#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/5/12 16:38 
# @Author : huxiaoliang
# @Description : 
# @See：

# 关闭警告
import warnings

warnings.filterwarnings("ignore")
import pandas as pd
def csv_file_read():
    # 读取表头
    head_row = pd.read_csv('../data/pd.csv', nrows=0)
    print(list(head_row))
    # 表头列转为 list
    head_row_list = list(head_row)

    # 读取
    csv_result = pd.read_csv('../data/pd.csv', usecols=head_row_list)
    print(csv_result['标题'])
    row_list = csv_result.values.tolist()
    print(f"行读取结果：{row_list}")
    col_obj = csv_result.T
    col_list = col_obj.values.tolist()
    print(f"行转列读取结果：{col_list}")
    return head_row_list, col_list

if __name__ == '__main__':
    csv_file_read()