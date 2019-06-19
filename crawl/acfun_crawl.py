#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2019-06-18 20:21:37
# Project: bilibili

from pyspider.libs.base_handler import *
import MySQLdb


class Handler(BaseHandler):
    crawl_config = {
        'headers': {

        }
    }

    def __init__(self):
        self.db = MySQLdb.connect('rm-wz9v6ey1y446me9055o.mysql.rds.aliyuncs.com', 'root', '@qwe123456', 'qa',
                                  charset='utf8')

    def add_user(self, name, head_url):
        try:
            cursor = self.db.cursor()
            sql = 'INSERT INTO `qa`.`tb_user`(`name`, `password`, `salt`, `head_url`, `auth`) VALUES ("' + name + '","AFC","DFC","' + head_url + '",0)'
            print(sql)
            cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
        return 0

    @every(minutes=24 * 60)
    def on_start(self):
        for i in range(100, 10000, 2):
            self.crawl('https://www.acfun.cn/u/14266' + str(i) + '.aspx', callback=self.detail_page,
                       validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):
        name = response.doc('div.clearfix>div.name.fl.text-overflow').text()
        print(name)
        src = response.doc('div.cover>div.img').attr('style')
        head_url = src.replace('background:url(\'', '').replace('\') 0% 0% / 100% no-repeat', '')
        print(head_url)
        if name is not None and name.find('ACer_')< 0:
            self.add_user(name, head_url)
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }
