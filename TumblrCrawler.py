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
import math
import LogUtil
import FileRemoveRepeat

logger = LogUtil.getLogger("tumblr")

queue = queue.Queue()

# 开启下载线程数
thread_count = 10


class ThreadTask(threading.Thread):
    def __init__(self, post_list):
        super(ThreadTask, self).__init__()
        self.post_list = post_list

    def run(self):
        for posturl in self.post_list:
            try:
                TumblrPostDownload.PostDownload(posturl)
            except:
                traceback.print_exc()
                print('Something wrong in post %s' % posturl)


def DownloadAllthepost(url):
    Task = []
    all_post_url = []
    DefaultStyle = PersonalThemeSearch.BlogStyleDetection(url)

    if DefaultStyle:
        PostUrlLists = ArchiveSearch.FindAllthePostUrl(url)
    else:
        PostUrlLists = ArchiveSearch.findalltheposturl(url)
    if PostUrlLists:
        PageNum = len(PostUrlLists)
        for pageNum in range(1, PageNum + 1):
            for posturl in PostUrlLists[pageNum]:
                all_post_url.append(posturl)
        n = int(math.ceil(len(all_post_url) / float(thread_count)))
        postList = [all_post_url[i:i + n] for i in range(0, len(all_post_url), n)]
        print('post分成了 %s 组，开启了 %s 线程' % (len(postList), len(postList)), postList)
        t_number = 0
        for post_list in postList:
            t_number = t_number + 1
            task = ThreadTask(post_list)
            Task.append(task)
            print('-' * 16, '\nThis is thread %s\n' % t_number, '-' * 16)
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


def addUser(username):
    """
    在下载队列中添加指定用户的关注账户
    :param url:
    :return:
    """
    new_users = ArchiveSearch.getFollower(username)
    for index, username in enumerate(new_users):
        print("关注用户共%s个 第%s 个为  %s" % (len(new_users), index + 1, username))
        queue.put(username)


def main():
    username = input('Input username: ')
    queue.put(username)
    start = time.time()
    addUser(username)
    reg = r'(http|https)://.*?'
    while not queue.empty():
        user = queue.get()
        URL = 'https://' + user + '.tumblr.com/'
        if re.match(reg, URL):
            try:
                discrimination = ArchiveSearch.Main_Post_URLDiscrimination(URL)
                if discrimination:
                    DownloadAllthepost(URL)
                else:
                    TumblrPostDownload.PostDownload(URL)
            except:
                traceback.print_exc()
        else:
            print('Input wrong format.')
        end = time.time()
        update_download_user_to_database(user)
        FileRemoveRepeat.dealFileAfterDownload()
    print(start, end, '=> Cost %ss' % (end - start))


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
