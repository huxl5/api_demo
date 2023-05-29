#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/4/12 15:16 
# @Author : huxiaoliang
# @Description : 1、csv分割符测试
# @See：

# 关闭警告
import warnings

warnings.filterwarnings("ignore")

import csv

csv_file = open("csv_test.csv", 'w', newline='',encoding='utf')  # 解决中文乱码问题。a+表示向csv文件追加,w直接写入;utf-8-sig;
writer = csv.writer(csv_file, delimiter="u\001")
writer.writerow(['标题', '新闻来源'])
datalist = [{'title': '阿里', 'source': 'baidu'}, {'title': '京东', 'source': 'baidu'}]
for data in datalist:
    writer.writerow(
        [data['title'], data['source'], ])
csv_file.close()
