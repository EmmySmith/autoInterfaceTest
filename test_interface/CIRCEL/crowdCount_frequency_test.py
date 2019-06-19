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


    #属性圈人-频率-消费频次 计算人数接口
    def test_BuyCount(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":4,"categoryName":"ConsumptionFrequency","categoryViewName":"频率","dateRange":"YES","level":2,"orderSort":4,"parentId":1,"parentName":"属性圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"REGION_NESTED","dateRange":"YES","disabled":"false","id":35,"showType":"INPUT","tag":"BuyCount","tagName":"消费频次"},{"dataType":"ENUM","dateRange":"YES","disabled":"false","id":39,"showType":"SELECTED","tag":"BuyCountLevel","tagName":"消费频率"}],"tag":"BuyCount","tagId":35,"dataType":"REGION_NESTED","regionType":"RG","showValues":[{"dataType":"REGION_NESTED","dateRange":"YES","disabled":"false","id":35,"showType":"INPUT","tag":"BuyCount","tagName":"消费频次"},""],"values":[1,100]},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}],"tagId":-1,"showValues":["1"],"values":[360]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #属性圈人-频率-消费频次 计算人数接口
    def test_BuyCountLevel(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":4,"categoryName":"ConsumptionFrequency","categoryViewName":"频率","dateRange":"YES","level":2,"orderSort":4,"parentId":1,"parentName":"属性圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"REGION_NESTED","dateRange":"YES","disabled":"false","id":35,"showType":"INPUT","tag":"BuyCount","tagName":"消费频次"},{"dataType":"ENUM","dateRange":"YES","disabled":"false","id":39,"showType":"SELECTED","tag":"BuyCountLevel","tagName":"消费频率"}],"tag":"BuyCountLevel","tagId":39,"dataType":"ENUM","id":7715,"showValues":[{"dataType":"ENUM","dateRange":"YES","disabled":"false","id":39,"showType":"SELECTED","tag":"BuyCountLevel","tagName":"消费频率"},{"createTime":1560944756000,"id":7715,"modifyTime":1560944756000,"sellerId":1000,"tag":"BuyCountLevel","tagId":39,"value":0,"valueName":"高频"}],"values":[0]},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}],"tagId":-1,"showValues":["1"],"values":[360]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()