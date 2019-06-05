#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
from common.public import *

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        # self.host = host_dev
        self.path = "/api/icem-resource/coupon/modify"
        print("----------开始测试----------")


    #优惠券更新接口
    def test_couponUpdate(self):
        self.url = self.host + self.path
        data = {
	"id": 23,
	"sellerId": 1000,
	"couponName": "解客优惠券1",
	"overdueType": 2,
	"afterReceive": 2,
	"effective": 5,
	"couponType": 2,
	"couponCount": 18,
	"limitNumber": 2,
	"limitOfGoods": [],
	"limitOfShops": [],
	"storeId": 21,
	"storeLogo": "release/1000/storeLogo/39b11e69612b4e0a8baa06593fb5fe17.png",
	"storeLogoAbsolute": "http://geek-icem.oss-cn-beijing.aliyuncs.com/release/1000/storeLogo/39b11e69612b4e0a8baa06593fb5fe17.png",
	"cover": "release/1000/couponCover/8d1f1aa23d984faba2a97121f8cb073f.jpg",
	"discountExplain": "解客优惠券",
	"notice": "解客使用",
	"customerServiceTel": "233322323",
	"benefit": {
		"threshold": 10,
		"benefit": 1
	},
	"images": [{
		"showUrl": "http://geek-icem.oss-cn-beijing.aliyuncs.com/release/1000/couponDetail/1830edee262e4c0e9e37e0ab43ad4c7d.jpg",
		"url": "release/1000/couponDetail/1830edee262e4c0e9e37e0ab43ad4c7d.jpg",
		"text": "解客图片"
	}],
	"benefitStr": 1
}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()