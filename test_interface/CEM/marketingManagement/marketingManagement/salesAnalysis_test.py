#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json,time,random
from common.public import *
from mysqlHandle.common_mysql import *

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/geek-dmp-api/activity/statistics/salesAnalysis"
        self.random = random.randint(1000,99999)
        self.sql = "SELECT id FROM t_activity ORDER BY id DESC LIMIT 1;"
        self.dbname = "geek_icem_activity"
        print("----------开始测试----------")


    #日销售情况分析接口
    def test_daySalesAnalysis(self):
        '''日销售情况分析接口'''
        self.url = self.host + self.path
        self.activityId = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"activityId":self.activityId,"begin":"2019-08-27 18:01:07","end":"2019-08-31 00:00:00","viewBy":"day"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #周销售情况分析接口
    def test_weekSalesAnaly(self):
        '''周销售情况分析接口'''
        self.url = self.host + self.path
        self.activityId = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"activityId":self.activityId,"begin":"2019-08-27 18:01:07","end":"2019-08-31 00:00:00","viewBy":"week"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()