#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
import random
from common.public import *

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.name = random.randint(1000,9000)
        self.path = "/api/icem-crowd/crowd/create"
        print("----------开始测试----------")


    #新建人群
    def test_createCrowd(self):
        self.url = self.host + self.path
        self.crowdName = "自动化" + str(self.name)
        data = {
    "list":[
        {
            "categoryId":8,
            "categoryName":"BasicInfo",
            "categoryViewName":"基础信息",
            "dateRange":"YES",
            "level":2,
            "orderSort":1,
            "parentId":1,
            "targetType":"AttributeClustering",
            "viewType":"LIST",
            "parentName":"属性圈人",
            "values":[
                {
                    "label":"标签名称",
                    "showType":"TAG_AND_VALUE",
                    "value":[
                        {
                            "dataType":"REGION",
                            "dateRange":"NO",
                            "disabled":"false",
                            "id":90,
                            "showType":"INPUT",
                            "tag":"Age",
                            "tagName":"年龄"
                        },
                        {
                            "dataType":"ENUM",
                            "dateRange":"NO",
                            "disabled":"false",
                            "id":91,
                            "showType":"SELECTED",
                            "tag":"AgeBracket",
                            "tagName":"年龄阶段"
                        },
                        {
                            "dataType":"ENUM",
                            "dateRange":"NO",
                            "disabled":"false",
                            "id":92,
                            "showType":"SELECTED",
                            "tag":"Gender",
                            "tagName":"性别"
                        },
                        {
                            "dataType":"ENUM",
                            "dateRange":"NO",
                            "disabled":"false",
                            "id":94,
                            "showType":"SELECTED",
                            "tag":"Constellation",
                            "tagName":"星座"
                        },
                        {
                            "dataType":"ENUM",
                            "dateRange":"NO",
                            "disabled":"false",
                            "id":97,
                            "showType":"SELECTED",
                            "tag":"LifeCycle",
                            "tagName":"人生阶段"
                        }
                    ],
                    "tag":"Gender",
                    "tagId":92,
                    "dataType":"ENUM",
                    "id":422,
                    "showValues":[
                        {
                            "dataType":"ENUM",
                            "dateRange":"NO",
                            "disabled":"false",
                            "id":92,
                            "showType":"SELECTED",
                            "tag":"Gender",
                            "tagName":"性别"
                        },
                        {
                            "createTime":1558251291000,
                            "id":422,
                            "modifyTime":1558251291000,
                            "sellerId":1000,
                            "tag":"Gender",
                            "tagId":92,
                            "value":1,
                            "valueName":"男"
                        }
                    ],
                    "values":[
                        1
                    ]
                },
                {
                    "dataType":"DATE",
                    "id":-1,
                    "label":"时间",
                    "showType":"DATE",
                    "tag":"JiekeDateTime",
                    "value":[
                        {
                            "dataType":"DATE",
                            "id":-1,
                            "showType":"DATE"
                        }
                    ]
                }
            ]
        }
    ],
    "crowdName":self.crowdName
}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()