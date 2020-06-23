# -*- coding: utf-8 -*-
# @File       : multiProcessThread.py
# @Author     : Yuchen Chai
# @Date       : 2020/4/28 10:57
# @Description:
from threading import Lock

class thread_dataAssignment():
    """
    数据分发类，用于循环分发数据
    """

    def __init__(self,thread_num=1):
        self.__database = []
        self.__index = 0
        self.thread_num = thread_num
        self.__lock = Lock()
        pass

    def initialize_data(self, p_data):
        """
        初始化需要分发的数据
        :param p_data:
        :return:
        """
        self.__database = p_data
        pass

    def __len__(self):
        """
        数据长度
        :return:
        """
        return len(self.__database)

    def get_data(self):
        """
        获取一个数据
        :return:
        """

        status = False
        data = None

        # 获得锁
        self.__lock.acquire()
        try:
            if self.__index < len(self.__database):
                data = self.__database[self.__index]
                status = True
                self.__index += 1
                pass
        finally:
            self.__lock.release()
            pass
        print(self.__index)
        return status, data
    def finish_thread(self):
        self.thread_num -= 1
        pass

class thread_dataPool():
    """
        数据存储类，用于储存循环读入的数据
        """

    def __init__(self):
        self.__database = []
        self.__lock = Lock()
        pass

    def save_data(self, p_data):
        """
        初始化需要分发的数据
        :param p_data:
        :return:
        """
        # 获得锁
        self.__lock.acquire()
        self.__database.append(p_data)
        self.__lock.release()
        pass

    def __len__(self):
        """
        数据长度
        :return:
        """
        return len(self.__database)

    def get_data(self):
        """
        获取数据
        :return:
        """
        return self.__database

    pass

def Template_MultiThread():
    """多线程的例子"""

    def job(index, pool):
        status, item = pool.get_data()
        while(status):
            # do job

            status, item = pool.get_data()
            pass
        pass


    from commonTools import multiProcessThread
    from threading import Thread


    data_sample = [1,2,3,4]

    # 数据分发
    datapool = multiProcessThread.thread_dataAssignment()
    # 初始化数据分发
    datapool.initialize_data(data_sample)

    thread_nums = 5
    threads_pool = []

    for i in range(thread_nums):
        t = Thread(target=job,args=(i,datapool))
        t.start()
        threads_pool.append(t)
        pass

    for t in threads_pool:
        t.join()
        pass