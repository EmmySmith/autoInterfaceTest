# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 2:48 PM
# @Author  : Emmy
# @File    : c_stores.py


# coding=utf-8
import requests
import unittest
import datetime,random
from common.public import *
from common.commonData import *

class c_stores(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path1 = "/api/icem-component/stores/update?appid=2019090466884677"

    def test_c_stores(self):
        self.url = self.host + self.path1
        data ={
            "activeColor": "#ff6a24",
            "backgroundColor": "#ffffff",
            "channel": "ALIPAY",
            "color": "#a7a7a7",
            "id": 6,
            "items": [{
                "activeIcon": "https://geek-icem.oss-cn-beijing.aliyuncs.com/dev/1/material/80c015d8da04428abe8cdb5c707453e8.png",
                "icon": "https://geek-icem.oss-cn-beijing.aliyuncs.com/dev/1/material/90a2e9959d8c4b9f996fa23e3a5a551d.png",
                "iconIndex": 1,
                "id": 22,
                "pageId": "",
                "pageName": "home",
                "pageTitle": "店铺首页",
                "pageUrl": "pages/home/index",
                "text": "自动化"+str(random.randrange(0,99999,2))
            }, {
                "activeIcon": "https://geek-icem.oss-cn-beijing.aliyuncs.com/dev/1/material/0835e9909bae4290af547377373212a8.png",
                "icon": "https://geek-icem.oss-cn-beijing.aliyuncs.com/dev/1/material/535ccf563c4b444ea2a538d3bf0c7ed0.png",
                "iconIndex": 2,
                "id": 23,
                "pageId": commonData.imageFirstId,
                "pageTitle": "微页面 | "+str(commonData.pageTitle),
                "pageUrl": "pages/tabpage1/index",
                "text": "个人中心"
            }]
        }
        print(self.url)
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0


if __name__ == "__main__":
    sms = c_stores()