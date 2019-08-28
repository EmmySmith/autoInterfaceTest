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
        self.path = "/api/icem-activity/workflow/add"
        # self.random = random.randint(1000,99999)
        # self.sql = "SELECT id FROM t_activity ORDER BY id DESC LIMIT 1;"
        # self.dbname = "geek_icem_activity"
        print("----------开始测试----------")


    #计算节点交集接口
    def test_workflowAddIntersection(self):
        '''计算节点交集'''
        self.url = self.host + self.path
        data = {"type":"INTERSECT","nodeName":"交集","activityId":400,"x":650,"y":466}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()