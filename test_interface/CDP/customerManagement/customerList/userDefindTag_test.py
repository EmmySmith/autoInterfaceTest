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
        self.path = "/api/geek-dmp-api/crowd/userDefinedTag"
        self.sql = "SELECT id from t_customer_list ORDER BY id DESC LIMIT 1;"
        self.dbname = "geek_dmp_api"
        print("----------开始测试----------")


    #用户自定义标签接口
    def test_userDefindTag(self):
        self.url = self.host + self.path
        self.customerId = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql))
        data = {"ids":[self.customerId],"tags":["5月九日"]}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()