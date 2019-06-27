# -*- coding: utf-8 -*-
# @Time    : 2019-06-17 18:09
# @Author  : Emmy
# @File    : materialGroupSave_test.py


#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json,time,random
from common.public import *
from mysqlHandle.common_mysql import *

class CAP_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/micropage/material/group/save"
        print("----------开始测试----------")


    def test_materialSave(self):
        """【素材分组】修改名称"""
        self.url = self.host + self.path
        data = {
            "type": "image",
            "group_name":"l0"+str((random.randint(0,9999))),
            "id": 4
        }

        response = requests.post(self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()

