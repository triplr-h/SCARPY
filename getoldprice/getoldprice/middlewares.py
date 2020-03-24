# encoding=utf-8
import random
from fake_useragent import UserAgent
import json


class UserAgentMiddleware(object):
    """ User-Agent """

    def process_request(self, request, spider):
        agent = UserAgent().random
        request.headers["User-Agent"] = agent
