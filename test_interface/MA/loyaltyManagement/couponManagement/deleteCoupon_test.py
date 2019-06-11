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
        self.path = "/api/icem-resource/coupon/delete"
        self.name = "geek_icem_resource"
        self.sql = "SELECT * FROM t_coupon WHERE state NOT IN (2) ORDER BY id DESC LIMIT 1;"
        print("----------开始测试----------")


    #删除优惠券接口
    def test_deleteCoupon(self):
        self.url = self.host + self.path
        self.couponId = DB_ICEM_proc(self.name).get_vslues(self.sql)
        data = {"id":self.couponId}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()