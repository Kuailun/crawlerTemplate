# -*- coding: utf-8 -*-
# @File       : database.py
# @Author     : Yuchen Chai
# @Date       : 2020/4/18 11:47
# @Description:

from .logger import logger
import pymongo
import os
import json

DATABASE_TYPES = {"TXT":"txt","MongoDb":"mongodb","Excel":"xls"}

class database:
    '''
    数据库类的基类，用于连接不同的数据库(Mongodb, txt, excel等等)
    '''

    def __init__(self, p_path, p_name, p_type):
        '''
        初始化数据基类
        :param p_path: 数据库保存路径
        :param p_name: 数据库名称
        :param p_type: 数据库类型（Mongodb, txt, excel等）
        '''

        self._name = p_name
        self._type = p_type
        self._database_path = p_path + p_name + "." + p_type
        self._database_available = True

        logger.debug("数据库选用模式为{0}".format(p_type))

        # 如果是Mongdo的形式，无需检查路径
        if p_type == DATABASE_TYPES["MongoDb"]:
            self._path_check = False
        pass

    def _Database_Path_Existing(self):
        '''
        检查数据库文件是否存在
        :return:
        '''

        # 如果无需检查，则返回
        if not self._path_check:
            return

        # 检查数据库的路径是否存在
        if not os.path.exists(self._database_path):
            logger.info(r"{0} 不存在，开始创建".format(self._name))
            self._Database_CreateFile()
            pass
        else:
            pass
        pass

    def _Database_CreateFile(self):
        '''
        创建数据库
        :return:
        '''
        raise("_Database_CreateFile函数未初始化")
    pass

class Mongo_Database(database):
    '''
    基于模板创立自己的数据库类
    '''

    def __init__(self):
        '''
        初始化自己的数据库类
        '''

        super(Mongo_Database, self).__init__("", "", DATABASE_TYPES['MongoDb'])

        # 连接MongoDb
        client = pymongo.MongoClient(host = "localhost", port = 27017)
        db = client.keepdata

        # 创建用户ID的集合
        collection_user_id = db.user
        collection_user_id.create_index('user_id', unique = True)

        # # 创建已确认的用户ID的集合
        # collection_confirmed_id = db.confirmed_id
        # collection_confirmed_id.create_index('confirmed_id', unique=True)

        # 数据库，不存在的话会创建
        # self._database = {"posts": collection_posts, "user_id": collection_user_id, "confirmed_id": collection_confirmed_id}
        self._database = {"user": collection_user_id}

        pass

    def post_in_collection(self, p_record):
        '''
        检查记录是否存在于Mongodb
        如果是，返回False
        如果否，记录到Mongodb中并返回True
        '''
        if self._database['posts'].find_one({"post_id":p_record}):
            return False
        else:
            data = {
                "post_id": p_record,
                "visited": 0
            }
            self._database['posts'].insert_one(data)
            logger.debug(r'将Post {0}插入Mongodb'.format(p_record))
            pass
        return True
    def not_visited_post(self):
        '''
        获取未曾访问过的Post列表
        '''

        not_visited = self._database['posts'].count_documents({"visited":0})
        if not_visited == 0:
            logger.info(r"所有Post均已经获得了对应的User ID")
            return None,0

        # MongoDb中未曾访问过的Post ID
        ret_data = self._database['posts'].find({"visited":0})
        return ret_data, not_visited
    def update_post(self, p_record, p_post_id):
        '''
        更新一个post记录
        '''
        self._database['posts'].update_one({"post_id":p_post_id}, {'$set':p_record})
        pass

    def update_user(self, p_record, p_user_id):
        """
        更新一个user记录
        """
        self._database['user_id'].update_one({"user_id":p_user_id},{"$set":p_record})
        pass

    def user_in_collection(self, p_record):
        '''
        检查记录是否存在于Mongodb
        如果是，返回False
        如果否，记录到Mongodb中并返回True
        '''
        if self._database['user_id'].find_one({"user_id":p_record}):
            return False
        else:
            data = {
                "user_id": p_record,
                "visited": 0
            }
            self._database['user_id'].insert_one(data)
            # logger.debug(r'将User ID {0}插入Mongodb'.format(p_record))
            return True
            pass
        pass

    def confirmed_in_collection(self, p_record):
        """
        添加confirmed到数据库中
        """
        if self._database['confirmed_id'].find_one({"confirmed_id":p_record}):
            return False
        else:
            data = {
                "confirmed_id": p_record
            }
            self._database['confirmed_id'].insert_one(data)
            logger.debug(r'将confirmed ID {0}插入Mongodb'.format(p_record))
            pass
        pass

    def all_users_in_collection(self,onlyMain = False, start=None,limit=None):
        """
        无条件获取所有用户的ID
        @return:
        """
        if not onlyMain:
            if start!=None and limit!=None:
                ret_number = self._database['user_id'].count_documents({})
                ret_data = self._database['user_id'].find({}).skip(start).limit(limit)
                return ret_data, ret_number
            else:
                ret_number = self._database['user_id'].count_documents({})
                ret_data = self._database['user_id'].find({})
                return ret_data, ret_number
        else:
            if start!=None and limit!=None:
                ret_number = self._database['user_id'].count_documents({})
                ret_data = self._database['user_id'].find({}, {"data": 0}).skip(start).limit(limit)
                return ret_data, ret_number
            else:
                ret_number = self._database['user_id'].count_documents({})
                ret_data = self._database['user_id'].find({},{"data":0})
                return ret_data, ret_number

    def get_user_in_collection(self, ID):
        """
        根据ID搜索用户并返回数据
        @param ID:
        @return:
        """
        ret_data = self._database['user_id'].find({"user_id":ID})
        return ret_data


    def all_unconverted_users_in_collection(self):
        '''
        返回所有未转换过的user的ID
        '''
        ret_number = self._database['user_id'].count_documents({"converted":0})
        ret_data = self._database['user_id'].find({"converted":0})
        return ret_data, ret_number

    def all_unvisited_users_in_collection(self):
        """
        返回所有未获取过关注/粉丝的ID
        @return:
        """
        ret_number = self._database['user_id'].count_documents({"visited": 0})
        ret_data = self._database['user_id'].find({"visited": 0})
        return ret_data, ret_number

    def all_confirmed_in_collection(self):
        '''
        返回所有confirmed的ID
        '''
        ret_number = self._database['confirmed_id'].count_documents({})
        ret_data = self._database['confirmed_id'].find({})
        return ret_data, ret_number

    def collection_statistic(self):
        """
        统计打印collection的数量
        """
        user_id = self._database['user_id'].count_documents({})
        print("总计有 {0} 个不同的userID".format(user_id))

        user_id_0 = self._database['user_id'].count_documents({"visited": 0})
        print("    其中有 {0} 个未获取好友".format(user_id_0))

        user_id_1 = self._database['user_id'].count_documents({"visited": 1})
        print("    其中有 {0} 个已获取好友".format(user_id_1))
        print()

        pass

    def collection_export_userId(self):
        """
        导出所有userID
        @return:
        """
        IDs = list(self._database['user_id'].find())

        json_data = []
        for item in IDs:
            json_data.append(item['user_id'])
            pass

        jsonData = json.dumps(json_data, ensure_ascii=False, indent=4, separators=(',', ':'), sort_keys=True)
        fileObject = open("UserInfo.json", 'w', encoding='utf-8')
        fileObject.write(jsonData)
        fileObject.close()
        pass

    def test(self):
        num = self._database['user_id'].count_documents({"timestamp":0})
        # self._database['user_id'].update_one({},{"$unset":{"converted":""}})
        print(num)
    pass