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
        self.path = "/api/geek-dmp-api/crowd/portrait"
        self.sql = "SELECT crowd_id FROM t_crowd WHERE `status` = 'COMPLETE' ORDER BY id DESC LIMIT 1;"
        self.dbname = "geek_icem_crowd"
        print("----------开始测试----------")


    #标签分类接口
    def test_crowdPortrait(self):
        self.url = self.host + self.path
        self.crowdId = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"crowdId":self.crowdId}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()