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
        self.path = "/api/icem-sms/sms/variable/status"
        # self.random = random.randint(1000, 99999)
        self.sql_disable = "SELECT id FROM t_sms_variable WHERE `status` = 1 ORDER BY id DESC LIMIT 1;"
        self.sql_enable = "SELECT id FROM t_sms_variable WHERE `status` = 2 ORDER BY id DESC LIMIT 1;"
        self.dbname = "geek_icem_system"
        print("----------开始测试----------")


    #禁用变量接口
    def test_variableStatus_disable(self):
        '''禁用变量接口'''
        self.url = self.host + self.path
        self.Id = DB_ICEM_proc(self.dbname).get_vslues(self.sql_disable)
        # print(self.Id)
        data = {"id":self.Id}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #启用变量接口
    def test_variableStatus_enable(self):
        '''启用变量接口'''
        self.url = self.host + self.path
        self.Id = DB_ICEM_proc(self.dbname).get_vslues(self.sql_enable)
        # print(self.Id)
        data = {"id":self.Id}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()