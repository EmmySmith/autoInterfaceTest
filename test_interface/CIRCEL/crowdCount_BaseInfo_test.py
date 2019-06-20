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


    #属性圈人-基础信息-年龄 计算人数接口
    def test_age(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":8,"categoryName":"BasicInfo","categoryViewName":"基础信息","dateRange":"YES","level":2,"orderSort":1,"parentId":1,"parentName":"属性圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"REGION","dateRange":"NO","disabled":"false","id":90,"showType":"INPUT","tag":"Age","tagName":"年龄"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":91,"showType":"SELECTED","tag":"AgeBracket","tagName":"年龄阶段"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":92,"showType":"SELECTED","tag":"Gender","tagName":"性别"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":94,"showType":"SELECTED","tag":"Constellation","tagName":"星座"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":97,"showType":"SELECTED","tag":"LifeCycle","tagName":"人生阶段"}],"tag":"Age","tagId":90,"dataType":"REGION","regionType":"RG","showValues":[{"dataType":"REGION","dateRange":"NO","disabled":"false","id":90,"showType":"INPUT","tag":"Age","tagName":"年龄"},""],"values":[1,100]},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #属性圈人-基础信息-年龄阶段 计算人数接口
    def test_AgeBracket(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":8,"categoryName":"BasicInfo","categoryViewName":"基础信息","dateRange":"YES","level":2,"orderSort":1,"parentId":1,"parentName":"属性圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"REGION","dateRange":"NO","disabled":"false","id":90,"showType":"INPUT","tag":"Age","tagName":"年龄"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":91,"showType":"SELECTED","tag":"AgeBracket","tagName":"年龄阶段"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":92,"showType":"SELECTED","tag":"Gender","tagName":"性别"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":94,"showType":"SELECTED","tag":"Constellation","tagName":"星座"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":97,"showType":"SELECTED","tag":"LifeCycle","tagName":"人生阶段"}],"tag":"AgeBracket","tagId":91,"dataType":"ENUM","id":8046,"showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":91,"showType":"SELECTED","tag":"AgeBracket","tagName":"年龄阶段"},{"createTime":1560944769000,"id":8046,"modifyTime":1560944769000,"sellerId":1000,"tag":"AgeBracket","tagId":91,"value":2,"valueName":"26-30"}],"values":[2]},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #属性圈人-基础信息-性别 计算人数接口
    def test_Gender(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":8,"categoryName":"BasicInfo","categoryViewName":"基础信息","dateRange":"YES","level":2,"orderSort":1,"parentId":1,"parentName":"属性圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"REGION","dateRange":"NO","disabled":"false","id":90,"showType":"INPUT","tag":"Age","tagName":"年龄"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":91,"showType":"SELECTED","tag":"AgeBracket","tagName":"年龄阶段"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":92,"showType":"SELECTED","tag":"Gender","tagName":"性别"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":94,"showType":"SELECTED","tag":"Constellation","tagName":"星座"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":97,"showType":"SELECTED","tag":"LifeCycle","tagName":"人生阶段"}],"tag":"Gender","tagId":92,"dataType":"ENUM","id":8051,"showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":92,"showType":"SELECTED","tag":"Gender","tagName":"性别"},{"createTime":1560944769000,"id":8051,"modifyTime":1560944769000,"sellerId":1000,"tag":"Gender","tagId":92,"value":1,"valueName":"男"}],"values":[1]},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #属性圈人-基础信息-星座 计算人数接口
    def test_Constellation(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":8,"categoryName":"BasicInfo","categoryViewName":"基础信息","dateRange":"YES","level":2,"orderSort":1,"parentId":1,"parentName":"属性圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"REGION","dateRange":"NO","disabled":"false","id":90,"showType":"INPUT","tag":"Age","tagName":"年龄"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":91,"showType":"SELECTED","tag":"AgeBracket","tagName":"年龄阶段"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":92,"showType":"SELECTED","tag":"Gender","tagName":"性别"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":94,"showType":"SELECTED","tag":"Constellation","tagName":"星座"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":97,"showType":"SELECTED","tag":"LifeCycle","tagName":"人生阶段"}],"tag":"Constellation","tagId":94,"dataType":"ENUM","id":8072,"showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":94,"showType":"SELECTED","tag":"Constellation","tagName":"星座"},{"createTime":1560944770000,"id":8072,"modifyTime":1560944770000,"sellerId":1000,"tag":"Constellation","tagId":94,"value":9,"valueName":"魔蝎座"}],"values":[9]},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #属性圈人-基础信息-人生阶段 计算人数接口
    def test_LifeCycle(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":8,"categoryName":"BasicInfo","categoryViewName":"基础信息","dateRange":"YES","level":2,"orderSort":1,"parentId":1,"parentName":"属性圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"REGION","dateRange":"NO","disabled":"false","id":90,"showType":"INPUT","tag":"Age","tagName":"年龄"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":91,"showType":"SELECTED","tag":"AgeBracket","tagName":"年龄阶段"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":92,"showType":"SELECTED","tag":"Gender","tagName":"性别"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":94,"showType":"SELECTED","tag":"Constellation","tagName":"星座"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":97,"showType":"SELECTED","tag":"LifeCycle","tagName":"人生阶段"}],"tag":"LifeCycle","tagId":97,"dataType":"ENUM","id":8088,"showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":97,"showType":"SELECTED","tag":"LifeCycle","tagName":"人生阶段"},{"createTime":1560944770000,"id":8088,"modifyTime":1560944770000,"sellerId":1000,"tag":"LifeCycle","tagId":97,"value":0,"valueName":"单身"}],"values":[0]},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0



    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()