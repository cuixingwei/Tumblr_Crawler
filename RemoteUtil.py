# -*- coding: utf-8 -*-

"""
  Author:   xwcui
  Purpose:  远程下载 工具
  Created:  2017-09-09
"""

import urllib.request
import math
import MysqlUtil
from urllib.parse import quote
import string
import re
import os
import traceback
import LogUtil
import FileRemoveRepeat

logger = LogUtil.getLogger("tumblr")

# 图片下载大小阈值  300Kb
imagedownsize = 1024 * 300

# 视频下载大小阈值 10Mb
videodownsize = 1024 * 1024 * 10

img_path = r'E:/BaiduNetdiskDownload/TumblrDownload/img/'
video_path = r'E:/BaiduNetdiskDownload/TumblrDownload/video/'


def getHeaders(url):
    """
    根据URL 获取headers
    :param url:
    :return:
    """
    headers = {}
    url = quote(url, safe=string.printable)
    try:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')]
        urllib.request.install_opener(opener)
        response = urllib.request.urlopen(url)
        headers['ContentLength'] = response.getheader('Content-Length')
        headers['ContentType'] = response.getheader('Content-Type')
        headers['Date'] = response.getheader('Date')
        headers['Server'] = response.getheader('Server')
        headers['LastModified'] = response.getheader('Last-Modified')
        headers['Etag'] = response.getheader('Etag')
        headers['TimingAllowOrigin'] = response.getheader('Timing-Allow-Origin')
        headers['AccessControlAllowOrigin'] = response.getheader('Access-Control-Allow-Origin')
        headers['AccessControlAllowMethods'] = response.getheader('Access-Control-Allow-Methods')
        headers['AccessControlMaxAge'] = response.getheader('Access-Control-Max-Age')
        headers['CacheControl'] = response.getheader('Cache-Control')
        headers['Age'] = response.getheader('Age')
        headers['Via'] = response.getheader('Via')
    except:
        traceback.print_exc()
        print("封装headers出错 url %s" % url)
    return headers


def judgeFileType(headers):
    """
    根据URL判断文件类型
    :param url:
    :return:
    """
    Image = {'jpg': 'image/jpeg', 'png': 'image/png', 'gif': 'image/gif', 'webp': 'image/webp',
             'cr2': 'image/x-canon-cr2', 'tif': 'image/tiff', 'bmp': 'image/bmp', 'jxr': 'image/vnd.ms-photo',
             'psd': 'image/vnd.adobe.photoshop', 'ico': 'image/x-icon'}
    Video = {'mp4 ': 'video/mp4', 'm4v': 'video/x-m4v', 'mkv': 'video/x-matroska', 'webm': 'video/webm',
             'mov': 'video/quicktime', 'avi': 'video/x-msvideo', 'wmv': 'video/x-ms-wmv', 'mpg': 'video/mpeg',
             'flv': 'video/x-flv'}
    Audio = {'mid': 'audio/midi', 'mp3': 'audio/mpeg', 'm4a': 'audio/m4a', 'ogg': 'audio/ogg',
             'flac': 'audio/x-flac', 'wav': 'audio/x-wav', 'amr': 'audio/amr'}
    Archive = {'epub': 'application/epub+zip', 'zip': 'application/zip', 'tar': 'application/x-tar',
               'rar': 'application/x-rar-compressed', 'gz': 'application/gzip', 'bz2': 'application/x-bzip2',
               '7z': 'application/x-7z-compressed', 'xz': 'application/x-xz', 'pdf': 'application/pdf',
               'exe': 'application/x-msdownload', 'swf': 'application/x-shockwave-flash', 'rtf': 'application/rtf',
               'eot': 'application/octet-stream', 'ps': 'application/postscript', 'sqlite': 'application/x-sqlite3',
               'nes': 'application/x-nintendo-nes-rom', 'crx': 'application/x-google-chrome-extension',
               'cab': 'application/vnd.ms-cab-compressed', 'deb': 'application/x-deb',
               'ar': 'application/x-unix-archive', 'Z': 'application/x-compress', 'lz': 'application/x-lzip'}
    Font = {'woff': 'application/font-woff', 'woff2': 'application/font-woff', 'ttf': 'application/font-sfnt',
            'otf': 'application/font-sfnt'}
    if headers:
        contentType = headers['ContentType']
        if contentType in Image.values():
            return {'type': 'Image', 'mine': contentType,
                    'ext': list(Image.keys())[list(Image.values()).index(contentType)]}
        elif contentType in Video.values():
            return {'type': 'Video', 'mine': contentType,
                    'ext': list(Video.keys())[list(Video.values()).index(contentType)]}
        elif contentType in Audio.values():
            return {'type': 'Audio', 'mine': contentType,
                    'ext': list(Audio.keys())[list(Audio.values()).index(contentType)]}
        elif contentType in Archive.values():
            return {'type': 'Archive', 'mine': contentType,
                    'ext': list(Archive.keys())[list(Archive.values()).index(contentType)]}
        elif contentType in Font.values():
            return {'type': 'Font', 'mine': contentType,
                    'ext': list(Font.keys())[list(Font.values()).index(contentType)]}
        else:
            return {}
    else:
        return {}


def getUrlFileName(url, filetype):
    """
    根据下载链接返回文件名称
    :param url:
    :return:
    """
    reg = r'https*://.*?\/tumblr_(.*)'
    namere = re.compile(reg)
    url = quote(url, safe=string.printable)
    nameList = re.findall(namere, url)
    if nameList:
        name = nameList[0]
    else:
        name = 'page1'
    name = "tumblr_" + name
    if name.find('/') > 0:
        name = name[:name.index('/')]
    if filetype['type'] == 'Video':
        name = name + "." + filetype['ext']
    return name


def downloadFile(fileurl, filename, filetype, sql, data):
    """
    下载文件
    :param fileurl:
    :param filename:
    :return:
    """
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    if not os.path.exists(video_path):
        os.makedirs(video_path)
    if filetype == 'Video':
        target = video_path + filename
    elif filetype == 'Image':
        target = img_path + filename
    else:
        print("未知文件类型不下载")
        return
    if not FileRemoveRepeat.judgeFileExistByName(filename):
        auto_down(fileurl, target, filetype)
        print("新文件 %s  %s 下载" % (fileurl, target))
        MysqlUtil.excute(sql, data)
    else:
        print("已存在 %s  %s 不下载" % (fileurl, target))


def auto_down(fileurl, target, filetype):
    """
    封装自动下载方法，处理网络不稳定下载失败
    :param fileurl:
    :param target:
    :return:
    """
    try:
        fileurl = quote(fileurl, safe=string.printable)
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(fileurl, target)
    except:
        traceback.print_exc()
        auto_down(fileurl, target, filetype)
        print('The %s is deleted or not found.' % filetype)


def judgeDown(url):
    """
    根据URL 判断是否下载该文件
    :param url:
    :return:
    """
    headers = getHeaders(url)
    contentLength = headers['ContentLength']
    contentLength = int(contentLength)
    filetype = judgeFileType(headers)
    if filetype:
        if filetype['type'] == "Image":
            if contentLength > imagedownsize:
                print('满足下载 %s 大小为 %s Kb 类型 %s 后缀 %s mime类型 %s' % (
                    url, math.ceil(contentLength / 1024), filetype['type'], filetype['ext'], filetype['mine']))
                result = True
            else:
                print('不下载 文件网址 %s 大小为 %s Kb 类型 %s 后缀 %s mime类型 %s' % (
                    url, math.ceil(contentLength / 1024), filetype['type'], filetype['ext'], filetype['mine']))
                result = False
        elif filetype['type'] == "Video":
            if contentLength > videodownsize:
                print('满足下载 文件网址 %s 大小为 %s Kb 类型 %s 后缀 %s mime类型 %s' % (
                    url, math.ceil(contentLength / 1024), filetype['type'], filetype['ext'], filetype['mine']))
                result = True
            else:
                print('不下载 文件网址 %s 大小为 %s Kb 类型 %s 后缀 %s mime类型 %s' % (
                    url, math.ceil(contentLength / 1024), filetype['type'], filetype['ext'], filetype['mine']))
                result = False
        else:
            print('非视频图片 文件网址 %s 大小为 %s Kb 类型 %s 后缀 %s mime类型 %s' % (
                url, math.ceil(contentLength / 1024), filetype['type'], filetype['ext'], filetype['mine']))
            result = False
    else:
        print('无效网址 %s' % url)
        result = False
    if result:
        filename = getUrlFileName(url, filetype)
        sql = 'insert into download_url (url,filename,size,type,ext,mine) VALUE (%s,%s,%s,%s,%s,%s) '
        data = (url, filename, math.ceil(contentLength / 1024), filetype['type'], filetype['ext'], filetype['mine'])
        downloadFile(url, filename, filetype['type'], sql, data)


if __name__ == '__main__':
    user = 'fefe'
