#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2019-06-18 11:59:13
# Project: zhihu

from pyspider.libs.base_handler import *
import MySQLdb
import random


class Handler(BaseHandler):
    crawl_config = {
        'headers': {
            'User-Agent': 'GoogleBot',
            'Host': 'www.zhihu.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        }
    }

    def __init__(self):
        self.db = MySQLdb.connect('rm-wz9v6ey1y446me9055o.mysql.rds.aliyuncs.com', 'root', '@qwe123456', 'qa',
                                  charset='utf8')

    def add_question(self, title, content, content_count):
        try:
            cursor = self.db.cursor()
            sql = 'INSERT INTO `qa`.`tb_question`( `title`, `content`, `user_id`, `created_date`, `comment_count`, `is_del`) VALUES ("%s","%s",%d,%s,%d,%d)' % (
                title, content, 22, 'now()', content_count, 0)
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
            sql = 'insert into tb_comment(content, entity_type, entity_id, user_id, add_time) values ("%s",%d,%d, %d,%s)' % (comment, 0, qid, 22, 'now()')
            print(sql)
            cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://www.zhihu.com/topic/19551275/top-answers', callback=self.index_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="https://www.zhihu.com/question/"]').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False)

    @config(priority=2, age=1000 * 24 * 60 * 60)
    def detail_page(self, response):
        title = response.doc('h1.QuestionHeader-title').text()
        content = response.doc('div.QuestionHeader-detail>div.QuestionRichText.QuestionRichText--expandable>div>span').html()
        items = response.doc('div.RichText.ztext.CopyrightRichText-richText').items()
        print(content)
        if content is not None:
            content = content.replace('"', '\\"')
        qid = self.add_question(title, content, sum(1 for x in items))
        for each in response.doc('div.RichText.ztext.CopyrightRichText-richText').items():
            self.add_comment(each.html().replace('"', '\\"'), qid)
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }
