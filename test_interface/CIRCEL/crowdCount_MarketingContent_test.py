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


    #营销圈人-营销内容-营销活动名称 计算人数接口
    def test_MarketingCampaignTitle(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":17,"categoryName":"MarketingContent","categoryViewName":"营销内容","dateRange":"NO","level":2,"orderSort":2,"parentId":16,"parentName":"营销圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":156,"showType":"FILTER_SELECTED","tag":"MarketingCampaignTitle","tagName":"营销活动名称"}],"tag":"MarketingCampaignTitle","tagId":156,"dataType":"ENUM","id":1,"showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":156,"showType":"FILTER_SELECTED","tag":"MarketingCampaignTitle","tagName":"营销活动名称"},{"createTime":1555911372000,"creator":"超级管理员","deadlineTime":1556467200000,"delFlag":0,"executeDefinition":"IMMEDIATE","id":1,"name":"去从从","remark":"去从","sellerId":1000,"startTime":1555997781000,"status":"DONE","updateTime":1556610259000}],"values":[1]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()