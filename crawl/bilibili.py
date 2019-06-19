#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2019-06-18 20:21:37
# Project: bilibili

from pyspider.libs.base_handler import *
import random


class Handler(BaseHandler):
    crawl_config = {
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'http://space.bilibili.com/45388',
            'Origin': 'http://space.bilibili.com',
            'Host': 'space.bilibili.com',
            'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
        }
    }

    @every(minutes=24 * 60)
    def on_start(self):
        for i in range(1, 100):
            self.crawl('https://space.bilibili.com/27264' + str(i * 7), callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        payload = {
            '_': datetime_to_timestamp_in_milliseconds(datetime.datetime.now()),
            'mid': url.replace('https://space.bilibili.com/', '')
        }
        ua = random.choice(uas)
        head = {
            'User-Agent': ua,
            'Referer': 'https://space.bilibili.com/' + str(i) + '?from=search&seid=' + str(random.randint(10000, 50000))
        }
        jscontent = requests \
            .session() \
            .post('http://space.bilibili.com/ajax/member/GetInfo',
                  headers=head,
                  data=payload,
                  proxies=proxies) \
            .text
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }
