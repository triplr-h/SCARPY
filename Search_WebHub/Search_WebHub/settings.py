# -*- coding: utf-8 -*-

# Scrapy settings for pornhub project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Search_WebHub'

SPIDER_MODULES = ['Search_WebHub.spiders']
NEWSPIDER_MODULE = 'Search_WebHub.spiders'

DOWNLOAD_DELAY = 1  # 间隔时间
LOG_LEVEL = 'WARNING'  # 日志级别
CONCURRENT_REQUESTS = 20  # 默认为16
# CONCURRENT_ITEMS = 1
# CONCURRENT_REQUESTS_PER_IP = 1
REDIRECT_ENABLED = False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pornhub (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DOWNLOADER_MIDDLEWARES = {
    "Search_WebHub.middlewares.UserAgentMiddleware": 401,
    "Search_WebHub.middlewares.CookiesMiddleware": 402,
}
ITEM_PIPELINES = {
    "Search_WebHub.pipelines.PornhubMongoDBPipeline": 403,
}

# FEED_URI = u'G:\Git_code\Search_WebHubBot\data\pornhub.csv'
# FEED_FORMAT='CSV'

DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

CLOSESPIDER_ITEMCOUNT = 5
# CLOSESPIDER_TIMEOUT = 30
