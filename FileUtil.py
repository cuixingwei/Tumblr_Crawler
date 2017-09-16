# -*- coding: utf-8 -*-
"""
  Author:   xwcui
  Purpose:  文件操作工具类
  Created:  2017-9-8
"""

import os
import hashlib
import math


def judgeFileExistByName(fileName):
    """
    根据文件名称判断是否已下载
    :param fileName:
    :return:
    """
    sql = 'SELECT * from download_url where filename = %s '
    data = (fileName)
    result = MysqlUtil.select(sql, data)
    if not result:
        return False
    else:
        return True


def filecount(dir):
    """
    返回目录中文件数 dir 为目录绝对路径
    :param dir:
    :return:
    """
    cmd = 'dir ' + dir + ' /B |find /V /C ""'
    print("cmd %s" % cmd)
    filecount = int(os.popen(cmd).read())
    return (filecount)


def md5sum(filename):
    """
    计算文件md5值  filename 为文件完成路径
    :param filename:
    :return:
    """
    md5 = hashlib.md5()
    fb = open(filename, 'rb')
    md5.update(fb.read())
    fb.close()
    return (md5.hexdigest())


def getFileSize(fpath):
    """
    返回文件的大小，单位为 Kb
    :param fpath:
    :return:
    """
    fsize = os.path.getsize(fpath)
    return math.ceil(fsize / 1024)


def fileExist(fpath):
    """
    判断文件是否存在
    :param fpath:
    :return:
    """
    return os.path.isfile(fpath)


if __name__ == '__main__':
    print('d')
