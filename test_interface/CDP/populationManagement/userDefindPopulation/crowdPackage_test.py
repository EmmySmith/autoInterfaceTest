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
        self.sql = "SELECT id FROM t_crowd ORDER BY id DESC LIMIT 1;"
        self.dbname = "geek_icem_crowd"
        self.crowdId = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        self.path = "/api/geek-dmp-api/crowd/downLoad?crowdId="+str(self.crowdId)+"&&mark=adasd"
        print("----------开始测试----------")


    #人群打包接口
    def test_crowdPackage(self):
        self.url = self.host + self.path
        print(self.url)
        response = requests.get(url=self.url,headers=self.headers)
        print (response.text)
        # assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()