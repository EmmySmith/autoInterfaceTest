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
        self.path = "/api/icem-sms/sms/variable/save"
        self.random = random.randint(1000, 99999)
        # self.sql = "SELECT id FROM t_sms_message ORDER BY id DESC LIMIT 1;"
        # self.dbname = "geek_icem_system"
        print("----------开始测试----------")


    #新增变量接口
    def test_AddVariable(self):
        '''新增变量接口'''
        self.url = self.host + self.path
        # self.logId = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"name":self.random,"attribute":"测试小明","defaultValue":"123456"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()