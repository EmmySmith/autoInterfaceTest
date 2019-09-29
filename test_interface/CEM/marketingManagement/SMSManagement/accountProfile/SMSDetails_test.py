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
        self.path = "/api/icem-sms/sms/log/details?page=1&size=5"
        self.sql = "SELECT id FROM t_sms_message ORDER BY id DESC LIMIT 1;"
        self.dbname = "geek_icem_system"
        print("----------开始测试----------")


    #短信明细-提交条数接口
    def test_SMSDetails_submit(self):
        '''短信明细-提交条数接口'''
        self.url = self.host + self.path
        self.logId = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"logId":self.logId}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #短信明细-成功条数接口
    def test_SMSDetails_success(self):
        '''短信明细-成功条数接口'''
        self.url = self.host + self.path
        self.logId = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"logId":self.logId,"status":1}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #短信明细-失败条数接口
    def test_SMSDetails_fail(self):
        '''短信明细-失败条数接口'''
        self.url = self.host + self.path
        self.logId = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"logId":self.logId,"status":2}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #短信明细-未知条数接口
    def test_SMSDetails_unknow(self):
        '''短信明细-未知条数接口'''
        self.url = self.host + self.path
        self.logId = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"logId":self.logId,"status":0}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0



    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()