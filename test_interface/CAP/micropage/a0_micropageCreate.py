# -*- coding: utf-8 -*-
# @Time    : 2019-06-27 22:17
# @Author  : Emmy
# @File    : a0_micropageCreate.py




#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import time,random
from common.public import *
from common.commonData import *

class a0_micropageCreate_test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-component/micropage/create"
        print("----------开始测试----------")


    def test_materialUpdateTitle(self):
        """创建页面"""
        self.url = self.host + self.path
        data = {
            "id": "yStqC3pZWq",
            "title": "空白页面",
            "type": 0,
            "pageInfo": {
                "background": "#f7f7f7",
                "title": "自动化"+str(random.randrange(0,99999,2)),
                "templateId": 0
            },
            "source": []
        }

        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        commonData.pageId = json.loads(response.text)["body"]["pageId"]
        print(commonData.pageId)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = a0_micropageCreate_test()
