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



    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()