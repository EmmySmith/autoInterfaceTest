#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
from common.public import *
from mysqlHandle.common_mysql import *

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-system/system/user/reset/pwd"
        self.dbname = "geek_icem_system"
        self.sql = "SELECT id FROM t_user WHERE is_delete != 'Y' AND real_name != '超级管理员' AND id != '9999' ORDER BY id DESC LIMIT 1;"
        print("----------开始测试----------")


    #修改登录密码接口
    def test_resetPassword(self):
        self.url = self.host + self.path
        self.userId = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql))
        data = {"id":self.userId}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()