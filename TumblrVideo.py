# -*- coding: utf-8 -*-
"""
  Author:  Sparrow
  Purpose: downloading one entire blog from Tumblr once.
  Created: 2017-1.1
"""
import re
import RemoteUtil
import ArchiveSearch


def getVideoUrlList(url):
    html = ArchiveSearch.getHtml(url)
    reg = r'<iframe src=\'(https\://www\.tumblr\.com/video/.*?)\''
    videopagere = re.compile(reg)
    videopageurlList = re.findall(videopagere, html)
    if videopageurlList:
        videopageurl = videopageurlList[0]
        videohtml = ArchiveSearch.getHtml(videopageurl)
        reg_url = r'<source src="(https://.*?.tumblr.com/video_file/t:.*?)" type="video/mp4">'
        videore = re.compile(reg_url)
        videourllist_none = re.findall(videore, videohtml)
        videourllist = list(set(videourllist_none))
        return videourllist
    else:
        return False


def getMP4(url):
    videourllist = getVideoUrlList(url)
    if videourllist:
        for videourl in videourllist:
            print("videourl %s " % videourl)
            RemoteUtil.judgeDown(videourl)
    else:
        print('There is no Video!')


if __name__ == '__main__':
    select = 'Y'
    while (select == 'Y'):
        URL = input('Input url: ')
        getMP4(URL)
        select = input("Do you want to Continue? [Y/N]")
