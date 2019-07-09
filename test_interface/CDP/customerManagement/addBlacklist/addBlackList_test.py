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
        self.path = "/api/geek-dmp-api/customer/black"
        self.sql1 = "SELECT id from t_customer_list ORDER BY id DESC LIMIT 1;"
        self.sql2 = "SELECT id from t_customer_list LIMIT 1;"
        self.dbname = "geek_dmp_api"
        print("----------开始测试----------")


    #添加黑名单接口
    def test_addBlackList(self):
        '''添加黑名单接口'''
        self.url = self.host + self.path
        self.customerId01 = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql1))
        data = {"ids":[self.customerId01],"blackMark":"12"}
        # print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    #批量添加黑名单接口
    def test_moreBlack(self):
        '''批量reblack移出黑名单接口'''
        self.url = self.host + self.path
        self.customerId01 = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql1))
        self.customerId02 = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql2))
        data = {"ids":[self.customerId01,self.customerId02],"blackMark":"12"}
        # print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()