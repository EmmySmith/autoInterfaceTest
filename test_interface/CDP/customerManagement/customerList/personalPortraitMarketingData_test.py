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
        self.path1 = "/api/geek-dmp-api/marketing/findMarketingEffect"
        self.path2 = "/api/geek-dmp-api/marketing/findMarketingValue"
        self.sql = "SELECT id from t_customer_list ORDER BY id DESC LIMIT 1;"
        self.dbname = "geek_dmp_api"
        print("----------开始测试----------")


    #营销效果接口
    def test_findMarketingEffect(self):
        self.url = self.host + self.path1
        self.customerId = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql))
        data = {"id":59,"merchantMemberId":self.customerId,"merchantId":"1000"}
        # print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        # print (response.json()['lower'][0]['viewName'])
        assert response.json()['lower'][0]['viewName'] != "NULL"

    #营销价值接口
    def test_findMarketingValue(self):
        self.url = self.host + self.path2
        self.customerId = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql))
        data = {"id":60,"merchantMemberId":self.customerId,"merchantId":"1000"}
        # print(data)s
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        # print (response.json()['lower'][0]['viewName'])
        assert response.json()[0]['viewName'] != "NULL"




    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()