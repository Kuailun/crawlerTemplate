# -*- coding: utf-8 -*-
# @File       : fileIO.py
# @Author     : Yuchen Chai
# @Date       : 2020/4/15 20:36
# @Description:

import os
import json
import pandas

def readTxt(fileName, encoding="utf-8",byLines=False):
    """
    根据要求，读入txt文件
    :param fileName: 文件的地址及名称
    :param encoding: 文件的编码方式
    :param byLines: 是否按行读入
    :return:
    """
    if os.path.exists(fileName):
        pass
    else:
        raise FileNotFoundError

    with open(fileName,'r',encoding=encoding) as f:
        if byLines:
            retLines = f.readlines()
        else:
            retLines = f.read()
    return retLines

def readJson(fileName,encoding="utf-8"):
    """
    读入json文件
    :param fileName:json文件的地址及名称
    :return:
    """
    if os.path.exists(fileName):
        pass
    else:
        raise FileNotFoundError

    with open(fileName,'r', encoding=encoding) as f:
        rtJs = json.load(f)

    return rtJs

def writeJson(fileName, content, encoding='utf-8',indent=0):
    """
    写入json文件
    :param fileName:
    :param encoding:
    :return:
    """
    with open(fileName,'w',encoding=encoding) as f:
        json.dump(content, f, ensure_ascii=False, indent=indent)
        pass
    pass

def readCSV_All(fileName,js=False):
    """
    读取csv文件
    :param fileName:
    :return:
    """
    if os.path.exists(fileName):
        pass
    else:
        raise FileNotFoundError

    df = pandas.read_csv(fileName)


    if js == False:
        return df
    else:
        ret_data = []
        temp = {}
        for index, row in df.iteritems:
            for item in row:
                temp[item] = row[item]
                pass
            ret_data.append(temp)
            pass
        pass

    return ret_data