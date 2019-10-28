# -*- coding: utf-8 -*-
# @Time    : 2019-07-10 10:05
# @Author  : renming
# @File    : materialGroup_test.py


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
        self.path = "/api/icem-wechat/material/wx90d8a37adac76a84/news"
        print("----------开始测试----------")

    #添加微信图文接口
    def test_addNews(self):
        """添加微信图文接口"""
        self.url = self.host + self.path
        self.data = {"articles":[{"title":"cececece","thumbMediaId":"l9Nxln_NQF5SG96148pY4FZQLEuCQUFZpNG2VoEHG5U","thumbUrl":"http://mmbiz.qpic.cn/mmbiz_png/SMzd2ReklgDbf9Vf0frJ1aSb9VSiaoZqGFfrXmpIUBGGbCVtr20D6Z4Hic6kw1zzhWdQNrC5GnAggKLxeRZKWBoA/0?wx_fmt=png","author":"mingming","digest":"sssssssssssssssssssssss","showCoverPic":1,"content":"<p><img src=\"http://mmbiz.qpic.cn/mmbiz_png/SMzd2ReklgDr9Pu3WGZcosnHcuQY92vQEKBV9ppZsvUC3bENpGk01O5ibxcoWtH3kzTD3hia8kicFgdjZ1Hf01Taw/0?wx_fmt=png\"></p>","contentSourceUrl":"www.baidu.com","cardIds":[]}]}
        print(self.url)
        response = requests.post(url=self.url,data=json.dumps(self.data),headers=self.headers)
        print (response.text)

    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()