#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
from common.public import *
from parameterized import parameterized
from testData.customerManagement.customerInfoOverview import *
from mysqlHandle.common_mysql import *

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-resource/coupon/useRecord?page=1&pageSize=10"
        self.dbname = "geek_icem_resource"
        self.sql = "SELECT * FROM t_coupon WHERE state NOT IN (2) ORDER BY id DESC LIMIT 1;"
        print("----------开始测试----------")


    #优惠券核销记录接口
    def test_couponWriteOffRecord(self):
        self.url = self.host + self.path
        self.couponId = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"id":self.couponId}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()