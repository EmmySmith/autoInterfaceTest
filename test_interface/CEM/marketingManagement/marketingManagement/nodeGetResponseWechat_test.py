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
        self.path = "/api/icem-activity/node/get/response"
        # self.random = random.randint(1000,99999)
        self.sql = "SELECT id FROM t_workflow_node_define WHERE node_name = '微信图文' ORDER BY id DESC LIMIT 1;"
        self.dbname = "geek_icem_activity"
        print("----------开始测试----------")


    #获取发送微信图文接口
    def test_nodeGetResponseWechat(self):
        '''获取发送微信图文接口'''
        self.url = self.host + self.path
        self.nodeDefineId = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"nodeDefineId":self.nodeDefineId,"type":"WECHAT"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()