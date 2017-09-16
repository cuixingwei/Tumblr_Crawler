# -*- coding: utf-8 -*-
"""
  Author:   xwcui
  Purpose:  remove repeat file(video,img)
  Created:  2017-9-3
"""

import os
import MysqlUtil
import FileUtil


def removeRepeat(dir):
    """
    删除指定目录中重复文件
    :param dir:
    :return:
    """
    oldf = FileUtil.filecount(dir)
    print('去重前有', oldf, '个文件\n\n\n请稍等正在为您删除重复文件...')
    delfile(dir)
    print('\n\n去重后剩', FileUtil.filecount(dir), '个文件')
    print('\n\n一共帮您删除了', oldf - FileUtil.filecount(dir), '个文件\n\n')


def calImgMD5ToDatabase():
    """
    计算指定目录中所有图片md5值，并写入数据库
    :return:
    """
    dir = 'E:\BaiduNetdiskDownload\TumblrDownload\img'
    filedir = os.walk(dir)
    for i in filedir:
        for tlie in i[2]:
            pathtlie = dir + '\\' + tlie
            if not judgeFileExistDb(pathtlie):
                sql = "insert into `source_md5` (`path`,`md5`,`type`) values (%s,%s,%s)"
                data = (pathtlie, FileUtil.md5sum(pathtlie), 'img')
                MysqlUtil.excute(sql, data)
            else:
                print("文件 %s md5已经计算出并存入数据库" % pathtlie)


def calVideoMD5ToDatabase():
    """
    计算指定目录中所有视频md5值，并写入数据库
    :return:
    """
    dir = 'E:\BaiduNetdiskDownload\TumblrDownload\\video'
    filedir = os.walk(dir)
    for i in filedir:
        for tlie in i[2]:
            pathtlie = dir + '\\' + tlie
            exist = judgeFileExistDb(pathtlie)
            if not exist:
                sql = "insert into `source_md5` (`path`,`md5`,`type`) values (%s,%s,%s)"
                data = (pathtlie, FileUtil.md5sum(pathtlie), 'video')
                MysqlUtil.excute(sql, data)
            else:
                print('数据库中已经存在文件: %s' % pathtlie)


def judgeFileExistDb(filepath):
    """
    判断指定文件信息数据中是否已存在
    :param filepath:
    :return:
    """
    sql = 'SELECT * from source_md5 where path = %s '
    data = (filepath)
    result = MysqlUtil.select(sql, data)
    if not result:
        return False
    else:
        return True



def delFileBySize(video_size, img_size):
    """
    读取数据库，删除指定大小的视频图片
    未下载完整
    位率小于500Kb/s
    :return:
    """
    sql = 'SELECT * from source_md5 where (type= %s and file_size < %s) OR (type= %s and file_size < %s) ' \
          'OR (type= %s and file_size < stream_size) OR (type= %s and overall_bit_rate < 500) '
    data = ('video', video_size, 'img', img_size, 'video', 'video')
    delfilecount = 0
    result = MysqlUtil.select(sql, data)
    for i, e in enumerate(result):
        delfilecount += 1
        print('第几个%d 文件 %s 文件大小为 %s Kb 流大小为 %s Kb 时长 %s S 删除' % (
            i, e['path'], e['file_size'], e['stream_size'], e['duration']))
        os.remove(e['path'])
        sql = 'delete from source_md5 where id= %s '
        data = (e['id'])
        MysqlUtil.excute(sql, data)
    print('删除的文件个数为 %s ' % (delfilecount))


def delfile(dir):
    """
    删除指定目录中重复文件，md5直接计算
    :param dir:
    :return:
    """
    all_md5 = {}
    filedir = os.walk(dir)
    for i in filedir:
        count = 0
        for tlie in i[2]:
            count += 1
            pathtlie = dir + '\\' + tlie
            if FileUtil.md5sum(pathtlie) in all_md5.values():
                print('第几个%d 文件 %s  删除' % (count, pathtlie))
                os.remove(pathtlie)
            else:
                print('第几个%d 文件 %s  不重复' % (count, pathtlie))
                all_md5[tlie] = FileUtil.md5sum(pathtlie)


def delRepeatFileByDB():
    """
    删除重复文件，文件md5值记录在数据库中
    :return:
    """
    sql = 'SELECT * from source_md5 '
    data = ()
    all_md5 = {}
    total = 0
    delfilecount = 0
    result = MysqlUtil.select(sql, data)
    for i, e in enumerate(result):
        total += 1
        if e['md5'] in all_md5.values():
            delfilecount += 1
            print('第几个%d 文件 %s  删除' % (i, e['path']))
            os.remove(e['path'])
            sql = 'delete from source_md5 where id= %s '
            data = (e['id'])
            MysqlUtil.excute(sql, data)
        else:
            print('第几个%d 文件 %s  不重复' % (i, e['path']))
            all_md5[e['path']] = e['md5']
    print('共 %s 个文件，删除重复的文件 %s ' % (total, delfilecount))


def delRepeatFileByName():
    sql = 'SELECT * from download_url  '
    data = ()
    all_name = []
    total = 0
    delfilecount = 0
    result = MysqlUtil.select(sql, data)
    for i, e in enumerate(result):
        total += 1
        if e['filename'] in all_name:
            delfilecount += 1
            print('第几个%d 文件 %s %s  删除' % (i, e['filename'], e["url"]))
            sql = 'delete from download_url where id= %s '
            data = (e['id'])
            MysqlUtil.excute(sql, data)
        else:
            print('第几个%d 文件 %s %s 不重复' % (i, e['filename'], e["url"]))
            all_name.append(e['filename'])
    print('共 %s 个文件，删除重复的文件 %s ' % (total, delfilecount))


def dealFileAfterDownload():
    """
    下载完一个用户后
    处理文件 计算md5 删除重复URL 删除重复文件
    计算video信息存入数据库
    删除小于指定大小的图片和视频
    :return:
    """
    delRepeatFileByName()  # 删除下载链接中文件名重复项
    calImgMD5ToDatabase()  # 计算图片md5，并存入数据库
    calVideoMD5ToDatabase()  # 计算视频md5，并存入数据库
    delRepeatFileByDB()  # 根据MD5删除重复文件
    delFileBySize(10 * 1024, 300)  # 删除视频小于10M 图片大小300Kb的图片 删除未下载完整的视频


if __name__ == '__main__':
    dealFileAfterDownload()
