#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2019-06-17 21:16:43
# Project: v2ex_test

from pyspider.libs.base_handler import *
import MySQLdb
import random


class Handler(BaseHandler):
    crawl_config = {
    }

    def __init__(self):
        self.db = MySQLdb.connect('rm-wz9v6ey1y446me9055o.mysql.rds.aliyuncs.com', 'root', '@qwe123456', 'qa',
                                  charset='utf8')

    def insert_value(self, title, content, count):
        try:
            cursor = self.db.cursor()
            sql = 'INSERT INTO `qa`.`tb_question`( `title`, `content`, `user_id`, `created_date`, `comment_count`, `is_del`) VALUES ("%s","%s",%d,%s,%d,%d)' % (
                title, content, random.randint(208, 342), 'now()', count, 0)
            cursor.execute(sql)
            qid = cursor.lastrowid
            self.db.commit()
            return qid
        except Exception as e:
            print(e)
            self.db.rollback()
        return 0

    def add_comment(self, comment, qid):
        try:
            cursor = self.db.cursor()
            sql = 'insert into tb_comment(content, entity_type, entity_id, user_id, add_time) values ("%s",%d,%d, %d,%s)' % (
            comment, 0, qid, random.randint(208, 342), 'now()')
            print(sql)
            cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://www.v2ex.com/', callback=self.index_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="https://www.v2ex.com/?tab="]').items():
            self.crawl(each.attr.href, callback=self.broad_page, validate_cert=False)

    @config(priority=2)
    def broad_page(self, response):
        for each in response.doc('a[href^="https://www.v2ex.com/go/"]').items():
            self.crawl(each.attr.href, callback=self.content_page, validate_cert=False)

    @config(priority=2)
    def content_page(self, response):
        for each in response.doc('a[href^="https://www.v2ex.com/t/"]').items():
            url = each.attr.href
            if url.find('#') > 0:
                url = url[0: url.find('#')]
            self.crawl(url, callback=self.detail_page, validate_cert=False)
        for each in response.doc('a[href^="https://www.v2ex.com/go/create"]').items():
            self.crawl(each.attr.href, callback=self.content_page, validate_cert=False)

    @config(priority=2, age=10 * 24 * 60 * 60)
    def detail_page(self, response):
        items = response.doc('div.reply_content').items()
        title = response.doc('h1').text()
        content = response.doc('div.topic_content').html()
        if content is not None:
            content = content.replace('"', '\\"')
        qid = self.insert_value(title, content, sum(1 for x in items))
        for each in response.doc('div.reply_content').items():
            self.add_comment(each.text().replace('"', '\\"'), qid)
        return {
            "url": response.url,
            "title": response.doc('h1').text(),
            "content": response.doc('div.topic_content').html().replace('"', '\\"')
        }
