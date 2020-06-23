# -*- coding: utf-8 -*-
# @File       : test.py
# @Author     : Yuchen Chai
# @Date       : 2020/4/16 11:21
# @Description:

from commonTools import fileIO as fi
from commonTools import timeDelay as td
from commonTools.logger import logger
import matplotlib.pyplot as plt
from commonTools import multiProcessThread
from threading import Thread
from time import time,sleep

print("{0}".format(td.date2Timestamp("2020-01-01 00:00:00")))