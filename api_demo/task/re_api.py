#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/5/4 15:45 
# @Author : huxiaoliang
# @Description : 
# @See：

# 关闭警告
import warnings

warnings.filterwarnings("ignore")

import re

matchObj =re.search(r'供应.{0,30}(中断|生变|限制|风险|重创|问题|紧张|无法.{0,5}恢复)','供应产业(03708.HK):公司相信日后不会出现沟通中断或再出现生变')
matchObj =re.search(r'财务造假|财务风险|数字造假','起步股份财务造假被罚5700万,陈丽红带领ABC童装1年关店417家 子弹财经')
matchObj =re.search(r'(CEO|董事长|总经理|实控人|实际控制人|).{0,5}破产','起步股份财务造假被破产罚5700万,陈丽红带领ABC童装1年关店417家 子弹财经')
# matchObj =re.search(r'抽贷$','辉侃‖ 为什么银行会突然抽贷')


# matchObj =re.search(r'流动性(.*)困难|告急|不足|压力','若发现植筋胶挤胶困难、流动性差，首先我们需要考虑胶体的成分和质量问题。劣质的植筋胶则会因为环氧树脂纯度不高、不合理的添加填料，以及采用了劣质的添加剂、固化剂导致植筋困难，胶 ')
if matchObj:

    print("match --> searchObj.group() : ", matchObj.group(),matchObj.span())
else:
    print("No match!!")

org_black_pattern = r'国务院|省委|市委|县委|银保监会|证监会|监管局|证监局|交易所|深交所|沪交所|港交所|信托|证券|财联社|新闻|媒体|财经|日报|时报|观察报|财报|经济网|协会|事务所|联储|董事会|网站$|网$'
org_black_list = ['多米诺骨牌', '专网', '*', '结婚产业观察', '关联', '中国网',]
if not re.search(org_black_pattern, '爱国网X') and '爱国网' not in org_black_list:
    print('match!!')
else:
    print("No match!!")



# line = "Cats are smarter than dogs"
#
# matchObj = re.match(r'dogs', line, re.M | re.I)
# if matchObj:
#     print("match --> matchObj.group() : ", matchObj.group())
# else:
#     print("No match!!")
#
# matchObj = re.search(r'dogs', line, re.M | re.I)
# if matchObj:
#     print("match --> searchObj.group() : ", matchObj.group())
# else:
#     print("No match!!")