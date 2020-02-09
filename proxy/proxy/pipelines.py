# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ProxyPipeline(object):
    def process_item(self, item, spider):
        #if spider.name == 'kdlspider':
        #    open('G:\Git_code\SCRAPY\proxy\proxy\data\kdl_proxy.txt').write(item['addr'] + '\n')
        print(item['addr'])
        return item
