# -*- coding: utf-8 -*-
# @File       : string.py
# @Author     : Yuchen Chai
# @Date       : 2020/4/18 16:04
# @Description:

def gbkBytes(response):
    """
    将GBK编码的Bytes转成正常中文
    :param response:
    :return:
    """
    return bytes.decode(response)