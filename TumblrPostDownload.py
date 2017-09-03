# -*- coding: utf-8 -*-
"""
  Author:  Sparrow
  Purpose: downloading one entire blog from Tumblr once.
  Created: 2017-1.1
"""
import re
import urllib.request
import Tumblrimage
import TumblrVideo
import traceback
from bs4 import BeautifulSoup
import TumblrCrawler
import threading

mutex = threading.Lock()


def getHtml(url):
    try:
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        return html
    except:
        # traceback.print_exc()
        print('The URL you requested could not be found In Module PostDownload')
        return 'Html'


def vedio_image_judge(url):
    html = getHtml(url)
    reg = r'<meta property="og:type" content="tumblr-feed:(.*?)" />'
    typere = re.compile(reg)
    type = re.findall(typere, html)
    if type:
        print('This is %s' % type[0])
        return type[0]
    else:
        return False


def findUser(url):
    html = getHtml(url)
    reg = r'<a class="reblog-link".*?</a>'
    userre = re.compile(reg)
    new_users = re.findall(userre, html)
    tmp_user = []
    for user in new_users:
        soup = BeautifulSoup(user)
        username = soup.a.text
        if username and username not in TumblrCrawler.total_user:
            TumblrCrawler.total_user.append(username)
            TumblrCrawler.queue.put(username)
            tmp_user.append(username)
            print('新用户 %s' % username)
    mutex.acquire()
    if tmp_user:
        TumblrCrawler.f_user.write('\n'.join(tmp_user) + '\n')
    mutex.release()


def PostDownload(url):
    findUser(url)

    Type = vedio_image_judge(url)

    if Type == 'video':
        TumblrVideo.getMP4(url)
    elif Type == 'photoset' or 'photo':
        Tumblrimage.getImg(url)
    else:
        print('There is nothing!')


if __name__ == '__main__':
    select = 'N'
    while not (select == 'Y'):
        # URL = input('Input url: ')
        URL = 'https://ndjhsnll.tumblr.com/post/149494233888'
        PostDownload(URL)
        select = input("Do you want to Quit? [Y/N]")
