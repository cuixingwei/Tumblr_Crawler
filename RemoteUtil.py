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

# 图片下载大小阈值  250Kb
imagedownsize = 1024 * 150

# 视频下载大小阈值 5Mb
videodownsize = 1024 * 1024 * 5

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
        print("封装headers出错")
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
    name = ''
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


def downloadFile(fileurl, filename, filetype):
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
        print('未知文件类型不下载')
        return
    try:
        fileurl = quote(fileurl, safe=string.printable)
        urllib.request.urlretrieve(fileurl, target)
    except:
        traceback.print_exc()
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
                print('下载的 文件网址 %s 大小为 %s Kb 类型 %s 后缀 %s mime类型 %s' % (
                    url, math.ceil(contentLength / 1024), filetype['type'], filetype['ext'], filetype['mine']))
                result = True
            else:
                print('不下载 文件网址 %s 大小为 %s Kb 类型 %s 后缀 %s mime类型 %s' % (
                    url, math.ceil(contentLength / 1024), filetype['type'], filetype['ext'], filetype['mine']))
                result = False
        elif filetype['type'] == "Video":
            if contentLength > videodownsize:
                print('下载的 文件网址 %s 大小为 %s Kb 类型 %s 后缀 %s mime类型 %s' % (
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
        MysqlUtil.excute(sql, data)
        downloadFile(url, filename, filetype['type'])


if __name__ == '__main__':
    urlImgList = ['https://68.media.tumblr.com/667201ba54e5d9c3f9f5e8b026bee1a5/tumblr_od6eavZ3rV1uxoh6yo6_1280.jpg',
                  'https://68.media.tumblr.com/990908066829f92a4a6509f27411ea08/tumblr_od6eavZ3rV1uxoh6yo2_1280.jpg',
                  'https://68.media.tumblr.com/afd103d7926081f196c546dd24da5e5a/tumblr_od6eavZ3rV1uxoh6yo7_1280.jpg',
                  'https://68.media.tumblr.com/e2f75f5b8d1a6bd85644ca25a121a47d/tumblr_od6eavZ3rV1uxoh6yo8_1280.jpg',
                  'https://68.media.tumblr.com/e2df39f8d672c83afdb4bb966bc1bfb7/tumblr_od6eavZ3rV1uxoh6yo5_1280.jpg',
                  'https://68.media.tumblr.com/ccbdf724d1393fe8389d694615159857/tumblr_od6eavZ3rV1uxoh6yo3_1280.jpg',
                  'https://68.media.tumblr.com/e2df39f8d672c83afdb4bb966bc1bfb7/tumblr_od6eavZ3rV1uxoh6yo4_1280.jpg']
    urlVideoList = [
        'https://oooxniooo.tumblr.com/video_file/t:k0LztXuyykvtDYa-3VIyIg/139691771794/tumblr_o0jeq9GFLU1ux8oee']
    url = r'https://68.media.tumblr.com/990908066829f92a4a6509f27411ea08/tumblr_od6eavZ3rV1uxoh6yo2_1280.jpg'
    list = ['https://xwcui.tumblr.com/video_file/t:gmEl28RzcgfmlkEJJ6K4Mw/164786216628/tumblr_o4bwvg1T7A1uxmo1u',
            'https://xwcui.tumblr.com/video_file/t:gmEl28RzcgfmlkEJJ6K4Mw/162411143698/tumblr_nuwimcorhK1ur5eqb',
            'https://xwcui.tumblr.com/video_file/t:gmEl28RzcgfmlkEJJ6K4Mw/161737849523/tumblr_o7cmy6WTCv1vu3mul',
            'https://xwcui.tumblr.com/video_file/t:gmEl28RzcgfmlkEJJ6K4Mw/161584922328/tumblr_o1t8oqmJMp1v5ithl/480',
            'https://xwcui.tumblr.com/video_file/t:gmEl28RzcgfmlkEJJ6K4Mw/160783888658/tumblr_nwyz2sMvVs1ua51rq',
            'https://xwcui.tumblr.com/video_file/t:gmEl28RzcgfmlkEJJ6K4Mw/160783559723/tumblr_o59dkgwE1a1sdiiuv',
            'https://xwcui.tumblr.com/video_file/t:gmEl28RzcgfmlkEJJ6K4Mw/159018263478/tumblr_okzg94y1ya1ukpv9m',
            'https://xwcui.tumblr.com/video_file/t:gmEl28RzcgfmlkEJJ6K4Mw/159018037983/tumblr_olx26zG47R1ukpv9m',
            'https://xwcui.tumblr.com/video_file/t:gmEl28RzcgfmlkEJJ6K4Mw/159017619233/tumblr_o63jelp8AG1vq3pfj',
            'https://xwcui.tumblr.com/video_file/t:gmEl28RzcgfmlkEJJ6K4Mw/159004465168/tumblr_o7dr5qtknw1tqr9po',
            'https://xwcui.tumblr.com/video_file/t:gmEl28RzcgfmlkEJJ6K4Mw/159003790378/tumblr_nuf4icRiD01udp704',
            'https://xwcui.tumblr.com/video_file/t:gmEl28RzcgfmlkEJJ6K4Mw/158955832883/tumblr_oacbr5dAPP1v9x8wv/480',
            'https://xwcui.tumblr.com/video_file/t:gmEl28RzcgfmlkEJJ6K4Mw/158944956303/tumblr_ntxmmiNDTn1uatgt2',
            'https://xwcui.tumblr.com/video_file/t:gmEl28RzcgfmlkEJJ6K4Mw/158929345138/tumblr_o5x081SeEm1vqwp3e',
            'https://xwcui.tumblr.com/video_file/t:gmEl28RzcgfmlkEJJ6K4Mw/158929271063/tumblr_oac3221GDQ1vnl0qg/480',
            'https://xwcui.tumblr.com/video_file/t:gmEl28RzcgfmlkEJJ6K4Mw/158929152913/tumblr_o7ptmehyeN1v079ne',
            'https://68.media.tumblr.com/34f6b4fc6b6670cb11bf86cfd2339488/tumblr_o2j39oNvvU1v6u3vio1_1280.jpg',
            'https://68.media.tumblr.com/38d9377ff36c0edd7b4202c9dcf3a503/tumblr_o2j39oNvvU1v6u3vio5_1280.jpg',
            'https://68.media.tumblr.com/c339f34361d564dd7fb6facbc09b82c9/tumblr_o2j39oNvvU1v6u3vio2_1280.jpg',
            'https://68.media.tumblr.com/49165f596e351ca05f90f5a64822a4b3/tumblr_o2j39oNvvU1v6u3vio3_1280.jpg',
            'https://68.media.tumblr.com/3aec473f923469ff30419c58ae7e8381/tumblr_o2j39oNvvU1v6u3vio4_1280.jpg',
            'https://xwcui.tumblr.com/video_file/t:gmEl28RzcgfmlkEJJ6K4Mw/158929054983/tumblr_o2kwefHViI1u6bsy0',
            'https://68.media.tumblr.com/0c59587f86a209d025696dcfbe0c6101/tumblr_o2lst01YTi1u6deczo1_500.jpg',
            'https://68.media.tumblr.com/a115d770389a445619c808c773259201/tumblr_npgc925zAI1t1muopo1_500.jpg',
            'https://68.media.tumblr.com/3742f0919c162d26cbe3be45b3770c28/tumblr_nxt7yx2Pp21ujccjqo1_1280.jpg',
            'https://68.media.tumblr.com/183ec94bd6c28cc616ab6e8b2163bdeb/tumblr_nxt7yx2Pp21ujccjqo3_r1_500.jpg',
            'https://68.media.tumblr.com/1f663a5e9550763f849662e21009c1ee/tumblr_nxt7yx2Pp21ujccjqo4_r1_1280.jpg',
            'https://68.media.tumblr.com/d8316e51b2c413b865c1d5945457a7ec/tumblr_nxt7yx2Pp21ujccjqo2_r1_400.jpg',
            'https://68.media.tumblr.com/9184687544d3c44eaf43a2f755fc27de/tumblr_oc14mx0l1x1vqhed4o3_500.jpg',
            'https://68.media.tumblr.com/620e4f10e5441ec703de737d6b8f3c5f/tumblr_oc14mx0l1x1vqhed4o1_500.jpg',
            'https://68.media.tumblr.com/309b8a8a0c7be85291634613ac38bfb6/tumblr_oc14mx0l1x1vqhed4o5_500.jpg',
            'https://68.media.tumblr.com/e468403959cabbeecbfded415e2a873e/tumblr_oc14mx0l1x1vqhed4o9_r1_500.gif',
            'https://68.media.tumblr.com/bb0fd119565cf6e7b9c080cfd92affa0/tumblr_oc14mx0l1x1vqhed4o2_500.jpg',
            'https://68.media.tumblr.com/a4d2d3ce8b3a5132020983534f6c9961/tumblr_oc14mx0l1x1vqhed4o4_500.jpg',
            'https://68.media.tumblr.com/16f00691ef80c815fbb909c2e588a323/tumblr_oc14mx0l1x1vqhed4o6_500.jpg',
            'https://68.media.tumblr.com/e575c3529a10b2fce9aa0c16df0511b8/tumblr_oc14mx0l1x1vqhed4o7_500.jpg',
            'https://68.media.tumblr.com/a99364aca1e2c11749473f874430523b/tumblr_oc14mx0l1x1vqhed4o8_500.jpg']
    print(len(list))
    n = int(math.ceil(len(list) / float(10)))
    l = [list[i:i + n] for i in range(0, len(list), n)]
    print(l)
    for i in range(0, len(list), n):
        print(i)
