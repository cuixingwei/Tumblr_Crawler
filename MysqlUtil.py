# -*- coding: utf-8 -*-

"""
  Author:   xwcui
  Purpose:  mysql 工具
  Created:  2017-09-05
"""

import pymysql


# Connect to the database

def connect():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='tumblr')
    return conn


def excute(sql, data):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, data)
    print(cur.description)
    conn.commit()
    close(conn)
    cur.close()


def select(sql, data):
    # 设置游标类型，默认游标类型为元祖形式
    # 将游标类型设置为字典形式
    conn = connect()
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute(sql, data)
    result = cur.fetchall()
    cur.close()
    close(conn)
    return result


def close(conn):
    conn.close()


if __name__ == '__main__':
    n = 2
