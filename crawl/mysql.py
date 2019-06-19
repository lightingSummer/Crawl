# -*- coding: utf-8 -*-
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect('rm-wz9v6ey1y446me9055o.mysql.rds.aliyuncs.com', 'root', '@qwe123456', 'qa', charset='utf8')
    try:
        cursor = db.cursor()
        '''
        sql = 'INSERT INTO `qa`.`tb_question`( `title`, `content`, `user_id`, `created_date`, `comment_count`, `is_del`) VALUES ("%s","%s",%d,%s,%d,%d)' % (
            "为什么我王者荣耀上不了王者呢", "为什么我王者荣耀上不了王者呢", 22, 'now()', 0, 0)
        cursor.execute(sql)
        qid = cursor.lastrowid
        db.commit()
        print(qid)
        '''
        sql = 'SELECT * FROM tb_question ORDER BY id DESC'
        cursor.execute(sql)
        for each in cursor.fetchall():
            for item in each:
                print(item)
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        db.close()
