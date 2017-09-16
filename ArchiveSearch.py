# -*- coding: utf-8 -*-
"""
  Author:  Sparrow
  Purpose: downloading one entire blog from Tumblr once.
  Created: 2017-1.1
"""

import re
import urllib.request
from urllib.parse import quote
import string
import traceback


def getHtml(url):
    try:
        url = quote(url, safe=string.printable)
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        return html
    except:
        traceback.print_exc()
        print('The URL you requested could not be found %s ' % url)
        return 'Html'


def ArchivePostfix(url):
    URL = url + 'archive'
    return URL


def findNextpage(ArchiveURL, url, PageList, PageNum):
    html = getHtml(url)
    reg = r'<a id="next_page_link" href="/archive(\?before_time=.*?)"'
    regc = re.compile(reg)
    nextpage = re.findall(regc, html)

    if nextpage:
        nextpageUrl = ArchiveURL + nextpage[0]
        PageNum += 1
        PageList[PageNum] = nextpageUrl
        print('Page %s' % PageNum, nextpageUrl)
        findNextpage(ArchiveURL, nextpageUrl, PageList, PageNum)


def findAllPage(url):
    archiveURL = ArchivePostfix(url)
    PageList = {1: archiveURL}
    PageNum = 1
    findNextpage(archiveURL, archiveURL, PageList, PageNum)
    return PageList


def FindPage(Homeurl):
    html = getHtml(Homeurl)
    PageList = {1: Homeurl}
    reg = r'<a href=".*?" class="next" data-current-page=".*?" data-total-pages="(.*?)">'
    total_pagere = re.compile(reg)
    total_page = re.findall(total_pagere, html)

    if total_page:
        PageNum = int(total_page[0])
        for i in range(2, PageNum + 1):
            PageList[i] = Homeurl + 'page/%s' % i
            print(i, PageList[i])
            i += 1
        print(PageList)
        return PageList
    else:
        print('There is only one page.')
        return PageList


def FindAllthePostUrl(url):
    PageList = FindPage(url)

    if PageList:
        Pagenum = len(PageList)
        PostUrlLists = {}
        for page in range(1, Pagenum + 1):
            Posturl = FindCurrentPagePostUrl(PageList[page])
            if Posturl:
                PostUrlLists[page] = Posturl
                print(page, PostUrlLists[page], sep=' ')
            else:
                print("There is no post in page %s!" % page)

        print(PostUrlLists, 'mark')
        return PostUrlLists

    else:
        print('There is no page!')
        return False


def reCodeURL(url):
    reg = '(.*?/post/.*)/.*'
    urlre = re.compile(reg)
    try:
        url_safe = quote(url, safe=string.printable)
        newnurlList = re.findall(urlre, url_safe)
        newurl = newnurlList[0]
        print(url, '=>', newurl)
        return newurl
    except:
        print(url, '=>')
        return url


def Main_Post_URLDiscrimination(url):
    post_reg = r'(.*?/post/.*?/*.*)'
    post_re = re.compile(post_reg)
    post_discrimination = re.findall(post_re, url)
    if post_discrimination:
        print('A Post page!')
        return False
    else:
        print('This is Main page!')
        return True


def FindCurrentPagePostUrl(url):
    html = getHtml(url)
    reg = r'<a target="_blank" class="hover" title="" href="(.*?)"'
    PostUrlre = re.compile(reg)
    PostUrlString = re.findall(PostUrlre, html)

    if PostUrlString:
        PostUrl = []
        for url in PostUrlString:
            Url = reCodeURL(url)
            PostUrl.append(Url)
        print(PostUrl)
        return PostUrl
    else:
        return False


def findalltheposturl(url):
    PageList = findAllPage(url)
    print(PageList)
    if PageList:
        Pagenum = len(PageList)
        PostUrlLists = {}
        for page in range(1, Pagenum + 1):
            Posturl = FindCurrentPagePostUrl(PageList[page])
            if Posturl:
                PostUrlLists[page] = Posturl
                print(page, PostUrlLists[page], sep=' ')
            else:
                print("There is no post in page %s!" % page)

        print(PostUrlLists, 'mark')
        return PostUrlLists
    else:
        print('There is no page!')
        return False


def getFollower(user):
    url = 'https://' + user + '.tumblr.com/following'
    html = getHtml(url)
    reg = r'<a href=".*?" class=".*?" data-current-page=".*?" data-total-pages="(.*?)">'
    pagere = re.compile(reg)
    pages = re.findall(pagere, html)
    follower_list = []
    if pages:
        pageNum = int(pages[0])
    try:
        for num in range(1, pageNum + 1):
            pageUrl = url + '/page/' + str(num)
            html = getHtml(pageUrl)
            reg = r'<span class="name">(.*?)</span>'
            fore = re.compile(reg)
            followers = re.findall(fore, html)
            if followers:
                for follower in followers:
                    if follower not in follower_list:
                        follower_list.append(follower)
    except:
        traceback.print_exc()
    return follower_list


if __name__ == '__main__':
    user = r'xwcui'
    getFollower(user)
