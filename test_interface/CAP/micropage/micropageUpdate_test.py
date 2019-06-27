# -*- coding: utf-8 -*-
# @Time    : 2019-06-27 20:57
# @Author  : Emmy
# @File    : micropageUpdate_test.py


#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json,time
from common.public import *

class CAP_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-component/micropage/update"
        print("----------开始测试----------")


    def test_materialUpdateTitle(self):
        """【新建页面】更新微页面"""
        self.url = self.host + self.path
        data = {
                "createDate": 1561640171710,
                "deleted": 0,
                "lastModifyDate": 1561640171710,
                "pageId": "5d14bcebe50665130731412f",
                "pageInfo": {
                    "background": "#f7f7f7",
                    "title": "自动化"+ time.strftime('%Y-%m-%d %H:%M:%S'),
                    "templateId": 0
                },
                "sellerId": 1000,
                "source": [],
                "title": "空白页面",
                "type": "0",
                "name": "PageSetting",
                "deploy": 0
            }

        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()
