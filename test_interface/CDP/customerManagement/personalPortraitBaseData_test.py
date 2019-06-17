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


    #workInfo接口
    def test_workInfo(self):
        self.url = self.host + self.path
        self.customerId = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql))
        data = {"merchantId":"1000","merchantMemberId":self.customerId,"biType":"workInfo","categoryId":39}
        # print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #baseInfo接口
    def test_baseInfo(self):
        self.url = self.host + self.path
        self.customerId = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql))
        data = {"merchantId":"1000","merchantMemberId":self.customerId,"biType":"baseInfo","categoryId":38}
        # print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #lbsInfo接口
    def test_lbsInfo(self):
        self.url = self.host + self.path
        self.customerId = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql))
        data = {"merchantId":"1000","merchantMemberId":self.customerId,"biType":"lbsInfo","categoryId":41}
        # print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0



    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()