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
        self.path = "/api/icem-crowd/custom/tag/delete"
        self.dbname = "geek_icem_crowd"
        self.sql = "SELECT id FROM t_tag_custom WHERE flag != 'YES' ORDER BY id DESC LIMIT 1;"
        print("----------开始测试----------")


    #删除自定义标签接口
    def test_getLabel(self):
        '''删除自定义标签接口'''
        self.url = self.host + self.path
        self.labelId = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql))
        data = {"id":self.labelId}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()