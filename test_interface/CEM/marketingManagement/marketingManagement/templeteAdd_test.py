#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json,time,random
from common.public import *
from mysqlHandle.common_mysql import *

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-activity/market/template/add"
        self.random = random.randint(1000,99999)
        self.sql = "SELECT id FROM t_activity ORDER BY id DESC LIMIT 1;"
        self.dbname = "geek_icem_activity"
        print("----------开始测试----------")


    #存为模板接口
    def test_templeteAdd(self):
        '''存为模板接口'''
        self.url = self.host + self.path
        self.activityId = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        self.name = "自动化" + str(self.random)
        data = {"name":"ren","remark":"小明","activityId":404,"list":[{"id":2007,"nodeName":"开始","type":"START","parentNodes":"","childNodes":"2008","x":220,"y":200},{"id":2008,"nodeName":"客群选人","type":"CROWD","parentNodes":"2007","childNodes":"2009","x":369,"y":206},{"id":2009,"nodeName":"生成目标组","type":"TARG_GROUP","parentNodes":"2008","childNodes":"2010","x":481,"y":247},{"id":2010,"nodeName":"发短信","type":"SMS","parentNodes":"2009","childNodes":"","x":630,"y":272}]}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()