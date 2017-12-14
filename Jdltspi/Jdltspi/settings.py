# -*- coding: utf-8 -*-
BOT_NAME = 'Jdltspi'

SPIDER_MODULES = ['Jdltspi.spiders']
NEWSPIDER_MODULE = 'Jdltspi.spiders'
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 15
AUTOTHROTTLE_ENABLED = True
FIELDS_TO_EXPORT = [
    'title',
    'ask',
    'answer',
    'content',
    'time_now',
    'user',
    'href',
    'talk_ID',
    'ProgramStarttime',
    'search',
]
ITEM_PIPELINES = {
    'Jdltspi.pipelines.MongoPipeline': 190,
    'Jdltspi.pipelines.CSVPipeline':200
}
#SEARCH指的是第几次搜索，方便增量排序
SEARCH=1
MONGO_HOST = "172.28.171.13"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "JDLT"  # 库名
# MONGO_COLL = "jdlt_midea"  #美的
# MONGO_COLL = "jdlt_gree"  #格力
# MONGO_COLL = "jdlt_dajin"  #大金
# MONGO_COLL = "jdlt_haier"  #海尔
# MONGO_COLL = "jdlt_aux"  #奥克斯
# MONGO_COLL = "jdlt_dkx"  #电烤箱
# MONGO_COLL = "jdlt_hisense"  #海信
# MONGO_COLL = "jdlt_dnq"  #电暖气
MONGO_COLL = "jdlt_TCL"  #TCL
#搜索关键词,start_urls通过模拟浏览器程序得到
# SEARCH_WORD='美的'
# SEARCH_WORD='格力'
# SEARCH_WORD='大金'
# SEARCH_WORD='海尔'
# SEARCH_WORD='奥克斯'
# SEARCH_WORD='电烤箱'
# SEARCH_WORD='海信'
# SEARCH_WORD='电暖气'
SEARCH_WORD='TCL'
# LOG_FILE='LOG.txt'