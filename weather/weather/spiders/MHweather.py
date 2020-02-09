# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem

class MhweatherSpider(scrapy.Spider):
    name = 'MHweather'
    allowed_domains = ['tianqi.com']
    start_urls = []
    citys = ['nanjing', 'suzhou', 'minhang']

    for city in citys:
        start_urls.append('http://www.tianqi.com/' + city + '/')

    def parse(self, response):
        sevenday = response.xpath('//div[@class="day7"]')
        items = []
        for day in rane(1, 7):
            item = WeatherItem()
            item['date'] = sevenday.xpath('./ul[1]/li[' + str(day) + ']/b/text()').extract()
            item['week'] = sevenday.xpath('./ul[1]/li[' + str(day) + ']/span/text()').extract()
            item['weather_s'] = sevenday.xpath('./ul[2]/li[' + str(day) + ']/text()').extract()
            item['wind'] = sevenday.xpath('./ul[3]/li[' + str(day) + ']/text()').extract()
            item['tem_h'] = sevenday.xpath('./div/ul/li[' + str(day) + '/span/text()').extract()
            item['tem_l'] = sevenday.xpath('./div/ul/li[' + str(day) + '/b/text()').extract()
            items.append(item)
        return items
