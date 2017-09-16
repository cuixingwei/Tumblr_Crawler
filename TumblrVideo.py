# -*- coding: utf-8 -*-
"""
  Author:  Sparrow
  Purpose: downloading one entire blog from Tumblr once.
  Created: 2017-1.1
"""
import re
import RemoteUtil
import ArchiveSearch
import LogUtil

logger = LogUtil.getLogger("tumblr")


def getVideoUrlList(url):
    html = ArchiveSearch.getHtml(url)
    reg = r'<iframe src=\'(https\://www\.tumblr\.com/video/.*?)\''
    videopagere = re.compile(reg)
    videopageurlList = re.findall(videopagere, html)
    videourllist = []
    if videopageurlList:
        for videopageurl in videopageurlList:
            videohtml = ArchiveSearch.getHtml(videopageurl)
            reg_url = r'<source src="(https://.*?.tumblr.com/video_file/t:.*?)" type="video/mp4">'
            videore = re.compile(reg_url)
            videourllist_none = re.findall(videore, videohtml)
            temp_list = list(set(videourllist_none))
            if temp_list:
                videourllist.append(temp_list[0])
        return list(set(videourllist))
    else:
        return False


def getMP4(url):
    videourllist = getVideoUrlList(url)
    if videourllist:
        for videourl in videourllist:
            RemoteUtil.judgeDown(videourl)
    else:
        print('There is no Video!')


if __name__ == '__main__':
    posturl = r'https://shoottttttt.tumblr.com/post/161853926560'
    getVideoUrlList(posturl)
