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
        self.path = "/api/icem-activity/workflow/modify"
        self.path_userDefinedCrowd = "/api/icem-crowd/crowds?page=0&size=10&sort=createTime,desc"
        self.random = random.randint(1000,99999)
        self.sql = "SELECT id FROM t_workflow_node_define WHERE node_name = '客群选人' ORDER BY id DESC LIMIT 1;"
        self.dbname = "geek_icem_activity"
        self.data = {"type": "USER_DEFINED"}
        print("----------开始测试----------")


    #客群选人确定接口
    def test_workFlowModify(self):
        '''客群选人确定接口'''
        self.url = self.host + self.path
        self.url_userDefinedCrowd = self.host + self.path_userDefinedCrowd
        self.response_userDefinedCrowd = requests.post(url=self.url_userDefinedCrowd, data=json.dumps(self.data), headers=self.headers)
        self.crowdKeyIds = self.response_userDefinedCrowd.json()['body']['content'][0]['id']
        print(self.crowdKeyIds)
        self.nodeDefineId = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"crowdKeyIds":[self.crowdKeyIds],"nodeDefineId":self.nodeDefineId,"nodeName":"客群选人"}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()