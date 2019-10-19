# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 5:51 PM
# @Author  : Emmy
# @File    : b_micropage.py

# coding=utf-8
import requests
import unittest
import datetime,random
from common.public import *
from common.commonData import *

class b_micropage(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path1 = "/api/icem-component/micropage/list?page=0&size=10&appid=2019090466884677"
        self.path2 = "/api/icem-component/micropage/update?appid=2019090466884677"

    def test_b1_material(self):
        self.url = self.host + self.path1
        data ={}
        print(self.url)
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        commonData.imageFirstId= json.loads(response.text)["body"][0]["pageId"]
        commonData.pageTitle = json.loads(response.text)["body"][0]["onPageInfo"]["title"]
        print("页面装修第一个pageId为:" + str(commonData.imageFirstId))
        print("页面装修第一个pageTitle为:" + str(commonData.pageTitle))
        assert response.json()['error'] == 0



    def test_b2_material(self):
        """创建页面"""
        self.url = self.host + self.path2
        data ={
            "appid": "2019090466884677",
            "createDate": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "deleted": 0,
            "lastModifyDate": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "pageId": "5d9c5cb4e506657802121393",
            "pageInfo": {
                "background": "#f7f7f7",
                "title": "自动化"+str(random.randrange(0,99999,2)),
                "templateId": 0,
                "desc": "",
                "backgroundStyle": 0,
                "backgroundImage": "https://geek-icem.oss-cn-beijing.aliyuncs.com/release/1000/material/4e24bbeb190f436fb60a0eecb35742c1.jpg",
                "p": {}
            },
            "sellerId": 1000,
            "source": [],
            "title": "自动化"+str(random.randrange(0,99999,2)),
            "type": "0",
            "deploy": 1
        }
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = b_micropage()
