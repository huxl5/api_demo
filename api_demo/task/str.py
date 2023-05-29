#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/4/11 15:08 
# @Author : huxiaoliang
# @Description : 
# @See：

import re
# str="hello egon bcd egon lge egon acd 19 hey"
# r=re.match("h\w+",str) #match，从起始位置开始匹配，匹配成功返回一个对象，未匹配成功返回None,非字母，汉字，数字及下划线分割
# print(r.group()) # 获取匹配到的所有结果，不管有没有分组将匹配到的全部拿出来
# print(r.groups()) # 获取模型中匹配到的分组结果，只拿出匹配到的字符串中分组部分的结果
# print(r.groupdict())  # 获取模型中匹配到的分组结果，只拿出匹配到的字符串中分组部分定义了key的组结果
#
# r2=re.match("h(\w+)",str) #match，从起始位置开始匹配，匹配成功返回一个对象，未匹配成功返回None
# print(r2.group())
# print(r2.groups())
# print(r2.groupdict())
#
# r3=re.match("(?P<n1>h)(?P<n2>\w+)",str)  #?P<>定义组里匹配内容的key(键)，<>里面写key名称，值就是匹配到的内容
# print(r3.group())
# print(r3.groups())
# print(r3.groupdict())



# exit()
# 提取匹配字符串
str = "来源：雪球App，作者： 证券市场红周刊，（https://xueqiu.com/2994748381/211707059）记者 | 李健 何艳 刘增禄 齐永超 王飞编辑 | 林伟萍 李壮 张晓添校对 | 苏华   技术支持 | 王洪全芒格本次股东会经典语录·中国"
print(re.sub(r"来源：.*?）", '', str))
res = re.search(r"来源：.*?）",str)
print(re.search(r'作者： .*?，（',res.group()).group()[3:-2].strip())
print(re.search(r'来源：.*?，',res.group()).group()[3:-1].strip())
print(type(res.group()),res.group())



# re.search(r"来源：.*?）")
# 去掉匹配上的部分:re.sub匹配替换
str = "被公司的<span class='highlight'>CEO</span>包装得非<span class='highlight'>CEO</span>常好之后"
new_str = re.sub(r"<span class='highlight'>.*?</span>", '', str)
print(new_str)

exit()
# 字符串切片
print('标题：睿智医药又换CEO了,能拯救这家曾经的一线CRO吗?'[3:])
print('签名银行和第一共和 摘要结束，点击查看详情'[2:-11])

