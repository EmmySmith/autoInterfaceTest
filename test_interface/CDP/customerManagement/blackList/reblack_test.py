#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json,random
from common.public import *
from mysqlHandle.common_mysql import *

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/geek-dmp-api/customer/reblack"
        self.path_reblack = "/api/geek-dmp-api/customer/black"
        self.path_list = "/api/icem-report/customer/list"
        #self.sql1 = "SELECT id from t_customer_list ORDER BY id DESC LIMIT 1;"
        self.sql = "SELECT  min(id) FROM t_customer_list WHERE blacklist =1"
        self.sql1 = "SELECT  min(id) FROM t_customer_list WHERE blacklist =1"
        #self.sql2 = "SELECT id from t_customer_list LIMIT 1;"
        self.sql2 = "SELECT  max(id) FROM t_customer_list WHERE blacklist =1"
        self.dbname = "geek_dmp_api"

        self.url_path = self.host + self.path_list
        data_list = {"page":0,"size":20}
        print(self.url_path)
        response_list = requests.post(url=self.url_path,data= json.dumps(data_list), headers=self.headers)
        if response_list.json()['body']['customerList'] == 'NULL':
            print("customerList is NULL")
        else:
            list = response_list.json()['body']['customerList']
            i = 0
            for item in list:
                print("%s" % item)
                i = i + 1
            print("customerList number is:", i)
            if i >= 3:
                for i in range(3):
                    self.sql_customer = "SELECT id FROM t_customer_list WHERE ISNULL(blacklist) OR blacklist = '0' ORDER BY id DESC LIMIT 1;"
                    self.url = self.host + self.path_reblack
                    self.customerId01 = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql_customer))
                    data = {"ids": [self.customerId01], "blackMark": "12"}
                    requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
            else:
                print("customerList number 小于 3，无需添加黑名单！")
        print("----------开始测试----------")


    #reblack移出黑名单接口
    def test_reblack(self):
        '''reblack移出黑名单接口'''
        self.url = self.host + self.path
        self.customerId01 = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql))
        data = {"ids":[self.customerId01]}
        # print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    #批量reblack移出黑名单接口
    def test_batchReblack(self):
        '''批量reblack移出黑名单接口'''
        self.url = self.host + self.path
        self.customerId01 = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql1))
        self.customerId02 = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql2))
        data = {"ids":[self.customerId01,self.customerId02]}
        # print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()