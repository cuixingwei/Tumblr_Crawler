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


def vedio_image_judge(url):
    html = ArchiveSearch.getHtml(url)
    reg = r'<meta property="og:type" content="tumblr-feed:(.*?)" />'
    typere = re.compile(reg)
    type = re.findall(typere, html)
    if type:
        print('This is %s' % type[0])
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


def FindUser(url):
    """
    发现post页面的新用户
    :param url:
    :return:
    """
    html = ArchiveSearch.getHtml(url)
    reg = r'<a class="reblog-link" .*? data-blog-card-username="(.*?)">'
    userre = re.compile(reg)
    new_users = re.findall(userre, html)
    if new_users:
        new_users = list(set(new_users))
    tmp_user = []
    for username in new_users:
        tmp_user.append(username)
    return tmp_user


def PostDownload(url):
    Type = vedio_image_judge(url)

    if Type == 'video':
        TumblrVideo.getMP4(url)
    elif (Type == 'photoset') or (Type == 'photo'):
        Tumblrimage.getImg(url)
    else:
        print('There is nothing!')


def getAllUrl(url):
    """
    根据POST URL返回所有文件URL
    :param url:
    :return:
    """
    Type = vedio_image_judge(url)
    if Type == 'video':
        tempUrl = TumblrVideo.getVideoUrlList(url)
    elif (Type == 'photoset') or (Type == 'photo'):
        tempUrl = Tumblrimage.getImageUrlList(url)
    else:
        return False
    return tempUrl


if __name__ == '__main__':
    select = 'N'
    while not (select == 'Y'):
        URL = input('Input url: ')
        # URL = 'https://24k-k42.tumblr.com/post/151463716357/ktv系列4'
        PostDownload(URL)
        select = input("Do you want to Quit? [Y/N]")
