#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/4/14 9:06 
# @Author : huxiaoliang
# @Description : 
# @See：

# 关闭警告
import warnings

warnings.filterwarnings("ignore")

import  wordcloud   # 生成词云
wc = wordcloud.WordCloud(height = 1000, width = 1000, font_path = 'simsun.ttc')
wc.generate(' '.join(words_fin))

from matplotlib import pyplot as plt

plt.imshow(wc)
wc.to_file('/Users/atom-g/spyder/Cai.png')      # 图片至本地
# see：https://blog.csdn.net/weixin_38411989/article/details/106025837