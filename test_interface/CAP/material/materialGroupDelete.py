# -*- coding: utf-8 -*-
# @Time    : 2019-06-13 23:28
# @Author  : Emmy
# @File    : materialGroupDelete.py


#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
from common.public import *

class CAP_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-component/material/group/delete"
        print("----------开始测试----------")


    def test_materialDelete(self):
        """【素材】删除"""
        self.url = self.host + self.path
        data = {
            "id": [103]

        }

        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()