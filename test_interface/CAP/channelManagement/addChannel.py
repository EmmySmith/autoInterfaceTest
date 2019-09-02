# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 2:44 PM
# @Author  : Emmy
# @File    : addChannel.py


#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
import random
from common.public import *
from common.commonData import *

class CAP_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-interaction/channel/save"


    def test_addChannel(self):
        """新增渠道"""
        self.url = self.host + self.path
        print(self.url)
        data={
                "sellerId": "1000",
               "channelName":"自动化"+str(random.randrange(0,99999,2)),
        }
        response = requests.post(url=self.url,data=json.dumps(data),headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0
        commonData.id = json.loads(response.text)["body"]["id"]
        print(commonData.id)


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()
