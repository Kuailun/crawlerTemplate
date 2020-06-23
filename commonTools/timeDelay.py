# -*- coding: utf-8 -*-
# @File       : timeDelay.py
# @Author     : Yuchen Chai
# @Date       : 2020/4/16 11:23
# @Description:

import random
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .logger import logger

def randomTimeDelay(lowerBound, higherBound):
    """
    根据上下限，随机产生数字并睡眠
    :param lowerBound:单位：豪秒
    :param higherBound:单位：豪秒
    :return:
    """
    delay = random.randint(lowerBound,higherBound)/1.0
    time.sleep(delay/1000)
    return delay

def randomTimeDelay_Manual():
    """
    手动设置的随机等待函数
    :return:
    """
    setting = [
        {"possibility": 500, "lowerBound": 50, "higherBound": 150},
        {"possibility": 501, "lowerBound": 250, "higherBound": 350},
        #{"possibility": 500, "lowerBound": 35000, "higherBound": 55000},
        000.0
    ]

    long_parameter = random.randint(0, 1000)
    lowerBound = 0
    higherBound = 0
    wait_time = setting[-1]
    for item in setting:
        if type(item) == float:
            continue
        lowerBound = lowerBound
        higherBound = higherBound + item['possibility']
        if long_parameter>=lowerBound and long_parameter<higherBound:
            wait_time = randomTimeDelay(item["lowerBound"],item["higherBound"])
            break
        lowerBound = lowerBound + item['possibility']
        pass
    return wait_time/1000.0

def timestamp2Date(timestamp):
    '''
    将10位时间戳转换为日期
    '''
    timeArray = time.localtime(timestamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

def date2Timestamp(p_date):
    """
    将日期转为10位时间戳
    :param date: 2020-01-02 01:02:03
    :return:
    """
    mTime = time.strptime(p_date,"%Y-%m-%d %H:%M:%S")
    otherStyleTime = int(time.mktime(mTime))
    return otherStyleTime


def fixedTimeScheduler(job,timeInterval):
    """
    定时运行函数
    :param job: 需要运行的函数
    :param timeInterval: 间隔
    :return:
    """
    logger.info(r"定时器设置完毕，运行间隔：{0}小时".format(timeInterval / 3600))
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, "interval", seconds=timeInterval)
    scheduler.start()
    return scheduler

def date2timestamp(date):
    date = datetime.datetime.strptime(date,"%Y-%m-%dT%H:%M:%S")
    return int(time.mktime(date.timetuple()))