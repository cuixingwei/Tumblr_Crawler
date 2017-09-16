# -*- coding: utf-8 -*-
"""
  Author:  xwcui
  Purpose: 获取视频mediainfo信息
  Created: 2017-9-16
"""

from pprint import pprint
import math
from pymediainfo import MediaInfo
import FileUtil
import MysqlUtil


def getMediaInfo(fname):
    videoinfo = {}
    media_info = MediaInfo.parse(fname)
    for track in media_info.tracks:
        if track.track_type == 'General':
            videoinfo['duration'] = math.ceil(track.duration / 1000)
            videoinfo['file_size'] = math.ceil(track.file_size / 1024)
            videoinfo['complete_name'] = track.complete_name
            videoinfo['overall_bit_rate'] = math.ceil(track.overall_bit_rate / 1024)
        elif track.track_type == 'Video':
            videoinfo['stream_size'] = math.ceil(track.stream_size / 1024)
            videoinfo['frame_rate'] = track.frame_rate
            videoinfo['height'] = track.height
            videoinfo['width'] = track.width
    return videoinfo


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


def updateFileInfoToDatabase():
    """
    更新数据中记录文件的信息
    :return:
    """
    sql = 'SELECT * from source_md5 where type = %s and file_size is not null  '
    data = ('video')
    result = MysqlUtil.select(sql, data)
    for i, e in enumerate(result):
        fpath = e['path']
        if FileUtil.fileExist(fpath):
            videoinfo = getMediaInfo(fpath)
            if videoinfo:
                sql = 'update source_md5 set path=%s,duration=%s,file_size=%s,stream_size=%s,frame_rate=%s,' \
                      'width=%s,height=%s,overall_bit_rate=%s where id= %s '
                data = (videoinfo['complete_name'], videoinfo['duration'], videoinfo['file_size'],
                        videoinfo['stream_size'], videoinfo['frame_rate'], videoinfo['width'],
                        videoinfo['height'], videoinfo['overall_bit_rate'], e['id'])
                MysqlUtil.excute(sql, data)
                print('第 %s 个文件' % i, videoinfo)
        else:
            print('第 %s 个文件 %s 的不存在' % (i, fpath))
            sql = 'delete from source_md5  where id= %s '
            data = (e['id'])
            MysqlUtil.excute(sql, data)


if __name__ == '__main__':
    updateFileInfoToDatabase()  # 更新视频信息
