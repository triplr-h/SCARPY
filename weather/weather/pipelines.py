# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests
import json
import codecs
import pymysql


class WeatherPipeline(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir + 'data/weather.txt'

        with open(filename, 'a') as f:
            f.write(item['date'] + '\n')
            f.write(item['week'] + '\n')
            f.write(item['tem_h'] + '\n')
            f.write(item['tem_l'] + '\n')
            f.write(item['weather'] + '\n')
            f.write(item['wind'] + '\n\n')

        return item

class W2json(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir + '/data/weather.json'

        with codecs.open(filename, 'a') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(line)

        return item

class W2mysql(object):
    def process_item(self, item, spider):
        date = item['date']
        week = item['week']
        tem_h = item['tem_h']
        tem_l = item['tem_l']
        weather = item['weather']
        wind = item['wind']

        connection = pymysql.connect(
            host='localhost',
            user='triplr',
            passwd='621286',
            db='scrapyDB',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
        
        try:
            with connection.cursor() as cursor:
                sql = """INSERT INTO WEATHER(date, week, tem_h, tem_l, weather, wind) VALUES (%s, %s, %s, %s, %s, %s)"""
                cursor.execute(
                    sql, (date, week, tem_h, tem_l, weather, wind)
                )
            connection.commit()
        finally:
            connection.close()

        return item