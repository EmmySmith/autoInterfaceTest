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
        self.path = "/api/icem-crowd/crowd/count"
        print("----------开始测试----------")


    #以场圈人-入会渠道-入会渠道 计算人数接口
    def test_MembershipChannel(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":32,"categoryName":"Membership_Channel","categoryViewName":"入会渠道","dateRange":"NO","level":2,"orderSort":4,"parentId":12,"parentName":"以场圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":185,"showType":"CHANNEL","tag":"MembershipChannel","tagName":"入会渠道 "}],"tag":"MembershipChannel","tagId":185,"dataType":"ENUM","showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":185,"showType":"CHANNEL","tag":"MembershipChannel","tagName":"入会渠道 "}],"values":[]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0




    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()