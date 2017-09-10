# -*- coding: utf-8 -*-
"""
  Author:  Sparrow
  Purpose: downloading one entire blog from Tumblr once.
  Created: 2017-1.1
"""

import re
import threading
import TumblrPostDownload
import time
import traceback
import PersonalThemeSearch
import ArchiveSearch
import queue
import RemoteUtil
import math

queue = queue.Queue()
total_user = []

# 开启下载线程数
thread_count = 10

# 爬取模式 1获取所有下载地址后批量下载 2按照用户网站页数开启相应线程
down_mode = 1


class ThreadTask(threading.Thread):
    def __init__(self, PostUrlList):
        super(ThreadTask, self).__init__()
        self.postUrllist = PostUrlList

    def run(self):
        for posturl in self.postUrllist:
            try:
                print('posturl: ', posturl)
                addUser(posturl)
                TumblrPostDownload.PostDownload(posturl)
            except:
                traceback.print_exc()
                print('Something wrong in post %s' % posturl)


class ThreadDownTask(threading.Thread):
    def __init__(self, UrlList):
        super(ThreadDownTask, self).__init__()
        self.UrlList = UrlList

    def run(self):
        for url in self.UrlList:
            try:
                RemoteUtil.judgeDown(url)
            except:
                traceback.print_exc()
                print('Something wrong in download %s' % url)


def getAllUrl(url):
    """
    获取给定网址中的所有文件URL
    :param url:
    :return:
    """
    DefaultStyle = PersonalThemeSearch.BlogStyleDetection(url)
    AllUrl = []
    if DefaultStyle:
        PostUrlLists = ArchiveSearch.FindAllthePostUrl(url)
    else:
        PostUrlLists = ArchiveSearch.findalltheposturl(url)
    if PostUrlLists:
        PageNum = len(PostUrlLists)
        for pageNum in range(1, PageNum + 1):
            pageUrlList = PostUrlLists[pageNum]
            tempurl = []
            for posturl in pageUrlList:
                try:
                    print('posturl: ', posturl)
                    tempurl = TumblrPostDownload.getAllUrl(posturl)
                    addUser(posturl)
                except:
                    traceback.print_exc()
                if tempurl:
                    for url in tempurl:
                        AllUrl.append(url)
    return AllUrl


def DownloadAllUrl(URL):
    """
    下载给定所有文件链接，开启多线程下载
    :param AllUrl:
    :return:
    """
    Task = []
    AllUrl = getAllUrl(URL)
    print('此次共下载文件 %s 所有URL:' % len(AllUrl), AllUrl)
    n = int(math.ceil(len(AllUrl) / float(thread_count)))
    downList = [AllUrl[i:i + n] for i in range(0, len(AllUrl), n)]
    i = 0
    for l_d in downList:
        i += 1
        task = ThreadDownTask(l_d)
        Task.append(task)
        print('-' * 16, '\nThis is thread %s\n' % i, '-' * 16)
    for task in Task:
        task.setDaemon(True)
        task.start()
        print(time.ctime(), 'thread %s start' % task)
    for task in Task:
        task.join()
    while 1:
        for task in Task:
            if task.is_alive():
                continue
            else:
                Task.remove(task)
                print(time.ctime(), 'thread %s is finished' % task)
        if len(Task) == 0:
            break


def DownloadAllthepost(url):
    Task = []
    DefaultStyle = PersonalThemeSearch.BlogStyleDetection(url)

    if DefaultStyle:
        PostUrlLists = ArchiveSearch.FindAllthePostUrl(url)
    else:
        PostUrlLists = ArchiveSearch.findalltheposturl(url)

    if PostUrlLists:
        PageNum = len(PostUrlLists)
        for pageNum in range(1, PageNum + 1):
            task = ThreadTask(PostUrlLists[pageNum])
            Task.append(task)
            print('-' * 16, '\nThis is thread %s\n' % pageNum, '-' * 16)

        for task in Task:
            task.setDaemon(True)
            task.start()
            print(time.ctime(), 'thread %s start' % task)
        for task in Task:
            task.join()
        while 1:
            for task in Task:
                if task.is_alive():
                    continue
                else:
                    Task.remove(task)
                    print(time.ctime(), 'thread %s is finished' % task)
            if len(Task) == 0:
                break


def addUser(url):
    """
    在下载队列中添加新用户
    :param url:
    :return:
    """
    new_users = TumblrPostDownload.FindUser(url)
    for username in new_users:
        global total_user
        if username and username not in total_user:
            total_user.append(username)
            print('新用户 %s' % username)
            global queue
            queue.put(username)


def main():
    username = input('Input username: ')
    global queue
    queue.put(username)
    select = 'N'
    reg = r'(http|https)://.*?'
    while not (select == 'Y'):
        start = time.time()
        while not queue.empty():
            user = queue.get()
            URL = 'https://' + user + '.tumblr.com/'
            if re.match(reg, URL):
                try:
                    discrimination = ArchiveSearch.Main_Post_URLDiscrimination(URL)
                    if discrimination:
                        if down_mode == 1:
                            DownloadAllUrl(URL)
                        elif down_mode == 2:
                            DownloadAllthepost(URL)
                        else:
                            print("错误下载模式 %s" % down_mode)
                    else:
                        print('posturl: ', URL)
                        addUser(URL)
                        TumblrPostDownload.PostDownload(URL)
                except:
                    traceback.print_exc()
            else:
                print('Input wrong format.')
            end = time.time()
            update_download_user_to_database(user)
            print(start, end, '=> Cost %ss' % (end - start))
        select = input("Do you want to Quit? [Y/N]")


def update_download_user_to_database(user):
    """
    下载完的用户写入数据表
    :param user:
    :return:
    """
    if not TumblrPostDownload.judgeUserExist(user):
        TumblrPostDownload.insertUserToDB(user)
    else:
        TumblrPostDownload.updateUserToDB(user)


if __name__ == '__main__':
    main()
