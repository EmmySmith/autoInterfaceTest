# -*- coding: utf-8 -*-
# @Time    : 2019-06-27 20:57
# @Author  : Emmy
# @File    : a2_micropageUpdate.py


#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json,time
from common.public import *
from test_interface.CAP.micropage.a1_micropageGet import *


class a2_micropageUpdate_test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-component/micropage/update"
        print("----------开始测试----------")


    def test_materialUpdateTitle(self):
        """更新微页面"""
        self.url = self.host + self.path
        data = {
                "createDate": 1561640171710,
                "deleted": 0,
                "lastModifyDate": 1561640171710,
                "pageId": commonData.pageId,
                "pageInfo": {
                    "background": "#f7f7f7",
                    "title": "自动化"+ str(random.randrange(0,9999,2)),
                    "templateId": 0
                },
                "sellerId": 1000,
                "source": [{
                    "conditionalItems": [{
                        "datas": [],
                        "matchRule": {
                            "crowds": [{
                                "id": 589,
                                "name": "微信测试"
                            }]
                        }
                    }],
                    "datas": [{
                        "img": "http://geek-icem.oss-cn-beijing.aliyuncs.com/release/1000/material/449cc33caf64498797d1b5e113aa6f32.jpg",
                        "id": "XkvW1CDBA",
                        "title": "自动化"
                    }],
                    "key": "Xme2OWm_s",
                    "name": "Banner",
                    "style": {
                        "boxShadow": "false",
                        "padding": 0,
                        "paginationType": 1,
                        "borderRadius": "false"
                    }
                }, {
                    "name": "Graphic",
                    "key": "9qYsSuWuO",
                    "style": {
                        "scroll": "false",
                        "backgroundColor": "#fff",
                        "textColor": "#000",
                        "template": 1,
                        "rcount": 4
                    },
                    "datas": [{
                        "id": "QANgn1ennZ",
                        "img": "http://geek-icem.oss-cn-beijing.aliyuncs.com/release/1000/material/fe6447ec8db94bd9a83231f7fbe519ea.jpg",
                        "title": "自动化1"
                    }, {
                        "id": "48-ZySVSHI",
                        "img": "http://geek-icem.oss-cn-beijing.aliyuncs.com/release/1000/material/836308f426cd48aaa8d7389cea395017.jpg",
                        "title": "自动化2"
                    }, {
                        "id": "AlXFblAxfk",
                        "img": "http://geek-icem.oss-cn-beijing.aliyuncs.com/release/1000/material/92f559e96e1d4e5fa956fa102158a83e.jpg",
                        "title": "自动化3"
                    }],
                    "conditionalItems": [{
                        "id": "AnmLcLjFt",
                        "matchRule": {
                            "crowds": [{
                                "name": "测试人群aaa",
                                "id": 588
                            }]
                        },
                        "datas": []
                    }]
                }, {
                    "name": "MemberCard",
                    "key": "koCHTsldE",
                    "style": {
                        "boxShadow": "true",
                        "borderRadius": "true",
                        "textColor": "#666",
                        "padding": 13,
                        "margin": 6,
                        "paginationType": 1
                    },
                    "datas": {
                        "showItems": [{
                            "name": "会员头像",
                            "label": "headImg"
                        }, {
                            "name": "会员昵称",
                            "label": "nickName",
                            "placeholder": "会员昵称"
                        }, {
                            "name": "二维码",
                            "label": "qrcode"
                        }, {
                            "name": "余额",
                            "label": "remainSum",
                            "placeholder": "0"
                        }, {
                            "name": "积分",
                            "label": "integral",
                            "placeholder": "0"
                        }, {
                            "name": "优惠券",
                            "label": "couponCount",
                            "placeholder": "0"
                        }, {
                            "name": "会员等级",
                            "label": "memberLevel",
                            "placeholder": "黄金"
                        }],
                        "cardImg": "http://geek-icem.oss-cn-beijing.aliyuncs.com/release/1000/material/c2e06d1e58194997b082b3d51716ed0b.jpg"
                    }
                }],
                "title": "空白页面",
                "type": "0",
                "name": "PageSetting",
                "deploy": 0
            }

        print(self.url)
        print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = a0_micropageCreate_test()



