# -*- coding: utf-8 -*-
# @File       : run.py
# @Author     : Yuchen Chai
# @Date       : 2020/4/18 11:46
# @Description:

import sys
sys.path.append(r'C:\Users\Administrator\Desktop\xxx')
from commonTools.logger import logger
from Service_V1 import settings as ss
from commonTools.timeDelay import fixedTimeScheduler
from Service_V1.job import JOB

logger.info("程序开始运行")

# 首次运行
JOB()

scheduler = fixedTimeScheduler(JOB,ss.SCHEDULER_INTERVAL)

try:
    while(True):
        pass
except(KeyboardInterrupt, SystemExit):
    scheduler.shutdown()