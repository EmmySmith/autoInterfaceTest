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


    #营销圈人-派样活动-参与排样活动次数 计算人数接口
    def test_SampleOrderCount(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":33,"categoryName":"Marketing_Activity","categoryViewName":"派样活动","dateRange":"YES","level":2,"orderSort":4,"parentId":16,"parentName":"营销圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"REGION","dateRange":"YES","disabled":"false","id":211,"showType":"INPUT","tag":"SampleOrderCount","tagName":"参与派样活动次数"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":212,"showType":"DATE","tag":"FirstSampleOrderDate","tagName":"首次参与派样活动时间"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":213,"showType":"DATE","tag":"LastSampleOrderDate","tagName":"最近一次参与派样活动时间"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":214,"showType":"FILTER_SELECTED","tag":"FirstSampleOrderProduct","tagName":"首次派样活动商品"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":215,"showType":"FILTER_SELECTED","tag":"LastSampleOrderProduct","tagName":"最近一次派样活动商品"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":216,"showType":"CHANNEL","tag":"FirstSampleOrderChannel","tagName":"首次派样活动渠道"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":217,"showType":"CHANNEL","tag":"LastSampleOrderChannel","tagName":"最近一次派样活动渠道"}],"tag":"SampleOrderCount","tagId":211,"dataType":"REGION","regionType":"RG","showValues":[{"dataType":"REGION","dateRange":"YES","disabled":"false","id":211,"showType":"INPUT","tag":"SampleOrderCount","tagName":"参与派样活动次数"},""],"values":[1,100]},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}],"tagId":-1,"showValues":["1"],"values":[3]}]}]}
        print(self.url)
        print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #营销圈人-派样活动-首次参与派样活动时间 计算人数接口
    def test_FirstSampleOrderDate(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":33,"categoryName":"Marketing_Activity","categoryViewName":"派样活动","dateRange":"YES","level":2,"orderSort":4,"parentId":16,"parentName":"营销圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"REGION","dateRange":"YES","disabled":"false","id":211,"showType":"INPUT","tag":"SampleOrderCount","tagName":"参与派样活动次数"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":212,"showType":"DATE","tag":"FirstSampleOrderDate","tagName":"首次参与派样活动时间"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":213,"showType":"DATE","tag":"LastSampleOrderDate","tagName":"最近一次参与派样活动时间"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":214,"showType":"FILTER_SELECTED","tag":"FirstSampleOrderProduct","tagName":"首次派样活动商品"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":215,"showType":"FILTER_SELECTED","tag":"LastSampleOrderProduct","tagName":"最近一次派样活动商品"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":216,"showType":"CHANNEL","tag":"FirstSampleOrderChannel","tagName":"首次派样活动渠道"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":217,"showType":"CHANNEL","tag":"LastSampleOrderChannel","tagName":"最近一次派样活动渠道"}],"tag":"FirstSampleOrderDate","tagId":212,"dataType":"DATE","showValues":[{"dataType":"DATE","dateRange":"NO","disabled":"false","id":212,"showType":"DATE","tag":"FirstSampleOrderDate","tagName":"首次参与派样活动时间"},"1"],"values":[3],"id":100045},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}],"tagId":-1,"showValues":["1"],"values":[3]}]}]}
        print(self.url)
        print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #营销圈人-派样活动-最近一次参与派样活动时间 计算人数接口
    def test_LastSampleOrderDate(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":33,"categoryName":"Marketing_Activity","categoryViewName":"派样活动","dateRange":"YES","level":2,"orderSort":4,"parentId":16,"parentName":"营销圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"REGION","dateRange":"YES","disabled":"false","id":211,"showType":"INPUT","tag":"SampleOrderCount","tagName":"参与派样活动次数"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":212,"showType":"DATE","tag":"FirstSampleOrderDate","tagName":"首次参与派样活动时间"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":213,"showType":"DATE","tag":"LastSampleOrderDate","tagName":"最近一次参与派样活动时间"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":214,"showType":"FILTER_SELECTED","tag":"FirstSampleOrderProduct","tagName":"首次派样活动商品"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":215,"showType":"FILTER_SELECTED","tag":"LastSampleOrderProduct","tagName":"最近一次派样活动商品"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":216,"showType":"CHANNEL","tag":"FirstSampleOrderChannel","tagName":"首次派样活动渠道"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":217,"showType":"CHANNEL","tag":"LastSampleOrderChannel","tagName":"最近一次派样活动渠道"}],"tag":"LastSampleOrderDate","tagId":213,"dataType":"DATE","showValues":[{"dataType":"DATE","dateRange":"NO","disabled":"false","id":213,"showType":"DATE","tag":"LastSampleOrderDate","tagName":"最近一次参与派样活动时间"},"1"],"values":[3],"id":100045},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}],"tagId":-1,"showValues":["1"],"values":[3]}]}]}
        print(self.url)
        print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #营销圈人-派样活动-首次派样活动商品 计算人数接口
    def test_FirstSampleOrderProduct(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":33,"categoryName":"Marketing_Activity","categoryViewName":"派样活动","dateRange":"YES","level":2,"orderSort":4,"parentId":16,"parentName":"营销圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"REGION","dateRange":"YES","disabled":"false","id":211,"showType":"INPUT","tag":"SampleOrderCount","tagName":"参与派样活动次数"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":212,"showType":"DATE","tag":"FirstSampleOrderDate","tagName":"首次参与派样活动时间"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":213,"showType":"DATE","tag":"LastSampleOrderDate","tagName":"最近一次参与派样活动时间"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":214,"showType":"FILTER_SELECTED","tag":"FirstSampleOrderProduct","tagName":"首次派样活动商品"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":215,"showType":"FILTER_SELECTED","tag":"LastSampleOrderProduct","tagName":"最近一次派样活动商品"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":216,"showType":"CHANNEL","tag":"FirstSampleOrderChannel","tagName":"首次派样活动渠道"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":217,"showType":"CHANNEL","tag":"LastSampleOrderChannel","tagName":"最近一次派样活动渠道"}],"tag":"FirstSampleOrderProduct","tagId":214,"dataType":"ENUM","showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":214,"showType":"FILTER_SELECTED","tag":"FirstSampleOrderProduct","tagName":"首次派样活动商品"},{"id":100043,"name":"绿茶身体磨砂膏"}],"values":[100043],"id":100043},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}],"tagId":-1,"showValues":["1"],"values":[3]}]}]}
        print(self.url)
        print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #营销圈人-派样活动-最近一次派样活动商品 计算人数接口
    def test_LastSampleOrderProduct(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":33,"categoryName":"Marketing_Activity","categoryViewName":"派样活动","dateRange":"YES","level":2,"orderSort":4,"parentId":16,"parentName":"营销圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"REGION","dateRange":"YES","disabled":"false","id":211,"showType":"INPUT","tag":"SampleOrderCount","tagName":"参与派样活动次数"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":212,"showType":"DATE","tag":"FirstSampleOrderDate","tagName":"首次参与派样活动时间"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":213,"showType":"DATE","tag":"LastSampleOrderDate","tagName":"最近一次参与派样活动时间"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":214,"showType":"FILTER_SELECTED","tag":"FirstSampleOrderProduct","tagName":"首次派样活动商品"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":215,"showType":"FILTER_SELECTED","tag":"LastSampleOrderProduct","tagName":"最近一次派样活动商品"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":216,"showType":"CHANNEL","tag":"FirstSampleOrderChannel","tagName":"首次派样活动渠道"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":217,"showType":"CHANNEL","tag":"LastSampleOrderChannel","tagName":"最近一次派样活动渠道"}],"tag":"LastSampleOrderProduct","tagId":215,"dataType":"ENUM","showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":215,"showType":"FILTER_SELECTED","tag":"LastSampleOrderProduct","tagName":"最近一次派样活动商品"},{"id":100043,"name":"绿茶身体磨砂膏"}],"values":[100043],"id":100043},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}],"tagId":-1,"showValues":["1"],"values":[3]}]}]}
        print(self.url)
        print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #营销圈人-派样活动-首次派样活动渠道 计算人数接口
    def test_FirstSampleOrderChannel(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":33,"categoryName":"Marketing_Activity","categoryViewName":"派样活动","dateRange":"YES","level":2,"orderSort":4,"parentId":16,"parentName":"营销圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"REGION","dateRange":"YES","disabled":"false","id":211,"showType":"INPUT","tag":"SampleOrderCount","tagName":"参与派样活动次数"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":212,"showType":"DATE","tag":"FirstSampleOrderDate","tagName":"首次参与派样活动时间"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":213,"showType":"DATE","tag":"LastSampleOrderDate","tagName":"最近一次参与派样活动时间"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":214,"showType":"FILTER_SELECTED","tag":"FirstSampleOrderProduct","tagName":"首次派样活动商品"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":215,"showType":"FILTER_SELECTED","tag":"LastSampleOrderProduct","tagName":"最近一次派样活动商品"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":216,"showType":"CHANNEL","tag":"FirstSampleOrderChannel","tagName":"首次派样活动渠道"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":217,"showType":"CHANNEL","tag":"LastSampleOrderChannel","tagName":"最近一次派样活动渠道"}],"tag":"FirstSampleOrderChannel","tagId":216,"dataType":"ENUM","showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":216,"showType":"CHANNEL","tag":"FirstSampleOrderChannel","tagName":"首次派样活动渠道"}],"values":[],"id":100043},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}],"tagId":-1,"showValues":["1"],"values":[3]}]}]}
        print(self.url)
        print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #营销圈人-派样活动-最近一次派样活动渠道 计算人数接口
    def test_LastSampleOrderChannel(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":33,"categoryName":"Marketing_Activity","categoryViewName":"派样活动","dateRange":"YES","level":2,"orderSort":4,"parentId":16,"parentName":"营销圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"REGION","dateRange":"YES","disabled":"false","id":211,"showType":"INPUT","tag":"SampleOrderCount","tagName":"参与派样活动次数"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":212,"showType":"DATE","tag":"FirstSampleOrderDate","tagName":"首次参与派样活动时间"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":213,"showType":"DATE","tag":"LastSampleOrderDate","tagName":"最近一次参与派样活动时间"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":214,"showType":"FILTER_SELECTED","tag":"FirstSampleOrderProduct","tagName":"首次派样活动商品"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":215,"showType":"FILTER_SELECTED","tag":"LastSampleOrderProduct","tagName":"最近一次派样活动商品"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":216,"showType":"CHANNEL","tag":"FirstSampleOrderChannel","tagName":"首次派样活动渠道"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":217,"showType":"CHANNEL","tag":"LastSampleOrderChannel","tagName":"最近一次派样活动渠道"}],"tag":"LastSampleOrderChannel","tagId":217,"dataType":"ENUM","showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":217,"showType":"CHANNEL","tag":"LastSampleOrderChannel","tagName":"最近一次派样活动渠道"}],"values":[],"id":100043},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}],"tagId":-1,"showValues":["1"],"values":[3]}]}]}
        print(self.url)
        print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0



    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()