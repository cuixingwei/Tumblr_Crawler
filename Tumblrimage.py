# -*- coding: utf-8 -*-
"""
  Author:  Sparrow
  Purpose: downloading one entire blog from Tumblr once.
  Created: 2017-1.1
"""
import re
import RemoteUtil
import ArchiveSearch


def getImageUrlList(url):
    """
    返回POST URL中的所有图片URL
    :param url:
    :return:
    """
    html = ArchiveSearch.getHtml(url)
    reg = r'<meta property="og:image" content="(https*://68.media.tumblr.com/.*?\.(jpg|gif|png))" />'
    imgre = re.compile(reg)
    imglist_none = re.findall(imgre, html)
    imglist = list(set(imglist_none))
    if imglist:
        imgurl_list = []
        for imgurls in imglist:
            imgurl_list.append(imgurls[0])
        return imgurl_list
    else:
        return False


def getImg(url):
    imgurl_list = getImageUrlList(url)
    if imgurl_list:
        for imgurl in imgurl_list:
            RemoteUtil.judgeDown(imgurl)
    else:
        print('There is no image!')


if __name__ == '__main__':

    select = 'Y'
    while (select == 'Y'):
        URL = input('Input url: ')
        getImg(URL)
        select = input("Do you want to Continue? [Y/N]")
