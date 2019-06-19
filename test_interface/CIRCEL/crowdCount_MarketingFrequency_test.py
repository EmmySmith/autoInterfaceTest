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


    #营销圈人-营销内容-营销总次数 计算人数接口
    def test_MarketingCount(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":18,"categoryName":"MarketingFrequency","categoryViewName":"营销频次","dateRange":"YES","level":2,"orderSort":3,"parentId":16,"parentName":"营销圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"REGION_NESTED","dateRange":"YES","disabled":"false","id":168,"showType":"INPUT","tag":"MarketingCount","tagName":"营销总次数"}],"tag":"MarketingCount","tagId":168,"dataType":"REGION_NESTED","regionType":"RG","showValues":[{"dataType":"REGION_NESTED","dateRange":"YES","disabled":"false","id":168,"showType":"INPUT","tag":"MarketingCount","tagName":"营销总次数"},""],"values":[1,100]},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}],"tagId":-1,"showValues":["1"],"values":[360]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()