#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json,random
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
        self.random = random.randint(1000,99999)
        self.couponName = "自动化"+str(self.random)
        self.path_create = "/api/icem-resource/coupon/add"
        self.createUrl = self.host + self.path_create

        data = {
            "couponName": self.couponName,
            "overdueType": 2,
            "couponType": 2,
            "afterReceive": 0,
            "effective": 90,
            "couponCount": 100,
            "limitNumber": 1,
            "benefitStr": 10,
            "benefit": {
                "threshold": 90,
                "benefit": 10
            },
            "limitOfGoods": [100043, 100044],
            "limitOfShops": [100001, 100002],
            "storeName": "自动化商户",
            "storeLogo": "release/1000/storeLogo/2ba1bba07be6407781a97f127b52eb41.png",
            "cover": "release/1000/couponCover/c483256a755a4ea3aad62eb956460898.png",
            "notice": "使用须知",
            "discountExplain": "优惠说明",
            "customerServiceTel": "5522322",
            "images": [{
                "showUrl": "http://geek-icem.oss-cn-beijing.aliyuncs.com/release/1000/couponDetail/c329f2eaf54a480499761c7efc3fe4d9.jpg",
                "url": "release/1000/couponDetail/c329f2eaf54a480499761c7efc3fe4d9.jpg"
            }]
        }
        requests.post(url=self.createUrl, data=json.dumps(data), headers=self.headers)
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