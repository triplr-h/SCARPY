# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from pymongo import IndexModel, ASCENDING
from Search_WebHub.items import PornVideoItem
from Search_WebHub.pornhub_type import PH_TYPES


class PornhubMongoDBPipeline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["Search_PornHub"]
        word_list = ''
        for word in list(set(PH_TYPES)):
            word_list = word_list + ' + ' + word
        word_list = word_list[3:]
        self.PhRes = db[word_list]
        idx = IndexModel([('link_url', ASCENDING)], unique=True)
        self.PhRes.create_indexes([idx])
        # if your existing DB has duplicate records, refer to:
        # https://stackoverflow.com/questions/35707496/remove-duplicate-in-mongodb/35711737

    def process_item(self, item, spider):
        print("判断数据中，准备写入：" , item)
        print('\n' + '*' * 10 + '分割线' + '*' * 10 + '\n')
        #print ('MongoDBItem', item)
        """ 判断类型 存入MongoDB """
        if isinstance(item, PornVideoItem):
            #print ("数据符合要求，写入中......\n")
            try:
                self.PhRes.update_one({'link_url': item['link_url']}, {'$set': dict(item)}, upsert=True)
            except Exception:
                pass
        return item
