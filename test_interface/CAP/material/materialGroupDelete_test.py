# -*- coding: utf-8 -*-
# @Time    : 2019-06-20 13:23
# @Author  : Emmy
# @File    : materialGroupDelete_test.py

#!/usr/bin/python
import unittest,requests
import time,os
from common.login import *
from common.public import *

class CAP_interface(unittest.TestCase):
    def setUp(self):
        self.headers=headers
        self.host= host
        self.path = "/api/icem-component/material/group/delete?id=44"

    def materialGroupDelete(self):
        """【素材中心】分组删除"""
        self.url = self.host + self.path
        data = {

        }
        response = requests.delete(url=self.url,data= json.dumps(data),headers=self.headers)
        print(response.text)
        print(response.status_code)
        assert response.json()["error"]==0

    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_interface()

