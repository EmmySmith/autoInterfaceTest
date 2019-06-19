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


    #预测属性-价值预测-终身价值预测 计算人数接口
    def test_LifetimeExpectedValue(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":25,"categoryName":"ValuePrediction","categoryViewName":"价值预测 ","dateRange":"NO","level":2,"orderSort":1,"parentId":24,"parentName":"预测属性","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"REGION","dateRange":"NO","disabled":"false","id":2,"showType":"INPUT","tag":"LifetimeExpectedValue","tagName":"终身价值预期"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":3,"showType":"SELECTED","tag":"PredictedHighValue","tagName":"高价值新用户预测"}],"tag":"LifetimeExpectedValue","tagId":2,"dataType":"REGION","regionType":"RG","showValues":[{"dataType":"REGION","dateRange":"NO","disabled":"false","id":2,"showType":"INPUT","tag":"LifetimeExpectedValue","tagName":"终身价值预期"},""],"values":[1,100]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #预测属性-价值预测-高价值新用户预测 计算人数接口
    def test_PredictedHighValue(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":25,"categoryName":"ValuePrediction","categoryViewName":"价值预测 ","dateRange":"NO","level":2,"orderSort":1,"parentId":24,"parentName":"预测属性","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"REGION","dateRange":"NO","disabled":"false","id":2,"showType":"INPUT","tag":"LifetimeExpectedValue","tagName":"终身价值预期"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":3,"showType":"SELECTED","tag":"PredictedHighValue","tagName":"高价值新用户预测"}],"tag":"PredictedHighValue","tagId":3,"dataType":"ENUM","showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":3,"showType":"SELECTED","tag":"PredictedHighValue","tagName":"高价值新用户预测"},{"createTime":1560944752000,"id":7632,"modifyTime":1560944752000,"sellerId":1000,"tag":"PredictedHighValue","tagId":3,"value":0,"valueName":"是"}],"values":[0],"id":7632}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()