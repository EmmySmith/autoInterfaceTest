# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 3:14 PM
# @Author  : Emmy

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
        self.path = "/api/icem-component/stores/update"
        print("----------开始测试----------")


    def test_materialDelete(self):
        """小程序导航管理"""
        self.url = self.host + self.path
        data = {
                "activeColor": "#ff6a24",
                "backgroundColor": "#ffffff",
                "channel": "ALIPAY",
                "color": "#a7a7a7",
                "id": 1,
                "items": [{
                    "activeIcon": "http://geek-icem.oss-cn-beijing.aliyuncs.com/dev/1/material/db6475b0b9e94075bc6cbaaab24ee532.png",
                    "icon": "http://geek-icem.oss-cn-beijing.aliyuncs.com/dev/1/material/a5581f55ba9940e8a90c55b77e27ec07.png",
                    "id": 1,
                    "pageName": "home",
                    "pageTitle": "店铺首页",
                    "pageUrl": "pages/home/index",
                    "text": "首页"
                }, {
                    "activeIcon": "http://geek-icem.oss-cn-beijing.aliyuncs.com/dev/1/material/0fb00e5602fd452d80e6e2c52099cda0.png",
                    "icon": "http://geek-icem.oss-cn-beijing.aliyuncs.com/dev/1/material/8f3419a754a84c568631d4cf59ffd38f.png",
                    "id": 6,
                    "pageId": "5d1c7938e5066515237b1c8f",
                    "pageTitle": "微页面 | 哈哈",
                    "pageUrl": "pages/tabpage1/index",
                    "text": "优惠券包"
                }, {
                    "activeIcon": "http://geek-icem.oss-cn-beijing.aliyuncs.com/dev/1/material/0835e9909bae4290af547377373212a8.png",
                    "icon": "http://geek-icem.oss-cn-beijing.aliyuncs.com/dev/1/material/535ccf563c4b444ea2a538d3bf0c7ed0.png",
                    "id": 12,
                    "pageId": "5cfe2549e5066531c85ca363",
                    "pageTitle": "微页面 | 个人中心",
                    "pageUrl": "pages/tabpage2/index",
                    "text": " 我的"
                }]
            }

        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()

