#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/4/18 13:56 
# @Author : huxiaoliang
# @Description : 
# @See：https://hanlp.hankcs.com/demos/ner.html#msra%E8%A7%84%E8%8C%83

# 关闭警告
import warnings

warnings.filterwarnings("ignore")

from hanlp_restful import HanLPClient
# 创建客户端，填入服务器地址和秘钥：
url = 'https://www.hanlp.com/api'
# url = 'https://www.hanlp.com/api/ner/nerMsra'
# url = 'http://comdo.hanlp.com/hanlp/v1/segment/crf'
# url = 'http://comdo.hanlp.com/hanlp/v21/ner/ner'
# url = 'http://comdo.hanlp.com/hanlp/v21/ner/nerPku'
HanLP = HanLPClient(url, auth='MjMzNkBiYnMuaGFubHAuY29tOjVPaGpUeUI2VkJBVzR6Vmo=', language='zh') # auth不填则匿名，zh中文，mul多语种
# HanLP = HanLPClient(url, auth='db69c93d99504cb288abff3b3f722bb01681885341451token', language='zh') # auth不填则匿名，zh中文，mul多语种

# 无论何种开发语言，调用parse接口，传入一篇文章，得到HanLP精准的分析结果。
print(HanLP.parse("2021年HanLPv2.1为生产环境带来次世代最先进的多语种NLP技术。阿婆主来到北京立方庭参观自然语义科技公司。"))

# 命名实体识别
# 同时执行所有标准的命名实体识别：
print(HanLP('2021年HanLPv2.1为生产环境带来次世代最先进的多语种NLP技术。阿婆主来到北京立方庭参观自然语义科技公司。', tasks='ner*'))

# 任务越少，速度越快。如指定仅执行命名实体识别，默认MSRA标准：
HanLP('来源：环球市场播报　　瑞典最大的养老基金Alecta周二宣布，其首席执行官Magnus Billing将立即辞职，此前该公司披露在美国多家银行的投资出现巨额亏损。　　Alecta上月表示，其在美国硅谷银行、签名银行和第一共和银行的持股损失了196亿瑞典克朗（约合18.7亿美元）。本月较早时，该公司宣布其股票主管Liselott Ledin被停职，因其对Alecta成为美国这三家地区银行的大股东负有直接责任。　　该公司周二在一份声明中表示：“董事会得出结论，Alecta需要新的领导层，以便在资产管理内部实施必要的改革，并重新建立信任。”　　Alecta表示，在寻找新首席执行官期间，副首席执行官Katarina Thorslund将暂时领导公司。', tasks='ner').pretty_print()
print(HanLP(
    '来源：环球市场播报　　瑞典最大的养老基金Alecta周二宣布，其首席执行官Magnus Billing将立即辞职，此前该公司披露在美国多家银行的投资出现巨额亏损。　　Alecta上月表示，其在美国硅谷银行、签名银行和第一共和银行的持股损失了196亿瑞典克朗（约合18.7亿美元）。本月较早时，该公司宣布其股票主管Liselott Ledin被停职，因其对Alecta成为美国这三家地区银行的大股东负有直接责任。　　该公司周二在一份声明中表示：“董事会得出结论，Alecta需要新的领导层，以便在资产管理内部实施必要的改革，并重新建立信任。”　　Alecta表示，在寻找新首席执行官期间，副首席执行官Katarina Thorslund将暂时领导公司。',
    tasks='ner'))
print(HanLP('2021年HanLPv2.1为生产环境带来次世代最先进的多语种NLP技术。阿婆主来到北京立方庭参观自然语义科技公司。', tasks='ner'))


# 为已分词的句子执行命名实体识别：
HanLP(tokens=[["阿婆主", "来到", "北京立方庭", "参观", "自然语义科技公司", "。"]], tasks='ner').pretty_print()


# import hanlp
# HanLP = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH) # 世界最大中文语料库
# HanLP(['2021年HanLPv2.1为生产环境带来次世代最先进的多语种NLP技术。', '阿婆主来到北京立方庭参观自然语义科技公司。'])
sentences = [
    "我在上海林原科技有限公司兼职工作，我经常在台川喜宴餐厅吃饭，偶尔去开元地中海影城看电影。"
]

print(HanLP('我在上海林原科技有限公司兼职工作，我经常在台川喜宴餐厅吃饭，偶尔去开元地中海影城看电影。', tasks='ner/msra'))
