# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdltspiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #标题
    title=scrapy.Field()
    #问题
    ask=scrapy.Field()
    #帖子回复时间
    time_now=scrapy.Field()
    #用户
    user=scrapy.Field()
    #回复
    answer=scrapy.Field()
    #内容
    content=scrapy.Field()
    #url
    href=scrapy.Field()
    #讨论ID
    talk_ID=scrapy.Field()
    #搜索次数
    search=scrapy.Field()
    #爬取时间
    ProgramStarttime=scrapy.Field()