# -*- coding: utf-8 -*-

"""
  Author:   xwcui
  Purpose:  remove repeat file(video,img)
  Created:  2017-9-3
"""

import cv2


def getVideoCvInfo(localurl):
    videocapture = cv2.VideoCapture(localurl)  # 用videocapture获取视频信息
    if videocapture:
        print('-' * 21)
        CAP_ANDROID = videocapture.get(cv2.CAP_ANDROID)
        print('CAP_ANDROID %s' % CAP_ANDROID)

        CAP_ANY = videocapture.get(cv2.CAP_ANY)
        print('CAP_ANY %s' % CAP_ANY)

        CAP_ARAVIS = videocapture.get(cv2.CAP_ARAVIS)
        print('CAP_ARAVIS %s' % CAP_ARAVIS)

        CAP_AVFOUNDATION = videocapture.get(cv2.CAP_AVFOUNDATION)
        print('CAP_AVFOUNDATION %s' % CAP_AVFOUNDATION)

        CAP_CMU1394 = videocapture.get(cv2.CAP_CMU1394)
        print('CAP_CMU1394 %s' % CAP_CMU1394)

        CAP_DC1394 = videocapture.get(cv2.CAP_DC1394)
        print('CAP_DC1394 %s' % CAP_DC1394)

        CAP_DSHOW = videocapture.get(cv2.CAP_DSHOW)
        print('CAP_DSHOW %s' % CAP_DSHOW)

        CAP_FFMPEG = videocapture.get(cv2.CAP_FFMPEG)
        print('CAP_FFMPEG %s' % CAP_FFMPEG)

        CAP_FIREWARE = videocapture.get(cv2.CAP_FIREWARE)
        print('CAP_FIREWARE %s' % CAP_FIREWARE)

        CAP_FIREWIRE = videocapture.get(cv2.CAP_FIREWIRE)
        print('CAP_FIREWIRE %s' % CAP_FIREWIRE)

        CAP_GIGANETIX = videocapture.get(cv2.CAP_GIGANETIX)
        print('CAP_GIGANETIX %s' % CAP_GIGANETIX)

        CAP_GPHOTO2 = videocapture.get(cv2.CAP_GPHOTO2)
        print('CAP_GPHOTO2 %s' % CAP_GPHOTO2)

        CAP_GSTREAMER = videocapture.get(cv2.CAP_GSTREAMER)
        print('CAP_GSTREAMER %s' % CAP_GSTREAMER)

        CAP_IEEE1394 = videocapture.get(cv2.CAP_IEEE1394)
        print('CAP_IEEE1394 %s' % CAP_IEEE1394)

        CAP_IMAGES = videocapture.get(cv2.CAP_IMAGES)
        print('CAP_IMAGES %s' % CAP_IMAGES)

        CAP_INTELPERC = videocapture.get(cv2.CAP_INTELPERC)
        print('CAP_INTELPERC %s' % CAP_INTELPERC)

        print('-' * 21)
        CAP_INTELPERC_DEPTH_GENERATOR = videocapture.get(cv2.CAP_INTELPERC_DEPTH_GENERATOR)
        print('CAP_INTELPERC_DEPTH_GENERATOR %s' % CAP_INTELPERC_DEPTH_GENERATOR)

        CAP_INTELPERC_DEPTH_MAP = videocapture.get(cv2.CAP_INTELPERC_DEPTH_MAP)
        print('CAP_INTELPERC_DEPTH_MAP %s' % CAP_INTELPERC_DEPTH_MAP)

        print('-' * 21)
        CAP_INTELPERC_GENERATORS_MASK = videocapture.get(cv2.CAP_INTELPERC_GENERATORS_MASK)
        print('CAP_INTELPERC_GENERATORS_MASK %s' % CAP_INTELPERC_GENERATORS_MASK)

        print('-' * 21)
        CAP_INTELPERC_IMAGE = videocapture.get(cv2.CAP_INTELPERC_IMAGE)
        print('CAP_INTELPERC_IMAGE %s' % CAP_INTELPERC_IMAGE)

        print('-' * 21)
        CAP_INTELPERC_IMAGE_GENERATOR = videocapture.get(cv2.CAP_INTELPERC_IMAGE_GENERATOR)
        print('CAP_INTELPERC_IMAGE_GENERATOR %s' % CAP_INTELPERC_IMAGE_GENERATOR)

        print('-' * 21)
        CAP_INTELPERC_IR_MAP = videocapture.get(cv2.CAP_INTELPERC_IR_MAP)
        print('CAP_INTELPERC_IR_MAP %s' % CAP_INTELPERC_IR_MAP)

        print('-' * 21)
        CAP_INTELPERC_UVDEPTH_MAP = videocapture.get(cv2.CAP_INTELPERC_UVDEPTH_MAP)
        print('CAP_INTELPERC_UVDEPTH_MAP %s' % CAP_INTELPERC_UVDEPTH_MAP)

        print('-' * 21)
        CAP_INTEL_MFX = videocapture.get(cv2.CAP_INTEL_MFX)
        print('CAP_INTEL_MFX %s' % CAP_INTEL_MFX)

        print('-' * 21)
        CAP_MODE_BGR = videocapture.get(cv2.CAP_MODE_BGR)
        print('CAP_MODE_BGR %s' % CAP_MODE_BGR)

        CAP_MODE_GRAY = videocapture.get(cv2.CAP_MODE_GRAY)
        print('CAP_MODE_GRAY %s' % CAP_MODE_GRAY)

        CAP_MODE_RGB = videocapture.get(cv2.CAP_MODE_RGB)
        print('CAP_MODE_RGB %s' % CAP_MODE_RGB)

        CAP_MODE_YUYV = videocapture.get(cv2.CAP_MODE_YUYV)
        print('CAP_MODE_YUYV %s' % CAP_MODE_YUYV)

        print('-' * 21)
        CAP_MSMF = videocapture.get(cv2.CAP_MSMF)
        print('CAP_MSMF %s' % CAP_MSMF)

        print('-' * 21)
        CAP_OPENCV_MJPEG = videocapture.get(cv2.CAP_OPENCV_MJPEG)
        print('CAP_OPENCV_MJPEG %s' % CAP_OPENCV_MJPEG)

        print('-' * 21)
        CAP_OPENNI = videocapture.get(cv2.CAP_OPENNI)
        print('CAP_OPENNI %s' % CAP_OPENNI)

        CAP_OPENNI2 = videocapture.get(cv2.CAP_OPENNI2)
        print('CAP_OPENNI2 %s' % CAP_OPENNI2)

        print('-' * 21)
        CAP_OPENNI2_ASUS = videocapture.get(cv2.CAP_OPENNI2_ASUS)
        print('CAP_OPENNI2_ASUS %s' % CAP_OPENNI2_ASUS)

        print('-' * 21)
        CAP_OPENNI_ASUS = videocapture.get(cv2.CAP_OPENNI_ASUS)
        print('CAP_OPENNI_ASUS %s' % CAP_OPENNI_ASUS)

        print('-' * 21)
        CAP_OPENNI_BGR_IMAGE = videocapture.get(cv2.CAP_OPENNI_BGR_IMAGE)
        print('CAP_OPENNI_BGR_IMAGE %s' % CAP_OPENNI_BGR_IMAGE)

        print('-' * 21)
        CAP_OPENNI_DEPTH_GENERATOR = videocapture.get(cv2.CAP_OPENNI_DEPTH_GENERATOR)
        print('CAP_OPENNI_DEPTH_GENERATOR %s' % CAP_OPENNI_DEPTH_GENERATOR)

        print('-' * 21)
        CAP_OPENNI_DEPTH_GENERATOR_BASELINE = videocapture.get(cv2.CAP_OPENNI_DEPTH_GENERATOR_BASELINE)
        print('CAP_OPENNI_DEPTH_GENERATOR_BASELINE %s' % CAP_OPENNI_DEPTH_GENERATOR_BASELINE)

        print('-' * 21)
        CAP_OPENNI_DEPTH_GENERATOR_FOCAL_LENGTH = videocapture.get(cv2.CAP_OPENNI_DEPTH_GENERATOR_FOCAL_LENGTH)
        print('CAP_OPENNI_DEPTH_GENERATOR_FOCAL_LENGTH %s' % CAP_OPENNI_DEPTH_GENERATOR_FOCAL_LENGTH)

        print('-' * 21)
        CAP_OPENNI_DEPTH_GENERATOR_PRESENT = videocapture.get(cv2.CAP_OPENNI_DEPTH_GENERATOR_PRESENT)
        print('CAP_OPENNI_DEPTH_GENERATOR_PRESENT %s' % CAP_OPENNI_DEPTH_GENERATOR_PRESENT)

        CAP_OPENNI_DEPTH_GENERATOR_REGISTRATION = videocapture.get(cv2.CAP_OPENNI_DEPTH_GENERATOR_REGISTRATION)
        print('CAP_OPENNI_DEPTH_GENERATOR_REGISTRATION %s' % CAP_OPENNI_DEPTH_GENERATOR_REGISTRATION)

        print('-' * 21)
        CAP_OPENNI_DEPTH_MAP = videocapture.get(cv2.CAP_OPENNI_DEPTH_MAP)
        print('CAP_OPENNI_DEPTH_MAP %s' % CAP_OPENNI_DEPTH_MAP)

        print('-' * 21)
        CAP_OPENNI_DISPARITY_MAP = videocapture.get(cv2.CAP_OPENNI_DISPARITY_MAP)
        print('CAP_OPENNI_DISPARITY_MAP %s' % CAP_OPENNI_DISPARITY_MAP)

        print('-' * 21)
        CAP_OPENNI_DISPARITY_MAP_32F = videocapture.get(cv2.CAP_OPENNI_DISPARITY_MAP_32F)
        print('CAP_OPENNI_DISPARITY_MAP_32F %s' % CAP_OPENNI_DISPARITY_MAP_32F)

        print('-' * 21)
        CAP_OPENNI_GENERATORS_MASK = videocapture.get(cv2.CAP_OPENNI_GENERATORS_MASK)
        print('CAP_OPENNI_GENERATORS_MASK %s' % CAP_OPENNI_GENERATORS_MASK)

        print('-' * 21)
        CAP_OPENNI_GRAY_IMAGE = videocapture.get(cv2.CAP_OPENNI_GRAY_IMAGE)
        print('CAP_OPENNI_GRAY_IMAGE %s' % CAP_OPENNI_GRAY_IMAGE)

        print('-' * 21)
        CAP_OPENNI_IMAGE_GENERATOR = videocapture.get(cv2.CAP_OPENNI_IMAGE_GENERATOR)
        print('CAP_OPENNI_IMAGE_GENERATOR %s' % CAP_OPENNI_IMAGE_GENERATOR)

        print('-' * 21)
        CAP_OPENNI_IMAGE_GENERATOR_OUTPUT_MODE = videocapture.get(cv2.CAP_OPENNI_IMAGE_GENERATOR_OUTPUT_MODE)
        print('CAP_OPENNI_IMAGE_GENERATOR_OUTPUT_MODE %s' % CAP_OPENNI_IMAGE_GENERATOR_OUTPUT_MODE)

        print('-' * 21)
        CAP_OPENNI_IMAGE_GENERATOR_PRESENT = videocapture.get(cv2.CAP_OPENNI_IMAGE_GENERATOR_PRESENT)
        print('CAP_OPENNI_IMAGE_GENERATOR_PRESENT %s' % CAP_OPENNI_IMAGE_GENERATOR_PRESENT)

        print('-' * 21)
        CAP_OPENNI_IR_GENERATOR = videocapture.get(cv2.CAP_OPENNI_IR_GENERATOR)
        print('CAP_OPENNI_IR_GENERATOR %s' % CAP_OPENNI_IR_GENERATOR)

        print('-' * 21)
        CAP_OPENNI_IR_GENERATOR_PRESENT = videocapture.get(cv2.CAP_OPENNI_IR_GENERATOR_PRESENT)
        print('CAP_OPENNI_IR_GENERATOR_PRESENT %s' % CAP_OPENNI_IR_GENERATOR_PRESENT)

        print('-' * 21)
        CAP_OPENNI_IR_IMAGE = videocapture.get(cv2.CAP_OPENNI_IR_IMAGE)
        print('CAP_OPENNI_IR_IMAGE %s' % CAP_OPENNI_IR_IMAGE)

        print('-' * 21)
        CAP_OPENNI_POINT_CLOUD_MAP = videocapture.get(cv2.CAP_OPENNI_POINT_CLOUD_MAP)
        print('CAP_OPENNI_POINT_CLOUD_MAP %s' % CAP_OPENNI_POINT_CLOUD_MAP)

        print('-' * 21)
        CAP_OPENNI_QVGA_30HZ = videocapture.get(cv2.CAP_OPENNI_QVGA_30HZ)
        print('CAP_OPENNI_QVGA_30HZ %s' % CAP_OPENNI_QVGA_30HZ)

        CAP_OPENNI_QVGA_60HZ = videocapture.get(cv2.CAP_OPENNI_QVGA_60HZ)
        print('CAP_OPENNI_QVGA_60HZ %s' % CAP_OPENNI_QVGA_60HZ)

        print('-' * 21)
        CAP_OPENNI_SXGA_15HZ = videocapture.get(cv2.CAP_OPENNI_SXGA_15HZ)
        print('CAP_OPENNI_SXGA_15HZ %s' % CAP_OPENNI_SXGA_15HZ)

        CAP_OPENNI_SXGA_30HZ = videocapture.get(cv2.CAP_OPENNI_SXGA_30HZ)
        print('CAP_OPENNI_SXGA_30HZ %s' % CAP_OPENNI_SXGA_30HZ)

        print('-' * 21)
        CAP_OPENNI_VALID_DEPTH_MASK = videocapture.get(cv2.CAP_OPENNI_VALID_DEPTH_MASK)
        print('CAP_OPENNI_VALID_DEPTH_MASK %s' % CAP_OPENNI_VALID_DEPTH_MASK)

        print('-' * 21)
        CAP_OPENNI_VGA_30HZ = videocapture.get(cv2.CAP_OPENNI_VGA_30HZ)
        print('CAP_OPENNI_VGA_30HZ %s' % CAP_OPENNI_VGA_30HZ)

        print('-' * 21)
        CAP_PROP_APERTURE = videocapture.get(cv2.CAP_PROP_APERTURE)
        print('CAP_PROP_APERTURE %s' % CAP_PROP_APERTURE)

        CAP_PROP_AUTOFOCUS = videocapture.get(cv2.CAP_PROP_AUTOFOCUS)
        print('CAP_PROP_AUTOFOCUS %s' % CAP_PROP_AUTOFOCUS)

        print('-' * 21)
        CAP_PROP_AUTO_EXPOSURE = videocapture.get(cv2.CAP_PROP_AUTO_EXPOSURE)
        print('CAP_PROP_AUTO_EXPOSURE %s' % CAP_PROP_AUTO_EXPOSURE)

        print('-' * 21)
        CAP_PROP_BACKLIGHT = videocapture.get(cv2.CAP_PROP_BACKLIGHT)
        print('CAP_PROP_BACKLIGHT %s' % CAP_PROP_BACKLIGHT)

        CAP_PROP_BRIGHTNESS = videocapture.get(cv2.CAP_PROP_BRIGHTNESS)
        print('CAP_PROP_BRIGHTNESS %s' % CAP_PROP_BRIGHTNESS)

        CAP_PROP_BUFFERSIZE = videocapture.get(cv2.CAP_PROP_BUFFERSIZE)
        print('CAP_PROP_BUFFERSIZE %s' % CAP_PROP_BUFFERSIZE)

        CAP_PROP_CONTRAST = videocapture.get(cv2.CAP_PROP_CONTRAST)
        print('CAP_PROP_CONTRAST %s' % CAP_PROP_CONTRAST)

        print('-' * 21)
        CAP_PROP_CONVERT_RGB = videocapture.get(cv2.CAP_PROP_CONVERT_RGB)
        print('CAP_PROP_CONVERT_RGB %s' % CAP_PROP_CONVERT_RGB)

        print('-' * 21)
        CAP_PROP_DC1394_MAX = videocapture.get(cv2.CAP_PROP_DC1394_MAX)
        print('CAP_PROP_DC1394_MAX %s' % CAP_PROP_DC1394_MAX)

        print('-' * 21)
        CAP_PROP_DC1394_MODE_AUTO = videocapture.get(cv2.CAP_PROP_DC1394_MODE_AUTO)
        print('CAP_PROP_DC1394_MODE_AUTO %s' % CAP_PROP_DC1394_MODE_AUTO)

        CAP_PROP_DC1394_MODE_MANUAL = videocapture.get(cv2.CAP_PROP_DC1394_MODE_MANUAL)
        print('CAP_PROP_DC1394_MODE_MANUAL %s' % CAP_PROP_DC1394_MODE_MANUAL)

        print('-' * 21)
        CAP_PROP_DC1394_MODE_ONE_PUSH_AUTO = videocapture.get(cv2.CAP_PROP_DC1394_MODE_ONE_PUSH_AUTO)
        print('CAP_PROP_DC1394_MODE_ONE_PUSH_AUTO %s' % CAP_PROP_DC1394_MODE_ONE_PUSH_AUTO)

        print('-' * 21)
        CAP_PROP_DC1394_OFF = videocapture.get(cv2.CAP_PROP_DC1394_OFF)
        print('CAP_PROP_DC1394_OFF %s' % CAP_PROP_DC1394_OFF)

        print('-' * 21)
        CAP_PROP_EXPOSURE = videocapture.get(cv2.CAP_PROP_EXPOSURE)
        print('CAP_PROP_EXPOSURE %s' % CAP_PROP_EXPOSURE)

        CAP_PROP_EXPOSUREPROGRAM = videocapture.get(cv2.CAP_PROP_EXPOSUREPROGRAM)
        print('CAP_PROP_EXPOSUREPROGRAM %s' % CAP_PROP_EXPOSUREPROGRAM)

        CAP_PROP_FOCUS = videocapture.get(cv2.CAP_PROP_FOCUS)
        print('CAP_PROP_FOCUS %s' % CAP_PROP_FOCUS)

        CAP_PROP_FORMAT = videocapture.get(cv2.CAP_PROP_FORMAT)
        print('CAP_PROP_FORMAT %s' % CAP_PROP_FORMAT)

        CAP_PROP_FOURCC = videocapture.get(cv2.CAP_PROP_FOURCC)
        print('CAP_PROP_FOURCC %s' % CAP_PROP_FOURCC)

        CAP_PROP_FPS = videocapture.get(cv2.CAP_PROP_FPS)
        print('CAP_PROP_FPS %s' % CAP_PROP_FPS)

        print('-' * 21)
        CAP_PROP_FRAME_COUNT = videocapture.get(cv2.CAP_PROP_FRAME_COUNT)
        print('CAP_PROP_FRAME_COUNT %s' % CAP_PROP_FRAME_COUNT)

        CAP_PROP_FRAME_HEIGHT = videocapture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print('CAP_PROP_FRAME_HEIGHT %s' % CAP_PROP_FRAME_HEIGHT)

        CAP_PROP_FRAME_WIDTH = videocapture.get(cv2.CAP_PROP_FRAME_WIDTH)
        print('CAP_PROP_FRAME_WIDTH %s' % CAP_PROP_FRAME_WIDTH)

        print('-' * 21)
        CAP_PROP_GAIN = videocapture.get(cv2.CAP_PROP_GAIN)
        print('CAP_PROP_GAIN %s' % CAP_PROP_GAIN)

        CAP_PROP_GAMMA = videocapture.get(cv2.CAP_PROP_GAMMA)
        print('CAP_PROP_GAMMA %s' % CAP_PROP_GAMMA)

        print('-' * 21)
        CAP_PROP_GIGA_FRAME_HEIGH_MAX = videocapture.get(cv2.CAP_PROP_GIGA_FRAME_HEIGH_MAX)
        print('CAP_PROP_GIGA_FRAME_HEIGH_MAX %s' % CAP_PROP_GIGA_FRAME_HEIGH_MAX)

        print('-' * 21)
        CAP_PROP_GIGA_FRAME_OFFSET_X = videocapture.get(cv2.CAP_PROP_GIGA_FRAME_OFFSET_X)
        print('CAP_PROP_GIGA_FRAME_OFFSET_X %s' % CAP_PROP_GIGA_FRAME_OFFSET_X)

        CAP_PROP_GIGA_FRAME_OFFSET_Y = videocapture.get(cv2.CAP_PROP_GIGA_FRAME_OFFSET_Y)
        print('CAP_PROP_GIGA_FRAME_OFFSET_Y %s' % CAP_PROP_GIGA_FRAME_OFFSET_Y)

        print('-' * 21)
        CAP_PROP_GIGA_FRAME_SENS_HEIGH = videocapture.get(cv2.CAP_PROP_GIGA_FRAME_SENS_HEIGH)
        print('CAP_PROP_GIGA_FRAME_SENS_HEIGH %s' % CAP_PROP_GIGA_FRAME_SENS_HEIGH)

        CAP_PROP_GIGA_FRAME_SENS_WIDTH = videocapture.get(cv2.CAP_PROP_GIGA_FRAME_SENS_WIDTH)
        print('CAP_PROP_GIGA_FRAME_SENS_WIDTH %s' % CAP_PROP_GIGA_FRAME_SENS_WIDTH)

        print('-' * 21)
        CAP_PROP_GIGA_FRAME_WIDTH_MAX = videocapture.get(cv2.CAP_PROP_GIGA_FRAME_WIDTH_MAX)
        print('CAP_PROP_GIGA_FRAME_WIDTH_MAX %s' % CAP_PROP_GIGA_FRAME_WIDTH_MAX)

        print('-' * 21)
        CAP_PROP_GPHOTO2_COLLECT_MSGS = videocapture.get(cv2.CAP_PROP_GPHOTO2_COLLECT_MSGS)
        print('CAP_PROP_GPHOTO2_COLLECT_MSGS %s' % CAP_PROP_GPHOTO2_COLLECT_MSGS)

        print('-' * 21)
        CAP_PROP_GPHOTO2_FLUSH_MSGS = videocapture.get(cv2.CAP_PROP_GPHOTO2_FLUSH_MSGS)
        print('CAP_PROP_GPHOTO2_FLUSH_MSGS %s' % CAP_PROP_GPHOTO2_FLUSH_MSGS)

        print('-' * 21)
        CAP_PROP_GPHOTO2_PREVIEW = videocapture.get(cv2.CAP_PROP_GPHOTO2_PREVIEW)
        print('CAP_PROP_GPHOTO2_PREVIEW %s' % CAP_PROP_GPHOTO2_PREVIEW)

        print('-' * 21)
        CAP_PROP_GPHOTO2_RELOAD_CONFIG = videocapture.get(cv2.CAP_PROP_GPHOTO2_RELOAD_CONFIG)
        print('CAP_PROP_GPHOTO2_RELOAD_CONFIG %s' % CAP_PROP_GPHOTO2_RELOAD_CONFIG)

        print('-' * 21)
        CAP_PROP_GPHOTO2_RELOAD_ON_CHANGE = videocapture.get(cv2.CAP_PROP_GPHOTO2_RELOAD_ON_CHANGE)
        print('CAP_PROP_GPHOTO2_RELOAD_ON_CHANGE %s' % CAP_PROP_GPHOTO2_RELOAD_ON_CHANGE)

        print('-' * 21)
        CAP_PROP_GPHOTO2_WIDGET_ENUMERATE = videocapture.get(cv2.CAP_PROP_GPHOTO2_WIDGET_ENUMERATE)
        print('CAP_PROP_GPHOTO2_WIDGET_ENUMERATE %s' % CAP_PROP_GPHOTO2_WIDGET_ENUMERATE)

        print('-' * 21)
        CAP_PROP_GSTREAMER_QUEUE_LENGTH = videocapture.get(cv2.CAP_PROP_GSTREAMER_QUEUE_LENGTH)
        print('CAP_PROP_GSTREAMER_QUEUE_LENGTH %s' % CAP_PROP_GSTREAMER_QUEUE_LENGTH)

        print('-' * 21)
        CAP_PROP_GUID = videocapture.get(cv2.CAP_PROP_GUID)
        print('CAP_PROP_GUID %s' % CAP_PROP_GUID)

        CAP_PROP_HUE = videocapture.get(cv2.CAP_PROP_HUE)
        print('CAP_PROP_HUE %s' % CAP_PROP_HUE)

        print('-' * 21)
        CAP_PROP_IMAGES_BASE = videocapture.get(cv2.CAP_PROP_IMAGES_BASE)
        print('CAP_PROP_IMAGES_BASE %s' % CAP_PROP_IMAGES_BASE)

        CAP_PROP_IMAGES_LAST = videocapture.get(cv2.CAP_PROP_IMAGES_LAST)
        print('CAP_PROP_IMAGES_LAST %s' % CAP_PROP_IMAGES_LAST)

        print('-' * 21)
        CAP_PROP_INTELPERC_DEPTH_CONFIDENCE_THRESHOLD = videocapture.get(
            cv2.CAP_PROP_INTELPERC_DEPTH_CONFIDENCE_THRESHOLD)
        print('CAP_PROP_INTELPERC_DEPTH_CONFIDENCE_THRESHOLD %s' % CAP_PROP_INTELPERC_DEPTH_CONFIDENCE_THRESHOLD)

        print('-' * 21)
        CAP_PROP_INTELPERC_DEPTH_FOCAL_LENGTH_HORZ = videocapture.get(cv2.CAP_PROP_INTELPERC_DEPTH_FOCAL_LENGTH_HORZ)
        print('CAP_PROP_INTELPERC_DEPTH_FOCAL_LENGTH_HORZ %s' % CAP_PROP_INTELPERC_DEPTH_FOCAL_LENGTH_HORZ)

        CAP_PROP_INTELPERC_DEPTH_FOCAL_LENGTH_VERT = videocapture.get(cv2.CAP_PROP_INTELPERC_DEPTH_FOCAL_LENGTH_VERT)
        print('CAP_PROP_INTELPERC_DEPTH_FOCAL_LENGTH_VERT %s' % CAP_PROP_INTELPERC_DEPTH_FOCAL_LENGTH_VERT)

        print('-' * 21)
        CAP_PROP_INTELPERC_DEPTH_LOW_CONFIDENCE_VALUE = videocapture.get(
            cv2.CAP_PROP_INTELPERC_DEPTH_LOW_CONFIDENCE_VALUE)
        print('CAP_PROP_INTELPERC_DEPTH_LOW_CONFIDENCE_VALUE %s' % CAP_PROP_INTELPERC_DEPTH_LOW_CONFIDENCE_VALUE)

        print('-' * 21)
        CAP_PROP_INTELPERC_DEPTH_SATURATION_VALUE = videocapture.get(cv2.CAP_PROP_INTELPERC_DEPTH_SATURATION_VALUE)
        print('CAP_PROP_INTELPERC_DEPTH_SATURATION_VALUE %s' % CAP_PROP_INTELPERC_DEPTH_SATURATION_VALUE)

        print('-' * 21)
        CAP_PROP_INTELPERC_PROFILE_COUNT = videocapture.get(cv2.CAP_PROP_INTELPERC_PROFILE_COUNT)
        print('CAP_PROP_INTELPERC_PROFILE_COUNT %s' % CAP_PROP_INTELPERC_PROFILE_COUNT)

        CAP_PROP_INTELPERC_PROFILE_IDX = videocapture.get(cv2.CAP_PROP_INTELPERC_PROFILE_IDX)
        print('CAP_PROP_INTELPERC_PROFILE_IDX %s' % CAP_PROP_INTELPERC_PROFILE_IDX)

        print('-' * 21)
        CAP_PROP_IOS_DEVICE_EXPOSURE = videocapture.get(cv2.CAP_PROP_IOS_DEVICE_EXPOSURE)
        print('CAP_PROP_IOS_DEVICE_EXPOSURE %s' % CAP_PROP_IOS_DEVICE_EXPOSURE)

        CAP_PROP_IOS_DEVICE_FLASH = videocapture.get(cv2.CAP_PROP_IOS_DEVICE_FLASH)
        print('CAP_PROP_IOS_DEVICE_FLASH %s' % CAP_PROP_IOS_DEVICE_FLASH)

        CAP_PROP_IOS_DEVICE_FOCUS = videocapture.get(cv2.CAP_PROP_IOS_DEVICE_FOCUS)
        print('CAP_PROP_IOS_DEVICE_FOCUS %s' % CAP_PROP_IOS_DEVICE_FOCUS)

        CAP_PROP_IOS_DEVICE_TORCH = videocapture.get(cv2.CAP_PROP_IOS_DEVICE_TORCH)
        print('CAP_PROP_IOS_DEVICE_TORCH %s' % CAP_PROP_IOS_DEVICE_TORCH)

        CAP_PROP_IOS_DEVICE_WHITEBALANCE = videocapture.get(cv2.CAP_PROP_IOS_DEVICE_WHITEBALANCE)
        print('CAP_PROP_IOS_DEVICE_WHITEBALANCE %s' % CAP_PROP_IOS_DEVICE_WHITEBALANCE)

        print('-' * 21)
        CAP_PROP_IRIS = videocapture.get(cv2.CAP_PROP_IRIS)
        print('CAP_PROP_IRIS %s' % CAP_PROP_IRIS)

        print('-' * 21)
        CAP_PROP_ISO_SPEED = videocapture.get(cv2.CAP_PROP_ISO_SPEED)
        print('CAP_PROP_ISO_SPEED %s' % CAP_PROP_ISO_SPEED)

        print('-' * 21)
        CAP_PROP_MODE = videocapture.get(cv2.CAP_PROP_MODE)
        print('CAP_PROP_MODE %s' % CAP_PROP_MODE)

        CAP_PROP_MONOCHROME = videocapture.get(cv2.CAP_PROP_MONOCHROME)
        print('CAP_PROP_MONOCHROME %s' % CAP_PROP_MONOCHROME)

        print('-' * 21)
        CAP_PROP_OPENNI2_MIRROR = videocapture.get(cv2.CAP_PROP_OPENNI2_MIRROR)
        print('CAP_PROP_OPENNI2_MIRROR %s' % CAP_PROP_OPENNI2_MIRROR)

        CAP_PROP_OPENNI2_SYNC = videocapture.get(cv2.CAP_PROP_OPENNI2_SYNC)
        print('CAP_PROP_OPENNI2_SYNC %s' % CAP_PROP_OPENNI2_SYNC)

        print('-' * 21)
        CAP_PROP_OPENNI_APPROX_FRAME_SYNC = videocapture.get(cv2.CAP_PROP_OPENNI_APPROX_FRAME_SYNC)
        print('CAP_PROP_OPENNI_APPROX_FRAME_SYNC %s' % CAP_PROP_OPENNI_APPROX_FRAME_SYNC)

        print('-' * 21)
        CAP_PROP_OPENNI_BASELINE = videocapture.get(cv2.CAP_PROP_OPENNI_BASELINE)
        print('CAP_PROP_OPENNI_BASELINE %s' % CAP_PROP_OPENNI_BASELINE)

        print('-' * 21)
        CAP_PROP_OPENNI_CIRCLE_BUFFER = videocapture.get(cv2.CAP_PROP_OPENNI_CIRCLE_BUFFER)
        print('CAP_PROP_OPENNI_CIRCLE_BUFFER %s' % CAP_PROP_OPENNI_CIRCLE_BUFFER)

        print('-' * 21)
        CAP_PROP_OPENNI_FOCAL_LENGTH = videocapture.get(cv2.CAP_PROP_OPENNI_FOCAL_LENGTH)
        print('CAP_PROP_OPENNI_FOCAL_LENGTH %s' % CAP_PROP_OPENNI_FOCAL_LENGTH)

        print('-' * 21)
        CAP_PROP_OPENNI_FRAME_MAX_DEPTH = videocapture.get(cv2.CAP_PROP_OPENNI_FRAME_MAX_DEPTH)
        print('CAP_PROP_OPENNI_FRAME_MAX_DEPTH %s' % CAP_PROP_OPENNI_FRAME_MAX_DEPTH)

        print('-' * 21)
        CAP_PROP_OPENNI_GENERATOR_PRESENT = videocapture.get(cv2.CAP_PROP_OPENNI_GENERATOR_PRESENT)
        print('CAP_PROP_OPENNI_GENERATOR_PRESENT %s' % CAP_PROP_OPENNI_GENERATOR_PRESENT)

        print('-' * 21)
        CAP_PROP_OPENNI_MAX_BUFFER_SIZE = videocapture.get(cv2.CAP_PROP_OPENNI_MAX_BUFFER_SIZE)
        print('CAP_PROP_OPENNI_MAX_BUFFER_SIZE %s' % CAP_PROP_OPENNI_MAX_BUFFER_SIZE)

        print('-' * 21)
        CAP_PROP_OPENNI_MAX_TIME_DURATION = videocapture.get(cv2.CAP_PROP_OPENNI_MAX_TIME_DURATION)
        print('CAP_PROP_OPENNI_MAX_TIME_DURATION %s' % CAP_PROP_OPENNI_MAX_TIME_DURATION)

        print('-' * 21)
        CAP_PROP_OPENNI_OUTPUT_MODE = videocapture.get(cv2.CAP_PROP_OPENNI_OUTPUT_MODE)
        print('CAP_PROP_OPENNI_OUTPUT_MODE %s' % CAP_PROP_OPENNI_OUTPUT_MODE)

        print('-' * 21)
        CAP_PROP_OPENNI_REGISTRATION = videocapture.get(cv2.CAP_PROP_OPENNI_REGISTRATION)
        print('CAP_PROP_OPENNI_REGISTRATION %s' % CAP_PROP_OPENNI_REGISTRATION)

        print('-' * 21)
        CAP_PROP_OPENNI_REGISTRATION_ON = videocapture.get(cv2.CAP_PROP_OPENNI_REGISTRATION_ON)
        print('CAP_PROP_OPENNI_REGISTRATION_ON %s' % CAP_PROP_OPENNI_REGISTRATION_ON)

        print('-' * 21)
        CAP_PROP_PAN = videocapture.get(cv2.CAP_PROP_PAN)
        print('CAP_PROP_PAN %s' % CAP_PROP_PAN)

        print('-' * 21)
        CAP_PROP_POS_AVI_RATIO = videocapture.get(cv2.CAP_PROP_POS_AVI_RATIO)
        print('CAP_PROP_POS_AVI_RATIO %s' % CAP_PROP_POS_AVI_RATIO)

        print('-' * 21)
        CAP_PROP_POS_FRAMES = videocapture.get(cv2.CAP_PROP_POS_FRAMES)
        print('CAP_PROP_POS_FRAMES %s' % CAP_PROP_POS_FRAMES)

        CAP_PROP_POS_MSEC = videocapture.get(cv2.CAP_PROP_POS_MSEC)
        print('CAP_PROP_POS_MSEC %s' % CAP_PROP_POS_MSEC)

        print('-' * 21)
        CAP_PROP_PVAPI_BINNINGX = videocapture.get(cv2.CAP_PROP_PVAPI_BINNINGX)
        print('CAP_PROP_PVAPI_BINNINGX %s' % CAP_PROP_PVAPI_BINNINGX)

        CAP_PROP_PVAPI_BINNINGY = videocapture.get(cv2.CAP_PROP_PVAPI_BINNINGY)
        print('CAP_PROP_PVAPI_BINNINGY %s' % CAP_PROP_PVAPI_BINNINGY)

        CAP_PROP_PVAPI_DECIMATIONHORIZONTAL = videocapture.get(cv2.CAP_PROP_PVAPI_DECIMATIONHORIZONTAL)
        print('CAP_PROP_PVAPI_DECIMATIONHORIZONTAL %s' % CAP_PROP_PVAPI_DECIMATIONHORIZONTAL)

        CAP_PROP_PVAPI_DECIMATIONVERTICAL = videocapture.get(cv2.CAP_PROP_PVAPI_DECIMATIONVERTICAL)
        print('CAP_PROP_PVAPI_DECIMATIONVERTICAL %s' % CAP_PROP_PVAPI_DECIMATIONVERTICAL)

        CAP_PROP_PVAPI_FRAMESTARTTRIGGERMODE = videocapture.get(cv2.CAP_PROP_PVAPI_FRAMESTARTTRIGGERMODE)
        print('CAP_PROP_PVAPI_FRAMESTARTTRIGGERMODE %s' % CAP_PROP_PVAPI_FRAMESTARTTRIGGERMODE)

        CAP_PROP_PVAPI_MULTICASTIP = videocapture.get(cv2.CAP_PROP_PVAPI_MULTICASTIP)
        print('CAP_PROP_PVAPI_MULTICASTIP %s' % CAP_PROP_PVAPI_MULTICASTIP)

        CAP_PROP_PVAPI_PIXELFORMAT = videocapture.get(cv2.CAP_PROP_PVAPI_PIXELFORMAT)
        print('CAP_PROP_PVAPI_PIXELFORMAT %s' % CAP_PROP_PVAPI_PIXELFORMAT)

        print('-' * 21)
        CAP_PROP_RECTIFICATION = videocapture.get(cv2.CAP_PROP_RECTIFICATION)
        print('CAP_PROP_RECTIFICATION %s' % CAP_PROP_RECTIFICATION)

        CAP_PROP_ROLL = videocapture.get(cv2.CAP_PROP_ROLL)
        print('CAP_PROP_ROLL %s' % CAP_PROP_ROLL)

        CAP_PROP_SATURATION = videocapture.get(cv2.CAP_PROP_SATURATION)
        print('CAP_PROP_SATURATION %s' % CAP_PROP_SATURATION)

        CAP_PROP_SETTINGS = videocapture.get(cv2.CAP_PROP_SETTINGS)
        print('CAP_PROP_SETTINGS %s' % CAP_PROP_SETTINGS)

        CAP_PROP_SHARPNESS = videocapture.get(cv2.CAP_PROP_SHARPNESS)
        print('CAP_PROP_SHARPNESS %s' % CAP_PROP_SHARPNESS)

        CAP_PROP_SPEED = videocapture.get(cv2.CAP_PROP_SPEED)
        print('CAP_PROP_SPEED %s' % CAP_PROP_SPEED)

        CAP_PROP_TEMPERATURE = videocapture.get(cv2.CAP_PROP_TEMPERATURE)
        print('CAP_PROP_TEMPERATURE %s' % CAP_PROP_TEMPERATURE)

        CAP_PROP_TILT = videocapture.get(cv2.CAP_PROP_TILT)
        print('CAP_PROP_TILT %s' % CAP_PROP_TILT)

        CAP_PROP_TRIGGER = videocapture.get(cv2.CAP_PROP_TRIGGER)
        print('CAP_PROP_TRIGGER %s' % CAP_PROP_TRIGGER)

        print('-' * 21)
        CAP_PROP_TRIGGER_DELAY = videocapture.get(cv2.CAP_PROP_TRIGGER_DELAY)
        print('CAP_PROP_TRIGGER_DELAY %s' % CAP_PROP_TRIGGER_DELAY)

        print('-' * 21)
        CAP_PROP_VIEWFINDER = videocapture.get(cv2.CAP_PROP_VIEWFINDER)
        print('CAP_PROP_VIEWFINDER %s' % CAP_PROP_VIEWFINDER)

        print('-' * 21)
        CAP_PROP_WHITE_BALANCE_BLUE_U = videocapture.get(cv2.CAP_PROP_WHITE_BALANCE_BLUE_U)
        print('CAP_PROP_WHITE_BALANCE_BLUE_U %s' % CAP_PROP_WHITE_BALANCE_BLUE_U)

        print('-' * 21)
        CAP_PROP_WHITE_BALANCE_RED_V = videocapture.get(cv2.CAP_PROP_WHITE_BALANCE_RED_V)
        print('CAP_PROP_WHITE_BALANCE_RED_V %s' % CAP_PROP_WHITE_BALANCE_RED_V)

        print('-' * 21)
        CAP_PROP_XI_ACQ_BUFFER_SIZE = videocapture.get(cv2.CAP_PROP_XI_ACQ_BUFFER_SIZE)
        print('CAP_PROP_XI_ACQ_BUFFER_SIZE %s' % CAP_PROP_XI_ACQ_BUFFER_SIZE)

        print('-' * 21)
        CAP_PROP_XI_ACQ_BUFFER_SIZE_UNIT = videocapture.get(cv2.CAP_PROP_XI_ACQ_BUFFER_SIZE_UNIT)
        print('CAP_PROP_XI_ACQ_BUFFER_SIZE_UNIT %s' % CAP_PROP_XI_ACQ_BUFFER_SIZE_UNIT)

        print('-' * 21)
        CAP_PROP_XI_ACQ_FRAME_BURST_COUNT = videocapture.get(cv2.CAP_PROP_XI_ACQ_FRAME_BURST_COUNT)
        print('CAP_PROP_XI_ACQ_FRAME_BURST_COUNT %s' % CAP_PROP_XI_ACQ_FRAME_BURST_COUNT)

        print('-' * 21)
        CAP_PROP_XI_ACQ_TIMING_MODE = videocapture.get(cv2.CAP_PROP_XI_ACQ_TIMING_MODE)
        print('CAP_PROP_XI_ACQ_TIMING_MODE %s' % CAP_PROP_XI_ACQ_TIMING_MODE)

        print('-' * 21)
        CAP_PROP_XI_ACQ_TRANSPORT_BUFFER_COMMIT = videocapture.get(cv2.CAP_PROP_XI_ACQ_TRANSPORT_BUFFER_COMMIT)
        print('CAP_PROP_XI_ACQ_TRANSPORT_BUFFER_COMMIT %s' % CAP_PROP_XI_ACQ_TRANSPORT_BUFFER_COMMIT)

        CAP_PROP_XI_ACQ_TRANSPORT_BUFFER_SIZE = videocapture.get(cv2.CAP_PROP_XI_ACQ_TRANSPORT_BUFFER_SIZE)
        print('CAP_PROP_XI_ACQ_TRANSPORT_BUFFER_SIZE %s' % CAP_PROP_XI_ACQ_TRANSPORT_BUFFER_SIZE)

        print('-' * 21)
        CAP_PROP_XI_AEAG = videocapture.get(cv2.CAP_PROP_XI_AEAG)
        print('CAP_PROP_XI_AEAG %s' % CAP_PROP_XI_AEAG)

        print('-' * 21)
        CAP_PROP_XI_AEAG_LEVEL = videocapture.get(cv2.CAP_PROP_XI_AEAG_LEVEL)
        print('CAP_PROP_XI_AEAG_LEVEL %s' % CAP_PROP_XI_AEAG_LEVEL)

        print('-' * 21)
        CAP_PROP_XI_AEAG_ROI_HEIGHT = videocapture.get(cv2.CAP_PROP_XI_AEAG_ROI_HEIGHT)
        print('CAP_PROP_XI_AEAG_ROI_HEIGHT %s' % CAP_PROP_XI_AEAG_ROI_HEIGHT)

        print('-' * 21)
        CAP_PROP_XI_AEAG_ROI_OFFSET_X = videocapture.get(cv2.CAP_PROP_XI_AEAG_ROI_OFFSET_X)
        print('CAP_PROP_XI_AEAG_ROI_OFFSET_X %s' % CAP_PROP_XI_AEAG_ROI_OFFSET_X)

        CAP_PROP_XI_AEAG_ROI_OFFSET_Y = videocapture.get(cv2.CAP_PROP_XI_AEAG_ROI_OFFSET_Y)
        print('CAP_PROP_XI_AEAG_ROI_OFFSET_Y %s' % CAP_PROP_XI_AEAG_ROI_OFFSET_Y)

        print('-' * 21)
        CAP_PROP_XI_AEAG_ROI_WIDTH = videocapture.get(cv2.CAP_PROP_XI_AEAG_ROI_WIDTH)
        print('CAP_PROP_XI_AEAG_ROI_WIDTH %s' % CAP_PROP_XI_AEAG_ROI_WIDTH)

        print('-' * 21)
        CAP_PROP_XI_AE_MAX_LIMIT = videocapture.get(cv2.CAP_PROP_XI_AE_MAX_LIMIT)
        print('CAP_PROP_XI_AE_MAX_LIMIT %s' % CAP_PROP_XI_AE_MAX_LIMIT)

        print('-' * 21)
        CAP_PROP_XI_AG_MAX_LIMIT = videocapture.get(cv2.CAP_PROP_XI_AG_MAX_LIMIT)
        print('CAP_PROP_XI_AG_MAX_LIMIT %s' % CAP_PROP_XI_AG_MAX_LIMIT)

        print('-' * 21)
        CAP_PROP_XI_APPLY_CMS = videocapture.get(cv2.CAP_PROP_XI_APPLY_CMS)
        print('CAP_PROP_XI_APPLY_CMS %s' % CAP_PROP_XI_APPLY_CMS)

        print('-' * 21)
        CAP_PROP_XI_AUTO_BANDWIDTH_CALCULATION = videocapture.get(cv2.CAP_PROP_XI_AUTO_BANDWIDTH_CALCULATION)
        print('CAP_PROP_XI_AUTO_BANDWIDTH_CALCULATION %s' % CAP_PROP_XI_AUTO_BANDWIDTH_CALCULATION)

        print('-' * 21)
        CAP_PROP_XI_AUTO_WB = videocapture.get(cv2.CAP_PROP_XI_AUTO_WB)
        print('CAP_PROP_XI_AUTO_WB %s' % CAP_PROP_XI_AUTO_WB)

        print('-' * 21)
        CAP_PROP_XI_AVAILABLE_BANDWIDTH = videocapture.get(cv2.CAP_PROP_XI_AVAILABLE_BANDWIDTH)
        print('CAP_PROP_XI_AVAILABLE_BANDWIDTH %s' % CAP_PROP_XI_AVAILABLE_BANDWIDTH)

        print('-' * 21)
        CAP_PROP_XI_BINNING_HORIZONTAL = videocapture.get(cv2.CAP_PROP_XI_BINNING_HORIZONTAL)
        print('CAP_PROP_XI_BINNING_HORIZONTAL %s' % CAP_PROP_XI_BINNING_HORIZONTAL)

        CAP_PROP_XI_BINNING_PATTERN = videocapture.get(cv2.CAP_PROP_XI_BINNING_PATTERN)
        print('CAP_PROP_XI_BINNING_PATTERN %s' % CAP_PROP_XI_BINNING_PATTERN)

        CAP_PROP_XI_BINNING_SELECTOR = videocapture.get(cv2.CAP_PROP_XI_BINNING_SELECTOR)
        print('CAP_PROP_XI_BINNING_SELECTOR %s' % CAP_PROP_XI_BINNING_SELECTOR)

        CAP_PROP_XI_BINNING_VERTICAL = videocapture.get(cv2.CAP_PROP_XI_BINNING_VERTICAL)
        print('CAP_PROP_XI_BINNING_VERTICAL %s' % CAP_PROP_XI_BINNING_VERTICAL)

        print('-' * 21)
        CAP_PROP_XI_BPC = videocapture.get(cv2.CAP_PROP_XI_BPC)
        print('CAP_PROP_XI_BPC %s' % CAP_PROP_XI_BPC)

        print('-' * 21)
        CAP_PROP_XI_BUFFERS_QUEUE_SIZE = videocapture.get(cv2.CAP_PROP_XI_BUFFERS_QUEUE_SIZE)
        print('CAP_PROP_XI_BUFFERS_QUEUE_SIZE %s' % CAP_PROP_XI_BUFFERS_QUEUE_SIZE)

        print('-' * 21)
        CAP_PROP_XI_BUFFER_POLICY = videocapture.get(cv2.CAP_PROP_XI_BUFFER_POLICY)
        print('CAP_PROP_XI_BUFFER_POLICY %s' % CAP_PROP_XI_BUFFER_POLICY)

        print('-' * 21)
        CAP_PROP_XI_CC_MATRIX_00 = videocapture.get(cv2.CAP_PROP_XI_CC_MATRIX_00)
        print('CAP_PROP_XI_CC_MATRIX_00 %s' % CAP_PROP_XI_CC_MATRIX_00)

        CAP_PROP_XI_CC_MATRIX_01 = videocapture.get(cv2.CAP_PROP_XI_CC_MATRIX_01)
        print('CAP_PROP_XI_CC_MATRIX_01 %s' % CAP_PROP_XI_CC_MATRIX_01)

        CAP_PROP_XI_CC_MATRIX_02 = videocapture.get(cv2.CAP_PROP_XI_CC_MATRIX_02)
        print('CAP_PROP_XI_CC_MATRIX_02 %s' % CAP_PROP_XI_CC_MATRIX_02)

        CAP_PROP_XI_CC_MATRIX_03 = videocapture.get(cv2.CAP_PROP_XI_CC_MATRIX_03)
        print('CAP_PROP_XI_CC_MATRIX_03 %s' % CAP_PROP_XI_CC_MATRIX_03)

        CAP_PROP_XI_CC_MATRIX_10 = videocapture.get(cv2.CAP_PROP_XI_CC_MATRIX_10)
        print('CAP_PROP_XI_CC_MATRIX_10 %s' % CAP_PROP_XI_CC_MATRIX_10)

        CAP_PROP_XI_CC_MATRIX_11 = videocapture.get(cv2.CAP_PROP_XI_CC_MATRIX_11)
        print('CAP_PROP_XI_CC_MATRIX_11 %s' % CAP_PROP_XI_CC_MATRIX_11)

        CAP_PROP_XI_CC_MATRIX_12 = videocapture.get(cv2.CAP_PROP_XI_CC_MATRIX_12)
        print('CAP_PROP_XI_CC_MATRIX_12 %s' % CAP_PROP_XI_CC_MATRIX_12)

        CAP_PROP_XI_CC_MATRIX_13 = videocapture.get(cv2.CAP_PROP_XI_CC_MATRIX_13)
        print('CAP_PROP_XI_CC_MATRIX_13 %s' % CAP_PROP_XI_CC_MATRIX_13)

        CAP_PROP_XI_CC_MATRIX_20 = videocapture.get(cv2.CAP_PROP_XI_CC_MATRIX_20)
        print('CAP_PROP_XI_CC_MATRIX_20 %s' % CAP_PROP_XI_CC_MATRIX_20)

        CAP_PROP_XI_CC_MATRIX_21 = videocapture.get(cv2.CAP_PROP_XI_CC_MATRIX_21)
        print('CAP_PROP_XI_CC_MATRIX_21 %s' % CAP_PROP_XI_CC_MATRIX_21)

        CAP_PROP_XI_CC_MATRIX_22 = videocapture.get(cv2.CAP_PROP_XI_CC_MATRIX_22)
        print('CAP_PROP_XI_CC_MATRIX_22 %s' % CAP_PROP_XI_CC_MATRIX_22)

        CAP_PROP_XI_CC_MATRIX_23 = videocapture.get(cv2.CAP_PROP_XI_CC_MATRIX_23)
        print('CAP_PROP_XI_CC_MATRIX_23 %s' % CAP_PROP_XI_CC_MATRIX_23)

        CAP_PROP_XI_CC_MATRIX_30 = videocapture.get(cv2.CAP_PROP_XI_CC_MATRIX_30)
        print('CAP_PROP_XI_CC_MATRIX_30 %s' % CAP_PROP_XI_CC_MATRIX_30)

        CAP_PROP_XI_CC_MATRIX_31 = videocapture.get(cv2.CAP_PROP_XI_CC_MATRIX_31)
        print('CAP_PROP_XI_CC_MATRIX_31 %s' % CAP_PROP_XI_CC_MATRIX_31)

        CAP_PROP_XI_CC_MATRIX_32 = videocapture.get(cv2.CAP_PROP_XI_CC_MATRIX_32)
        print('CAP_PROP_XI_CC_MATRIX_32 %s' % CAP_PROP_XI_CC_MATRIX_32)

        CAP_PROP_XI_CC_MATRIX_33 = videocapture.get(cv2.CAP_PROP_XI_CC_MATRIX_33)
        print('CAP_PROP_XI_CC_MATRIX_33 %s' % CAP_PROP_XI_CC_MATRIX_33)

        print('-' * 21)
        CAP_PROP_XI_CHIP_TEMP = videocapture.get(cv2.CAP_PROP_XI_CHIP_TEMP)
        print('CAP_PROP_XI_CHIP_TEMP %s' % CAP_PROP_XI_CHIP_TEMP)

        print('-' * 21)
        CAP_PROP_XI_CMS = videocapture.get(cv2.CAP_PROP_XI_CMS)
        print('CAP_PROP_XI_CMS %s' % CAP_PROP_XI_CMS)

        print('-' * 21)
        CAP_PROP_XI_COLOR_FILTER_ARRAY = videocapture.get(cv2.CAP_PROP_XI_COLOR_FILTER_ARRAY)
        print('CAP_PROP_XI_COLOR_FILTER_ARRAY %s' % CAP_PROP_XI_COLOR_FILTER_ARRAY)

        print('-' * 21)
        CAP_PROP_XI_COLUMN_FPN_CORRECTION = videocapture.get(cv2.CAP_PROP_XI_COLUMN_FPN_CORRECTION)
        print('CAP_PROP_XI_COLUMN_FPN_CORRECTION %s' % CAP_PROP_XI_COLUMN_FPN_CORRECTION)

        print('-' * 21)
        CAP_PROP_XI_COOLING = videocapture.get(cv2.CAP_PROP_XI_COOLING)
        print('CAP_PROP_XI_COOLING %s' % CAP_PROP_XI_COOLING)

        print('-' * 21)
        CAP_PROP_XI_COUNTER_SELECTOR = videocapture.get(cv2.CAP_PROP_XI_COUNTER_SELECTOR)
        print('CAP_PROP_XI_COUNTER_SELECTOR %s' % CAP_PROP_XI_COUNTER_SELECTOR)

        CAP_PROP_XI_COUNTER_VALUE = videocapture.get(cv2.CAP_PROP_XI_COUNTER_VALUE)
        print('CAP_PROP_XI_COUNTER_VALUE %s' % CAP_PROP_XI_COUNTER_VALUE)

        print('-' * 21)
        CAP_PROP_XI_DATA_FORMAT = videocapture.get(cv2.CAP_PROP_XI_DATA_FORMAT)
        print('CAP_PROP_XI_DATA_FORMAT %s' % CAP_PROP_XI_DATA_FORMAT)

        print('-' * 21)
        CAP_PROP_XI_DEBOUNCE_EN = videocapture.get(cv2.CAP_PROP_XI_DEBOUNCE_EN)
        print('CAP_PROP_XI_DEBOUNCE_EN %s' % CAP_PROP_XI_DEBOUNCE_EN)

        CAP_PROP_XI_DEBOUNCE_POL = videocapture.get(cv2.CAP_PROP_XI_DEBOUNCE_POL)
        print('CAP_PROP_XI_DEBOUNCE_POL %s' % CAP_PROP_XI_DEBOUNCE_POL)

        CAP_PROP_XI_DEBOUNCE_T0 = videocapture.get(cv2.CAP_PROP_XI_DEBOUNCE_T0)
        print('CAP_PROP_XI_DEBOUNCE_T0 %s' % CAP_PROP_XI_DEBOUNCE_T0)

        CAP_PROP_XI_DEBOUNCE_T1 = videocapture.get(cv2.CAP_PROP_XI_DEBOUNCE_T1)
        print('CAP_PROP_XI_DEBOUNCE_T1 %s' % CAP_PROP_XI_DEBOUNCE_T1)

        print('-' * 21)
        CAP_PROP_XI_DEBUG_LEVEL = videocapture.get(cv2.CAP_PROP_XI_DEBUG_LEVEL)
        print('CAP_PROP_XI_DEBUG_LEVEL %s' % CAP_PROP_XI_DEBUG_LEVEL)

        print('-' * 21)
        CAP_PROP_XI_DECIMATION_HORIZONTAL = videocapture.get(cv2.CAP_PROP_XI_DECIMATION_HORIZONTAL)
        print('CAP_PROP_XI_DECIMATION_HORIZONTAL %s' % CAP_PROP_XI_DECIMATION_HORIZONTAL)

        CAP_PROP_XI_DECIMATION_PATTERN = videocapture.get(cv2.CAP_PROP_XI_DECIMATION_PATTERN)
        print('CAP_PROP_XI_DECIMATION_PATTERN %s' % CAP_PROP_XI_DECIMATION_PATTERN)

        CAP_PROP_XI_DECIMATION_SELECTOR = videocapture.get(cv2.CAP_PROP_XI_DECIMATION_SELECTOR)
        print('CAP_PROP_XI_DECIMATION_SELECTOR %s' % CAP_PROP_XI_DECIMATION_SELECTOR)

        CAP_PROP_XI_DECIMATION_VERTICAL = videocapture.get(cv2.CAP_PROP_XI_DECIMATION_VERTICAL)
        print('CAP_PROP_XI_DECIMATION_VERTICAL %s' % CAP_PROP_XI_DECIMATION_VERTICAL)

        print('-' * 21)
        CAP_PROP_XI_DEFAULT_CC_MATRIX = videocapture.get(cv2.CAP_PROP_XI_DEFAULT_CC_MATRIX)
        print('CAP_PROP_XI_DEFAULT_CC_MATRIX %s' % CAP_PROP_XI_DEFAULT_CC_MATRIX)

        print('-' * 21)
        CAP_PROP_XI_DEVICE_MODEL_ID = videocapture.get(cv2.CAP_PROP_XI_DEVICE_MODEL_ID)
        print('CAP_PROP_XI_DEVICE_MODEL_ID %s' % CAP_PROP_XI_DEVICE_MODEL_ID)

        print('-' * 21)
        CAP_PROP_XI_DEVICE_RESET = videocapture.get(cv2.CAP_PROP_XI_DEVICE_RESET)
        print('CAP_PROP_XI_DEVICE_RESET %s' % CAP_PROP_XI_DEVICE_RESET)

        CAP_PROP_XI_DEVICE_SN = videocapture.get(cv2.CAP_PROP_XI_DEVICE_SN)
        print('CAP_PROP_XI_DEVICE_SN %s' % CAP_PROP_XI_DEVICE_SN)

        print('-' * 21)
        CAP_PROP_XI_DOWNSAMPLING = videocapture.get(cv2.CAP_PROP_XI_DOWNSAMPLING)
        print('CAP_PROP_XI_DOWNSAMPLING %s' % CAP_PROP_XI_DOWNSAMPLING)

        print('-' * 21)
        CAP_PROP_XI_DOWNSAMPLING_TYPE = videocapture.get(cv2.CAP_PROP_XI_DOWNSAMPLING_TYPE)
        print('CAP_PROP_XI_DOWNSAMPLING_TYPE %s' % CAP_PROP_XI_DOWNSAMPLING_TYPE)

        print('-' * 21)
        CAP_PROP_XI_EXPOSURE = videocapture.get(cv2.CAP_PROP_XI_EXPOSURE)
        print('CAP_PROP_XI_EXPOSURE %s' % CAP_PROP_XI_EXPOSURE)

        print('-' * 21)
        CAP_PROP_XI_EXPOSURE_BURST_COUNT = videocapture.get(cv2.CAP_PROP_XI_EXPOSURE_BURST_COUNT)
        print('CAP_PROP_XI_EXPOSURE_BURST_COUNT %s' % CAP_PROP_XI_EXPOSURE_BURST_COUNT)

        print('-' * 21)
        CAP_PROP_XI_EXP_PRIORITY = videocapture.get(cv2.CAP_PROP_XI_EXP_PRIORITY)
        print('CAP_PROP_XI_EXP_PRIORITY %s' % CAP_PROP_XI_EXP_PRIORITY)

        print('-' * 21)
        CAP_PROP_XI_FFS_ACCESS_KEY = videocapture.get(cv2.CAP_PROP_XI_FFS_ACCESS_KEY)
        print('CAP_PROP_XI_FFS_ACCESS_KEY %s' % CAP_PROP_XI_FFS_ACCESS_KEY)

        print('-' * 21)
        CAP_PROP_XI_FFS_FILE_ID = videocapture.get(cv2.CAP_PROP_XI_FFS_FILE_ID)
        print('CAP_PROP_XI_FFS_FILE_ID %s' % CAP_PROP_XI_FFS_FILE_ID)

        CAP_PROP_XI_FFS_FILE_SIZE = videocapture.get(cv2.CAP_PROP_XI_FFS_FILE_SIZE)
        print('CAP_PROP_XI_FFS_FILE_SIZE %s' % CAP_PROP_XI_FFS_FILE_SIZE)

        print('-' * 21)
        CAP_PROP_XI_FRAMERATE = videocapture.get(cv2.CAP_PROP_XI_FRAMERATE)
        print('CAP_PROP_XI_FRAMERATE %s' % CAP_PROP_XI_FRAMERATE)

        print('-' * 21)
        CAP_PROP_XI_FREE_FFS_SIZE = videocapture.get(cv2.CAP_PROP_XI_FREE_FFS_SIZE)
        print('CAP_PROP_XI_FREE_FFS_SIZE %s' % CAP_PROP_XI_FREE_FFS_SIZE)

        print('-' * 21)
        CAP_PROP_XI_GAIN = videocapture.get(cv2.CAP_PROP_XI_GAIN)
        print('CAP_PROP_XI_GAIN %s' % CAP_PROP_XI_GAIN)

        print('-' * 21)
        CAP_PROP_XI_GAIN_SELECTOR = videocapture.get(cv2.CAP_PROP_XI_GAIN_SELECTOR)
        print('CAP_PROP_XI_GAIN_SELECTOR %s' % CAP_PROP_XI_GAIN_SELECTOR)

        print('-' * 21)
        CAP_PROP_XI_GAMMAC = videocapture.get(cv2.CAP_PROP_XI_GAMMAC)
        print('CAP_PROP_XI_GAMMAC %s' % CAP_PROP_XI_GAMMAC)

        CAP_PROP_XI_GAMMAY = videocapture.get(cv2.CAP_PROP_XI_GAMMAY)
        print('CAP_PROP_XI_GAMMAY %s' % CAP_PROP_XI_GAMMAY)

        print('-' * 21)
        CAP_PROP_XI_GPI_LEVEL = videocapture.get(cv2.CAP_PROP_XI_GPI_LEVEL)
        print('CAP_PROP_XI_GPI_LEVEL %s' % CAP_PROP_XI_GPI_LEVEL)

        CAP_PROP_XI_GPI_MODE = videocapture.get(cv2.CAP_PROP_XI_GPI_MODE)
        print('CAP_PROP_XI_GPI_MODE %s' % CAP_PROP_XI_GPI_MODE)

        CAP_PROP_XI_GPI_SELECTOR = videocapture.get(cv2.CAP_PROP_XI_GPI_SELECTOR)
        print('CAP_PROP_XI_GPI_SELECTOR %s' % CAP_PROP_XI_GPI_SELECTOR)

        print('-' * 21)
        CAP_PROP_XI_GPO_MODE = videocapture.get(cv2.CAP_PROP_XI_GPO_MODE)
        print('CAP_PROP_XI_GPO_MODE %s' % CAP_PROP_XI_GPO_MODE)

        CAP_PROP_XI_GPO_SELECTOR = videocapture.get(cv2.CAP_PROP_XI_GPO_SELECTOR)
        print('CAP_PROP_XI_GPO_SELECTOR %s' % CAP_PROP_XI_GPO_SELECTOR)

        print('-' * 21)
        CAP_PROP_XI_HDR = videocapture.get(cv2.CAP_PROP_XI_HDR)
        print('CAP_PROP_XI_HDR %s' % CAP_PROP_XI_HDR)

        print('-' * 21)
        CAP_PROP_XI_HDR_KNEEPOINT_COUNT = videocapture.get(cv2.CAP_PROP_XI_HDR_KNEEPOINT_COUNT)
        print('CAP_PROP_XI_HDR_KNEEPOINT_COUNT %s' % CAP_PROP_XI_HDR_KNEEPOINT_COUNT)

        print('-' * 21)
        CAP_PROP_XI_HDR_T1 = videocapture.get(cv2.CAP_PROP_XI_HDR_T1)
        print('CAP_PROP_XI_HDR_T1 %s' % CAP_PROP_XI_HDR_T1)

        CAP_PROP_XI_HDR_T2 = videocapture.get(cv2.CAP_PROP_XI_HDR_T2)
        print('CAP_PROP_XI_HDR_T2 %s' % CAP_PROP_XI_HDR_T2)

        print('-' * 21)
        CAP_PROP_XI_HEIGHT = videocapture.get(cv2.CAP_PROP_XI_HEIGHT)
        print('CAP_PROP_XI_HEIGHT %s' % CAP_PROP_XI_HEIGHT)

        print('-' * 21)
        CAP_PROP_XI_HOUS_BACK_SIDE_TEMP = videocapture.get(cv2.CAP_PROP_XI_HOUS_BACK_SIDE_TEMP)
        print('CAP_PROP_XI_HOUS_BACK_SIDE_TEMP %s' % CAP_PROP_XI_HOUS_BACK_SIDE_TEMP)

        print('-' * 21)
        CAP_PROP_XI_HOUS_TEMP = videocapture.get(cv2.CAP_PROP_XI_HOUS_TEMP)
        print('CAP_PROP_XI_HOUS_TEMP %s' % CAP_PROP_XI_HOUS_TEMP)

        print('-' * 21)
        CAP_PROP_XI_HW_REVISION = videocapture.get(cv2.CAP_PROP_XI_HW_REVISION)
        print('CAP_PROP_XI_HW_REVISION %s' % CAP_PROP_XI_HW_REVISION)

        print('-' * 21)
        CAP_PROP_XI_IMAGE_BLACK_LEVEL = videocapture.get(cv2.CAP_PROP_XI_IMAGE_BLACK_LEVEL)
        print('CAP_PROP_XI_IMAGE_BLACK_LEVEL %s' % CAP_PROP_XI_IMAGE_BLACK_LEVEL)

        print('-' * 21)
        CAP_PROP_XI_IMAGE_DATA_BIT_DEPTH = videocapture.get(cv2.CAP_PROP_XI_IMAGE_DATA_BIT_DEPTH)
        print('CAP_PROP_XI_IMAGE_DATA_BIT_DEPTH %s' % CAP_PROP_XI_IMAGE_DATA_BIT_DEPTH)

        print('-' * 21)
        CAP_PROP_XI_IMAGE_DATA_FORMAT = videocapture.get(cv2.CAP_PROP_XI_IMAGE_DATA_FORMAT)
        print('CAP_PROP_XI_IMAGE_DATA_FORMAT %s' % CAP_PROP_XI_IMAGE_DATA_FORMAT)

        print('-' * 21)
        CAP_PROP_XI_IMAGE_DATA_FORMAT_RGB32_ALPHA = videocapture.get(cv2.CAP_PROP_XI_IMAGE_DATA_FORMAT_RGB32_ALPHA)
        print('CAP_PROP_XI_IMAGE_DATA_FORMAT_RGB32_ALPHA %s' % CAP_PROP_XI_IMAGE_DATA_FORMAT_RGB32_ALPHA)

        print('-' * 21)
        CAP_PROP_XI_IMAGE_IS_COLOR = videocapture.get(cv2.CAP_PROP_XI_IMAGE_IS_COLOR)
        print('CAP_PROP_XI_IMAGE_IS_COLOR %s' % CAP_PROP_XI_IMAGE_IS_COLOR)

        print('-' * 21)
        CAP_PROP_XI_IMAGE_PAYLOAD_SIZE = videocapture.get(cv2.CAP_PROP_XI_IMAGE_PAYLOAD_SIZE)
        print('CAP_PROP_XI_IMAGE_PAYLOAD_SIZE %s' % CAP_PROP_XI_IMAGE_PAYLOAD_SIZE)

        print('-' * 21)
        CAP_PROP_XI_IS_COOLED = videocapture.get(cv2.CAP_PROP_XI_IS_COOLED)
        print('CAP_PROP_XI_IS_COOLED %s' % CAP_PROP_XI_IS_COOLED)

        print('-' * 21)
        CAP_PROP_XI_IS_DEVICE_EXIST = videocapture.get(cv2.CAP_PROP_XI_IS_DEVICE_EXIST)
        print('CAP_PROP_XI_IS_DEVICE_EXIST %s' % CAP_PROP_XI_IS_DEVICE_EXIST)

        print('-' * 21)
        CAP_PROP_XI_KNEEPOINT1 = videocapture.get(cv2.CAP_PROP_XI_KNEEPOINT1)
        print('CAP_PROP_XI_KNEEPOINT1 %s' % CAP_PROP_XI_KNEEPOINT1)

        CAP_PROP_XI_KNEEPOINT2 = videocapture.get(cv2.CAP_PROP_XI_KNEEPOINT2)
        print('CAP_PROP_XI_KNEEPOINT2 %s' % CAP_PROP_XI_KNEEPOINT2)

        print('-' * 21)
        CAP_PROP_XI_LED_MODE = videocapture.get(cv2.CAP_PROP_XI_LED_MODE)
        print('CAP_PROP_XI_LED_MODE %s' % CAP_PROP_XI_LED_MODE)

        CAP_PROP_XI_LED_SELECTOR = videocapture.get(cv2.CAP_PROP_XI_LED_SELECTOR)
        print('CAP_PROP_XI_LED_SELECTOR %s' % CAP_PROP_XI_LED_SELECTOR)

        print('-' * 21)
        CAP_PROP_XI_LENS_APERTURE_VALUE = videocapture.get(cv2.CAP_PROP_XI_LENS_APERTURE_VALUE)
        print('CAP_PROP_XI_LENS_APERTURE_VALUE %s' % CAP_PROP_XI_LENS_APERTURE_VALUE)

        print('-' * 21)
        CAP_PROP_XI_LENS_FEATURE = videocapture.get(cv2.CAP_PROP_XI_LENS_FEATURE)
        print('CAP_PROP_XI_LENS_FEATURE %s' % CAP_PROP_XI_LENS_FEATURE)

        print('-' * 21)
        CAP_PROP_XI_LENS_FEATURE_SELECTOR = videocapture.get(cv2.CAP_PROP_XI_LENS_FEATURE_SELECTOR)
        print('CAP_PROP_XI_LENS_FEATURE_SELECTOR %s' % CAP_PROP_XI_LENS_FEATURE_SELECTOR)

        print('-' * 21)
        CAP_PROP_XI_LENS_FOCAL_LENGTH = videocapture.get(cv2.CAP_PROP_XI_LENS_FOCAL_LENGTH)
        print('CAP_PROP_XI_LENS_FOCAL_LENGTH %s' % CAP_PROP_XI_LENS_FOCAL_LENGTH)

        print('-' * 21)
        CAP_PROP_XI_LENS_FOCUS_DISTANCE = videocapture.get(cv2.CAP_PROP_XI_LENS_FOCUS_DISTANCE)
        print('CAP_PROP_XI_LENS_FOCUS_DISTANCE %s' % CAP_PROP_XI_LENS_FOCUS_DISTANCE)

        CAP_PROP_XI_LENS_FOCUS_MOVE = videocapture.get(cv2.CAP_PROP_XI_LENS_FOCUS_MOVE)
        print('CAP_PROP_XI_LENS_FOCUS_MOVE %s' % CAP_PROP_XI_LENS_FOCUS_MOVE)

        print('-' * 21)
        CAP_PROP_XI_LENS_FOCUS_MOVEMENT_VALUE = videocapture.get(cv2.CAP_PROP_XI_LENS_FOCUS_MOVEMENT_VALUE)
        print('CAP_PROP_XI_LENS_FOCUS_MOVEMENT_VALUE %s' % CAP_PROP_XI_LENS_FOCUS_MOVEMENT_VALUE)

        print('-' * 21)
        CAP_PROP_XI_LENS_MODE = videocapture.get(cv2.CAP_PROP_XI_LENS_MODE)
        print('CAP_PROP_XI_LENS_MODE %s' % CAP_PROP_XI_LENS_MODE)

        print('-' * 21)
        CAP_PROP_XI_LIMIT_BANDWIDTH = videocapture.get(cv2.CAP_PROP_XI_LIMIT_BANDWIDTH)
        print('CAP_PROP_XI_LIMIT_BANDWIDTH %s' % CAP_PROP_XI_LIMIT_BANDWIDTH)

        print('-' * 21)
        CAP_PROP_XI_LUT_EN = videocapture.get(cv2.CAP_PROP_XI_LUT_EN)
        print('CAP_PROP_XI_LUT_EN %s' % CAP_PROP_XI_LUT_EN)

        CAP_PROP_XI_LUT_INDEX = videocapture.get(cv2.CAP_PROP_XI_LUT_INDEX)
        print('CAP_PROP_XI_LUT_INDEX %s' % CAP_PROP_XI_LUT_INDEX)

        CAP_PROP_XI_LUT_VALUE = videocapture.get(cv2.CAP_PROP_XI_LUT_VALUE)
        print('CAP_PROP_XI_LUT_VALUE %s' % CAP_PROP_XI_LUT_VALUE)

        print('-' * 21)
        CAP_PROP_XI_MANUAL_WB = videocapture.get(cv2.CAP_PROP_XI_MANUAL_WB)
        print('CAP_PROP_XI_MANUAL_WB %s' % CAP_PROP_XI_MANUAL_WB)

        print('-' * 21)
        CAP_PROP_XI_OFFSET_X = videocapture.get(cv2.CAP_PROP_XI_OFFSET_X)
        print('CAP_PROP_XI_OFFSET_X %s' % CAP_PROP_XI_OFFSET_X)

        CAP_PROP_XI_OFFSET_Y = videocapture.get(cv2.CAP_PROP_XI_OFFSET_Y)
        print('CAP_PROP_XI_OFFSET_Y %s' % CAP_PROP_XI_OFFSET_Y)

        print('-' * 21)
        CAP_PROP_XI_OUTPUT_DATA_BIT_DEPTH = videocapture.get(cv2.CAP_PROP_XI_OUTPUT_DATA_BIT_DEPTH)
        print('CAP_PROP_XI_OUTPUT_DATA_BIT_DEPTH %s' % CAP_PROP_XI_OUTPUT_DATA_BIT_DEPTH)

        print('-' * 21)
        CAP_PROP_XI_OUTPUT_DATA_PACKING = videocapture.get(cv2.CAP_PROP_XI_OUTPUT_DATA_PACKING)
        print('CAP_PROP_XI_OUTPUT_DATA_PACKING %s' % CAP_PROP_XI_OUTPUT_DATA_PACKING)

        print('-' * 21)
        CAP_PROP_XI_OUTPUT_DATA_PACKING_TYPE = videocapture.get(cv2.CAP_PROP_XI_OUTPUT_DATA_PACKING_TYPE)
        print('CAP_PROP_XI_OUTPUT_DATA_PACKING_TYPE %s' % CAP_PROP_XI_OUTPUT_DATA_PACKING_TYPE)

        print('-' * 21)
        CAP_PROP_XI_RECENT_FRAME = videocapture.get(cv2.CAP_PROP_XI_RECENT_FRAME)
        print('CAP_PROP_XI_RECENT_FRAME %s' % CAP_PROP_XI_RECENT_FRAME)

        print('-' * 21)
        CAP_PROP_XI_REGION_MODE = videocapture.get(cv2.CAP_PROP_XI_REGION_MODE)
        print('CAP_PROP_XI_REGION_MODE %s' % CAP_PROP_XI_REGION_MODE)

        CAP_PROP_XI_REGION_SELECTOR = videocapture.get(cv2.CAP_PROP_XI_REGION_SELECTOR)
        print('CAP_PROP_XI_REGION_SELECTOR %s' % CAP_PROP_XI_REGION_SELECTOR)

        print('-' * 21)
        CAP_PROP_XI_ROW_FPN_CORRECTION = videocapture.get(cv2.CAP_PROP_XI_ROW_FPN_CORRECTION)
        print('CAP_PROP_XI_ROW_FPN_CORRECTION %s' % CAP_PROP_XI_ROW_FPN_CORRECTION)

        print('-' * 21)
        CAP_PROP_XI_SENSOR_BOARD_TEMP = videocapture.get(cv2.CAP_PROP_XI_SENSOR_BOARD_TEMP)
        print('CAP_PROP_XI_SENSOR_BOARD_TEMP %s' % CAP_PROP_XI_SENSOR_BOARD_TEMP)

        print('-' * 21)
        CAP_PROP_XI_SENSOR_CLOCK_FREQ_HZ = videocapture.get(cv2.CAP_PROP_XI_SENSOR_CLOCK_FREQ_HZ)
        print('CAP_PROP_XI_SENSOR_CLOCK_FREQ_HZ %s' % CAP_PROP_XI_SENSOR_CLOCK_FREQ_HZ)

        CAP_PROP_XI_SENSOR_CLOCK_FREQ_INDEX = videocapture.get(cv2.CAP_PROP_XI_SENSOR_CLOCK_FREQ_INDEX)
        print('CAP_PROP_XI_SENSOR_CLOCK_FREQ_INDEX %s' % CAP_PROP_XI_SENSOR_CLOCK_FREQ_INDEX)

        print('-' * 21)
        CAP_PROP_XI_SENSOR_DATA_BIT_DEPTH = videocapture.get(cv2.CAP_PROP_XI_SENSOR_DATA_BIT_DEPTH)
        print('CAP_PROP_XI_SENSOR_DATA_BIT_DEPTH %s' % CAP_PROP_XI_SENSOR_DATA_BIT_DEPTH)

        print('-' * 21)
        CAP_PROP_XI_SENSOR_FEATURE_SELECTOR = videocapture.get(cv2.CAP_PROP_XI_SENSOR_FEATURE_SELECTOR)
        print('CAP_PROP_XI_SENSOR_FEATURE_SELECTOR %s' % CAP_PROP_XI_SENSOR_FEATURE_SELECTOR)

        CAP_PROP_XI_SENSOR_FEATURE_VALUE = videocapture.get(cv2.CAP_PROP_XI_SENSOR_FEATURE_VALUE)
        print('CAP_PROP_XI_SENSOR_FEATURE_VALUE %s' % CAP_PROP_XI_SENSOR_FEATURE_VALUE)

        print('-' * 21)
        CAP_PROP_XI_SENSOR_MODE = videocapture.get(cv2.CAP_PROP_XI_SENSOR_MODE)
        print('CAP_PROP_XI_SENSOR_MODE %s' % CAP_PROP_XI_SENSOR_MODE)

        print('-' * 21)
        CAP_PROP_XI_SENSOR_OUTPUT_CHANNEL_COUNT = videocapture.get(cv2.CAP_PROP_XI_SENSOR_OUTPUT_CHANNEL_COUNT)
        print('CAP_PROP_XI_SENSOR_OUTPUT_CHANNEL_COUNT %s' % CAP_PROP_XI_SENSOR_OUTPUT_CHANNEL_COUNT)

        print('-' * 21)
        CAP_PROP_XI_SENSOR_TAPS = videocapture.get(cv2.CAP_PROP_XI_SENSOR_TAPS)
        print('CAP_PROP_XI_SENSOR_TAPS %s' % CAP_PROP_XI_SENSOR_TAPS)

        print('-' * 21)
        CAP_PROP_XI_SHARPNESS = videocapture.get(cv2.CAP_PROP_XI_SHARPNESS)
        print('CAP_PROP_XI_SHARPNESS %s' % CAP_PROP_XI_SHARPNESS)

        print('-' * 21)
        CAP_PROP_XI_SHUTTER_TYPE = videocapture.get(cv2.CAP_PROP_XI_SHUTTER_TYPE)
        print('CAP_PROP_XI_SHUTTER_TYPE %s' % CAP_PROP_XI_SHUTTER_TYPE)

        print('-' * 21)
        CAP_PROP_XI_TARGET_TEMP = videocapture.get(cv2.CAP_PROP_XI_TARGET_TEMP)
        print('CAP_PROP_XI_TARGET_TEMP %s' % CAP_PROP_XI_TARGET_TEMP)

        print('-' * 21)
        CAP_PROP_XI_TEST_PATTERN = videocapture.get(cv2.CAP_PROP_XI_TEST_PATTERN)
        print('CAP_PROP_XI_TEST_PATTERN %s' % CAP_PROP_XI_TEST_PATTERN)

        print('-' * 21)
        CAP_PROP_XI_TEST_PATTERN_GENERATOR_SELECTOR = videocapture.get(cv2.CAP_PROP_XI_TEST_PATTERN_GENERATOR_SELECTOR)
        print('CAP_PROP_XI_TEST_PATTERN_GENERATOR_SELECTOR %s' % CAP_PROP_XI_TEST_PATTERN_GENERATOR_SELECTOR)

        print('-' * 21)
        CAP_PROP_XI_TIMEOUT = videocapture.get(cv2.CAP_PROP_XI_TIMEOUT)
        print('CAP_PROP_XI_TIMEOUT %s' % CAP_PROP_XI_TIMEOUT)

        print('-' * 21)
        CAP_PROP_XI_TRANSPORT_PIXEL_FORMAT = videocapture.get(cv2.CAP_PROP_XI_TRANSPORT_PIXEL_FORMAT)
        print('CAP_PROP_XI_TRANSPORT_PIXEL_FORMAT %s' % CAP_PROP_XI_TRANSPORT_PIXEL_FORMAT)

        print('-' * 21)
        CAP_PROP_XI_TRG_DELAY = videocapture.get(cv2.CAP_PROP_XI_TRG_DELAY)
        print('CAP_PROP_XI_TRG_DELAY %s' % CAP_PROP_XI_TRG_DELAY)

        CAP_PROP_XI_TRG_SELECTOR = videocapture.get(cv2.CAP_PROP_XI_TRG_SELECTOR)
        print('CAP_PROP_XI_TRG_SELECTOR %s' % CAP_PROP_XI_TRG_SELECTOR)

        CAP_PROP_XI_TRG_SOFTWARE = videocapture.get(cv2.CAP_PROP_XI_TRG_SOFTWARE)
        print('CAP_PROP_XI_TRG_SOFTWARE %s' % CAP_PROP_XI_TRG_SOFTWARE)

        CAP_PROP_XI_TRG_SOURCE = videocapture.get(cv2.CAP_PROP_XI_TRG_SOURCE)
        print('CAP_PROP_XI_TRG_SOURCE %s' % CAP_PROP_XI_TRG_SOURCE)

        print('-' * 21)
        CAP_PROP_XI_TS_RST_MODE = videocapture.get(cv2.CAP_PROP_XI_TS_RST_MODE)
        print('CAP_PROP_XI_TS_RST_MODE %s' % CAP_PROP_XI_TS_RST_MODE)

        CAP_PROP_XI_TS_RST_SOURCE = videocapture.get(cv2.CAP_PROP_XI_TS_RST_SOURCE)
        print('CAP_PROP_XI_TS_RST_SOURCE %s' % CAP_PROP_XI_TS_RST_SOURCE)

        print('-' * 21)
        CAP_PROP_XI_USED_FFS_SIZE = videocapture.get(cv2.CAP_PROP_XI_USED_FFS_SIZE)
        print('CAP_PROP_XI_USED_FFS_SIZE %s' % CAP_PROP_XI_USED_FFS_SIZE)

        print('-' * 21)
        CAP_PROP_XI_WB_KB = videocapture.get(cv2.CAP_PROP_XI_WB_KB)
        print('CAP_PROP_XI_WB_KB %s' % CAP_PROP_XI_WB_KB)

        CAP_PROP_XI_WB_KG = videocapture.get(cv2.CAP_PROP_XI_WB_KG)
        print('CAP_PROP_XI_WB_KG %s' % CAP_PROP_XI_WB_KG)

        CAP_PROP_XI_WB_KR = videocapture.get(cv2.CAP_PROP_XI_WB_KR)
        print('CAP_PROP_XI_WB_KR %s' % CAP_PROP_XI_WB_KR)

        print('-' * 21)
        CAP_PROP_XI_WIDTH = videocapture.get(cv2.CAP_PROP_XI_WIDTH)
        print('CAP_PROP_XI_WIDTH %s' % CAP_PROP_XI_WIDTH)

        print('-' * 21)
        CAP_PROP_ZOOM = videocapture.get(cv2.CAP_PROP_ZOOM)
        print('CAP_PROP_ZOOM %s' % CAP_PROP_ZOOM)

        print('-' * 21)
        CAP_PVAPI = videocapture.get(cv2.CAP_PVAPI)
        print('CAP_PVAPI %s' % CAP_PVAPI)

        print('-' * 21)
        CAP_PVAPI_DECIMATION_2OUTOF16 = videocapture.get(cv2.CAP_PVAPI_DECIMATION_2OUTOF16)
        print('CAP_PVAPI_DECIMATION_2OUTOF16 %s' % CAP_PVAPI_DECIMATION_2OUTOF16)

        CAP_PVAPI_DECIMATION_2OUTOF4 = videocapture.get(cv2.CAP_PVAPI_DECIMATION_2OUTOF4)
        print('CAP_PVAPI_DECIMATION_2OUTOF4 %s' % CAP_PVAPI_DECIMATION_2OUTOF4)

        CAP_PVAPI_DECIMATION_2OUTOF8 = videocapture.get(cv2.CAP_PVAPI_DECIMATION_2OUTOF8)
        print('CAP_PVAPI_DECIMATION_2OUTOF8 %s' % CAP_PVAPI_DECIMATION_2OUTOF8)

        CAP_PVAPI_DECIMATION_OFF = videocapture.get(cv2.CAP_PVAPI_DECIMATION_OFF)
        print('CAP_PVAPI_DECIMATION_OFF %s' % CAP_PVAPI_DECIMATION_OFF)

        print('-' * 21)
        CAP_PVAPI_FSTRIGMODE_FIXEDRATE = videocapture.get(cv2.CAP_PVAPI_FSTRIGMODE_FIXEDRATE)
        print('CAP_PVAPI_FSTRIGMODE_FIXEDRATE %s' % CAP_PVAPI_FSTRIGMODE_FIXEDRATE)

        CAP_PVAPI_FSTRIGMODE_FREERUN = videocapture.get(cv2.CAP_PVAPI_FSTRIGMODE_FREERUN)
        print('CAP_PVAPI_FSTRIGMODE_FREERUN %s' % CAP_PVAPI_FSTRIGMODE_FREERUN)

        CAP_PVAPI_FSTRIGMODE_SOFTWARE = videocapture.get(cv2.CAP_PVAPI_FSTRIGMODE_SOFTWARE)
        print('CAP_PVAPI_FSTRIGMODE_SOFTWARE %s' % CAP_PVAPI_FSTRIGMODE_SOFTWARE)

        CAP_PVAPI_FSTRIGMODE_SYNCIN1 = videocapture.get(cv2.CAP_PVAPI_FSTRIGMODE_SYNCIN1)
        print('CAP_PVAPI_FSTRIGMODE_SYNCIN1 %s' % CAP_PVAPI_FSTRIGMODE_SYNCIN1)

        CAP_PVAPI_FSTRIGMODE_SYNCIN2 = videocapture.get(cv2.CAP_PVAPI_FSTRIGMODE_SYNCIN2)
        print('CAP_PVAPI_FSTRIGMODE_SYNCIN2 %s' % CAP_PVAPI_FSTRIGMODE_SYNCIN2)

        print('-' * 21)
        CAP_PVAPI_PIXELFORMAT_BAYER16 = videocapture.get(cv2.CAP_PVAPI_PIXELFORMAT_BAYER16)
        print('CAP_PVAPI_PIXELFORMAT_BAYER16 %s' % CAP_PVAPI_PIXELFORMAT_BAYER16)

        CAP_PVAPI_PIXELFORMAT_BAYER8 = videocapture.get(cv2.CAP_PVAPI_PIXELFORMAT_BAYER8)
        print('CAP_PVAPI_PIXELFORMAT_BAYER8 %s' % CAP_PVAPI_PIXELFORMAT_BAYER8)

        CAP_PVAPI_PIXELFORMAT_BGR24 = videocapture.get(cv2.CAP_PVAPI_PIXELFORMAT_BGR24)
        print('CAP_PVAPI_PIXELFORMAT_BGR24 %s' % CAP_PVAPI_PIXELFORMAT_BGR24)

        CAP_PVAPI_PIXELFORMAT_BGRA32 = videocapture.get(cv2.CAP_PVAPI_PIXELFORMAT_BGRA32)
        print('CAP_PVAPI_PIXELFORMAT_BGRA32 %s' % CAP_PVAPI_PIXELFORMAT_BGRA32)

        CAP_PVAPI_PIXELFORMAT_MONO16 = videocapture.get(cv2.CAP_PVAPI_PIXELFORMAT_MONO16)
        print('CAP_PVAPI_PIXELFORMAT_MONO16 %s' % CAP_PVAPI_PIXELFORMAT_MONO16)

        CAP_PVAPI_PIXELFORMAT_MONO8 = videocapture.get(cv2.CAP_PVAPI_PIXELFORMAT_MONO8)
        print('CAP_PVAPI_PIXELFORMAT_MONO8 %s' % CAP_PVAPI_PIXELFORMAT_MONO8)

        CAP_PVAPI_PIXELFORMAT_RGB24 = videocapture.get(cv2.CAP_PVAPI_PIXELFORMAT_RGB24)
        print('CAP_PVAPI_PIXELFORMAT_RGB24 %s' % CAP_PVAPI_PIXELFORMAT_RGB24)

        CAP_PVAPI_PIXELFORMAT_RGBA32 = videocapture.get(cv2.CAP_PVAPI_PIXELFORMAT_RGBA32)
        print('CAP_PVAPI_PIXELFORMAT_RGBA32 %s' % CAP_PVAPI_PIXELFORMAT_RGBA32)

        print('-' * 21)
        CAP_QT = videocapture.get(cv2.CAP_QT)
        print('CAP_QT %s' % CAP_QT)

        CAP_UNICAP = videocapture.get(cv2.CAP_UNICAP)
        print('CAP_UNICAP %s' % CAP_UNICAP)

        CAP_V4L = videocapture.get(cv2.CAP_V4L)
        print('CAP_V4L %s' % CAP_V4L)

        CAP_V4L2 = videocapture.get(cv2.CAP_V4L2)
        print('CAP_V4L2 %s' % CAP_V4L2)

        CAP_VFW = videocapture.get(cv2.CAP_VFW)
        print('CAP_VFW %s' % CAP_VFW)

        CAP_WINRT = videocapture.get(cv2.CAP_WINRT)
        print('CAP_WINRT %s' % CAP_WINRT)

        CAP_XIAPI = videocapture.get(cv2.CAP_XIAPI)
        print('CAP_XIAPI %s' % CAP_XIAPI)

        fps = videocapture.get(cv2.CAP_PROP_FPS)
        framenum = videocapture.get(cv2.CAP_PROP_FRAME_COUNT)
        duration = framenum / fps
        size = (int(videocapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videocapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        print(fps, framenum, duration, size)


if __name__ == '__main__':
    localurl = r'F:\BaiduNetdiskDownload\TumblrDownload\video\162711259557.mp4'
    getVideoCvInfo(localurl)
