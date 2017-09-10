# -*- coding: utf-8 -*-
"""
  Author:   xwcui
  Purpose:  文件操作工具类
  Created:  2017-9-8
"""

import os
import hashlib
import math
import sys
from pprint import pprint

from pymediainfo import MediaInfo


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


def print_frame(text):
    print("+-{}-+".format("-" * len(text)))
    print("| {} |".format(text))
    print("+-{}-+".format("-" * len(text)))


def process(fname):
    media_info = MediaInfo.parse(fname)
    for track in media_info.tracks:
        print_frame(track.track_type)
        pprint(track.to_data())
    print()
    for track in media_info.tracks:
        if track.track_type == 'General' and track.duration:
            print("Duration: {} sec.".format(track.duration / 1000.0))


def getMediaInfo(fname):
    videoinfo = {}
    media_info = MediaInfo.parse(fname)
    for track in media_info.tracks:
        if track.track_type == 'General':
            videoinfo['duration'] = math.ceil(track.duration / 1000)
            videoinfo['file_size'] = math.ceil(track.file_size / 1024)
            videoinfo['complete_name'] = track.complete_name
        elif track.track_type == 'Video':
            videoinfo['stream_size'] = math.ceil(track.stream_size / 1024)
            videoinfo['frame_rate'] = track.frame_rate
            videoinfo['height'] = track.height
            videoinfo['width'] = track.width
    return videoinfo


escape_dict = {'\a': r'\a',
               '\b': r'\b',
               '\c': r'\c',
               '\f': r'\f',
               '\n': r'\n',
               '\r': r'\r',
               '\t': r'\t',
               '\v': r'\v',
               '\'': r'\'',
               '\"': r'\"',
               '\0': r'\0',
               '\1': r'\1',
               '\2': r'\2',
               '\3': r'\3',
               '\4': r'\4',
               '\5': r'\5',
               '\6': r'\6',
               '\7': r'\7',
               '\8': r'\8',
               '\9': r'\9'}


def raw(text):
    new_string = ''
    for char in text:
        try:
            new_string += escape_dict[char]
        except KeyError:
            new_string += char
    return new_string
if __name__ == '__main__':
    localurl = r'F:\BaiduNetdiskDownload\TumblrDownload\video\162711259557.mp4'
    process(localurl)
