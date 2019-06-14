# -*- coding: utf-8 -*-
# @Time    : 2019-06-13 23:19
# @Author  : Emmy
# @File    : materialGroupSave_test.py



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
        self.path = "/api/icem-component/material/group/save"
        print("----------开始测试----------")


    def test_materialDelete(self):
        """【素材】移动分组"""
        self.url = self.host + self.path
        data = {
                "type": "image",
                "group_name": "笑话"
            }

        print(self.url)
        response = requests.get(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()