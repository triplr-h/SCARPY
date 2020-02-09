#coding:utf-8
import requests
import logging
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from Search_WebHub.items import PornVideoItem
from Search_WebHub.pornhub_type import PH_TYPES
from scrapy.http import Request
import re
import json
import random



class Spider(CrawlSpider):
    name = 'Search_pornHubSpider'
    host = 'https://www.pornhub.com'
    start_urls = list(set(PH_TYPES))
    logging.getLogger("requests").setLevel(logging.WARNING
                                          )  # 将requests的日志级别设成WARNING
    logging.basicConfig(
        level=logging.DEBUG,
        format=
        '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename='cataline.log',
        filemode='w')

    # test = True
    def start_requests(self):
        for ph_type in self.start_urls:
            print("开始搜索：" + ph_type + "\n")
            yield Request(url='https://www.pornhub.com/video/search?search=%s' % ph_type,
                          callback=self.parse_ph_key)

    def parse_ph_key(self, response):
        selector = Selector(response)
        logging.debug('request url:------>' + response.url)
        # logging.info(selector)
        print("搜索成功，开始解析网页......\n")
        divs = selector.xpath('//div[@class="phimage"]') # 找到每个搜索结果，都存在这个含phimage的class里面
        for div in divs:
            # logging.debug('divs :------>' + div.extract())

            viewkey = re.findall('viewkey=(.*?)"', div.extract()) # 找到储存有视频信息的a标签，并保存viewkey（就是等于号后面的一堆）
            print("获取viewkey：" + str(viewkey[0]) + "\n")
            # logging.debug(viewkey)
            # 下面的这个yield打开的是单个视频的窗口，能够从中提取文件或视频（就是下载链接）
            yield Request(url='https://www.pornhub.com/embed/%s' % viewkey[0],
                          callback=self.parse_ph_info)

        # 翻页用，这个定位翻页的链接
        url_next = selector.xpath(
            '//a[@class="orangeButton" and text()="Next "]/@href').extract()
        logging.debug(url_next)
        # 执行翻页的request
        if url_next:
            # if self.test:
            print("翻页中......\n")
            logging.debug(' next page:---------->' + self.host + url_next[0])
            yield Request(url=self.host + url_next[0],
                          callback=self.parse_ph_key)
            # self.test = False
        

    def parse_ph_info(self, response):
        phItem = PornVideoItem()
        selector = Selector(response)
        # logging.info(selector)
        _ph_info = re.findall('var flashvars =(.*?),\n', selector.extract()) #找到储存有视频信息的script文件，也就是下面的一大堆信息
        logging.debug('PH信息的JSON:')
        logging.debug(_ph_info) # 这个就是一大堆信息的那个
        _ph_info_json = json.loads(_ph_info[0])
        duration = _ph_info_json.get('video_duration')
        phItem['video_duration'] = duration
        title = _ph_info_json.get('video_title')
        phItem['video_title'] = title
        image_url = _ph_info_json.get('image_url')
        phItem['image_url'] = image_url
        link_url = _ph_info_json.get('link_url')
        phItem['link_url'] = link_url
        quality_480p = _ph_info_json.get('quality_480p')
        phItem['quality_480p'] = quality_480p
        word_list = ''
        for word in list(set(PH_TYPES)):
            word_list = word_list + ' + ' + word
        word_list = word_list[3:]
        phItem['search_words'] = word_list
        # phItem['download_url'] = download_url
        # 有的下载链接直接就是mp4文件，有的是分段文件，需要区分开

        logging.info('duration:' + duration + ' title:' + title + ' image_url:'
                     + image_url + ' link_url:' + link_url + ' search_words:' + word_list + '\n')
        print('收集到信息：' + ' 时长：' + duration + ' 标题：' + title + ' 图片链接：'
              + image_url + ' 视频链接：' + link_url + ' 搜索关键词：' + word_list + '\n')
        yield phItem
