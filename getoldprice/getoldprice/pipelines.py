# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from pymongo import IndexModel, ASCENDING
from getoldprice.items import priceitem
from getoldprice.price_type import p_jd_type, p_tb_item

class GetoldpricePipeline(object):
    def __init__(self):
        client = pymongo.MongoClient("localhost", 27017)
        db1 = client['京东']
        db2 = client['淘宝']
        jd_item_list = ''
        for jd_item in list(set(p_jd_type)):#这个是让每次搜索的名字之间加一个+，需要更改。
            item_list = item_list + 's'
        self.PhRes

    def process_item(self, item, spider):
        return item
