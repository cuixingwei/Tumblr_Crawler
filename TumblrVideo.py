# -*- coding: utf-8 -*-
"""
  Author:  Sparrow
  Purpose: downloading one entire blog from Tumblr once.
  Created: 2017-1.1
"""
import multiprocessing
import re
import urllib.request
import os
import traceback

def getHtml(url):
    try:
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        return html
    except:
        # traceback.print_exc()
        print('The URL you requested could not be found in Module Video')
        return 'Html'

def getPostname(posturl):
	reg = r'https*://.*?\/post\/(.*)'
	postname = re.compile(reg)
	postnamelist = re.findall(postname, posturl)
	print(postnamelist)
	if postnamelist:
		return postnamelist[0]
	else:
		postnamelist = ['page1']
		return postnamelist[0]

def getMP4(url):
    html = getHtml(url)
    reg = r'<iframe src=\'(https\://www\.tumblr\.com/video/.*?)\''
    videopagere = re.compile(reg)
    videopageurl = re.findall(videopagere, html)
    if videopageurl:
        print(videopageurl[0])

        videohtml = getHtml(videopageurl[0])
        reg_url = r'<source src="(https://.*?.tumblr.com/video_file/t:.*?)" type="video/mp4">'
        videore = re.compile(reg_url)
        videourlList = re.findall(videore, videohtml)
        print("videourl %s " % videourlList)
        videourl = re.findall(videore, videohtml)[0]

        Postname = getPostname(url)
        if len(Postname) > 12:
            Name = Postname[:12]
        else:
            Name = Postname

        path = 'TumblrDownload/video'
        if not os.path.exists(path):
            os.makedirs(path)
        target = path + '%s.mp4' % Name

        print("Downloading %s " % target)
        try:
            urllib.request.urlretrieve(videourl, target)
        except:
            # traceback.print_exc()
            print('The video is deleted or not found.')
        return True

    else:
        print('There is no Video!')
        return False


if __name__ == '__main__':
    select = 'Y'
    while (select == 'Y'):
        URL = input('Input url: ')
        getMP4(URL)
        select = input("Do you want to Continue? [Y/N]")
