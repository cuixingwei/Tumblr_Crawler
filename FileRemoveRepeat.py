# -*- coding: utf-8 -*-
"""
  Author:   xwcui
  Purpose:  remove repeat file(video,img)
  Created:  2017-9-3
"""

import os, hashlib


def filecount(dir):
    # d当前目录
    curdir = os.popen('echo %cd%').read()
    cmd = 'dir ' + dir + ' /B |find /V /C ""'
    print("cmd %s" % cmd)
    filecount = int(os.popen(cmd).read())
    return (filecount)


def md5sum(filename):
    f = open(filename, 'rb')
    md5 = hashlib.md5()
    while True:
        fb = f.read(8096)
        if not fb:
            break
        md5.update(fb)
    f.close()
    return (md5.hexdigest())


def delfile(dir):
    all_md5 = {}
    filedir = os.walk(dir)
    for i in filedir:
        count = 0
        for tlie in i[2]:
            count += 1
            pathtlie = dir + '\\' + tlie
            if md5sum(pathtlie) in all_md5.values():
                print('第几个%d 文件 %s  删除' % (count, pathtlie))
                os.remove(pathtlie)
            else:
                print('第几个%d 文件 %s  不重复' % (count, pathtlie))
                all_md5[tlie] = md5sum(pathtlie)


def removeRepeat(dir):
    oldf = filecount(dir)
    print('去重前有', oldf, '个文件\n\n\n请稍等正在为您删除重复文件...')
    delfile(dir)
    print('\n\n去重后剩', filecount(dir), '个文件')
    print('\n\n一共帮您删除了', oldf - filecount(dir), '个文件\n\n')


if __name__ == '__main__':
    dir = input('请输入文件目录:')
    print('输入路径为 %s' % dir)
    oldf = filecount(dir)
    print('去重前有', oldf, '个文件\n\n\n请稍等正在为您删除重复文件...')
    delfile(dir)
    print('\n\n去重后剩', filecount(dir), '个文件')
    print('\n\n一共帮您删除了', oldf - filecount(dir), '个文件\n\n')
