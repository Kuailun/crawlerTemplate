# -*- coding: utf-8 -*-
# @File       : internet.py
# @Author     : Yuchen Chai
# @Date       : 2020/4/16 12:32
# @Description:

import random
import requests
from .logger import logger

class UserAgent:
    """
    构造Useragent库
    """

    def __init__(self):
        """
        初始化
        """
        self.__cellphoneUseragent = [
            "Dalvik/2.1.0 (Linux; U; Android 8.0.0; HUAWEI NXT-TL00 Build/HUAWEINXT-TL00)",
            "Dalvik/2.1.0 (Linux; U; Android 10.0.0; HUAWEI CLT-AL01 Build/HUAWEICLT-AL01)",
            "Dalvik/2.1.0 (Linux; U; Android 9.0.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10)",
            "Dalvik/2.1.0 (Linux; U; Android 9.0.0; HUAWEI NXT-DL00 Build/HUAWEINXT-AL10)",
        ]
        self.__browserUseragent = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        ]
        pass

    @property
    def cellAgent(self):
        """
        随机回传一个cellphone的useragent
        :return:
        """
        return str(self.__cellphoneUseragent[random.randint(0,len(self.__cellphoneUseragent)-1)])

    @property
    def browserAgent(self):
        """
                随机回传一个cellphone的useragent
                :return:
                """
        return str(self.__browserUseragent[random.randint(0, len(self.__browserUseragent) - 1)])
    pass

def get_response(url, headers = None):
    """
    根据用户要求，发生get请求
    :param url:
    :param headers:
    :return:
    """

    response = None
    try:
        if not headers:
            response = requests.get(url)
        else:
            response = requests.get(url,headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        # In the event of the rare invalid HTTP response, Requests will raise an HTTPError exception (e.g. 401 Unauthorized)
        logger.error('Request获取失败，{0}'.format(errh))
        pass
    except requests.exceptions.ConnectionError as errc:
        # In the event of a network problem (e.g. DNS failure, refused connection, etc)
        logger.error('Request获取失败，{0}'.format(errc))
        pass
    except requests.exceptions.Timeout as errt:
        # If a request times out, a Timeout exception is raised. Maybe set up for a retry, or continue in a retry loop
        logger.error('Request获取失败，{0}'.format(errt))
        pass
    except requests.exceptions.TooManyRedirects as errr:
        # If a request exceeds the configured number of maximum redirections, a TooManyRedirects exception is raised. Tell the user their URL was bad and try a different one
        logger.error('Request获取失败，{0}'.format(errr))
        pass
    except requests.exceptions.RequestException as err:
        # catastrophic error. bail.
        logger.error('Request获取失败，{0}'.format(err))
        pass
    except Exception as err:
        logger.error('Request其他失败原因，{0}'.format(err.__class__))
        pass
    return response