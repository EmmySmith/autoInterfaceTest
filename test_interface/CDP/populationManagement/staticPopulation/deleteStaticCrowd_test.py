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
        self.path = "/api/icem-crowd/crowd/delete"
        self.sql = "SELECT id from t_crowd ORDER BY id DESC LIMIT 1;"
        self.dbname = "geek_icem_crowd"
        print("----------开始测试----------")


    #静态人群删除接口
    def test_crowdDownload(self):
        '''静态人群删除接口'''
        self.url = self.host + self.path
        self.crowd_id = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"id":self.crowd_id}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.text != "null"
        # assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()