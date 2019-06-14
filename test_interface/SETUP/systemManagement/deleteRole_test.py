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
        self.path = "/api/icem-system/system/role/delete"
        self.sql = "SELECT id FROM t_role WHERE is_delete != 'Y' ORDER BY id DESC LIMIT 1;"
        self.dbname = "geek_icem_system"
        print("----------开始测试----------")


    #删除角色接口
    def test_deleteRole(self):
        self.url = self.host + self.path
        roleId = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql))
        print(roleId)
        data = {"ids":[roleId]}
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()