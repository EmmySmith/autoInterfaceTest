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
        self.path = "/api/geek-dmp-api/member/info"
        self.sql = "SELECT id from t_customer_list ORDER BY id DESC LIMIT 1;"
        self.dbname = "geek_dmp_api"
        print("----------开始测试----------")


    #diyLabel接口
    def test_diyLabel(self):
        self.url = self.host + self.path
        self.customerId = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql))
        data = {"merchantId":"1000","merchantMemberId":self.customerId,"biType":"diyLabel","categoryId":61}
        # print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0



    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()