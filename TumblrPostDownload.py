# -*- coding: utf-8 -*-
"""
  Author:  Sparrow
  Purpose: downloading one entire blog from Tumblr once.
  Created: 2017-1.1
"""
import re
import Tumblrimage
import TumblrVideo
import MysqlUtil
import ArchiveSearch
import LogUtil

logger = LogUtil.getLogger("tumblr")


def vedio_image_judge(url):
    html = ArchiveSearch.getHtml(url)
    reg = r'<meta property="og:type" content="tumblr-feed:(.*?)" />'
    typere = re.compile(reg)
    type = re.findall(typere, html)
    if type:
        logger.debug('This is %s' % type[0])
        return type[0]
    else:
        return False


def judgeUserExist(username):
    """
    判断数据中用户列表中是否已存在该用户
    :param username:
    :return:
    """
    sql = "select * from tumblr_username where username = %s "
    data = (username)
    result = MysqlUtil.select(sql, data)
    if result:
        return True
    else:
        return False


def insertUserToDB(username):
    """
    数据用户表添加新用户
    :param username:
    :return:
    """
    sql = "insert into tumblr_username (username) VALUE (%s) "
    data = (username)
    MysqlUtil.excute(sql, data)


def updateUserToDB(username):
    """
    用户下载次数加1
    :param username:
    :return:
    """
    sql = "update tumblr_username set count=count+1 WHERE username = (%s) "
    data = (username)
    MysqlUtil.excute(sql, data)


def PostDownload(url):
    Type = vedio_image_judge(url)
    if Type == 'video':
        TumblrVideo.getMP4(url)
    elif (Type == 'photoset') or (Type == 'photo'):
        print("不下图片")
        # Tumblrimage.getImg(url)
    else:
        print('There is nothing!')


if __name__ == '__main__':
    URL = r'https://shoottttttt.tumblr.com/post/162499930155'
    PostDownload(URL)
