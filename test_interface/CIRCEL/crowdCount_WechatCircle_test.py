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


    #特定圈人-微信圈人-全部公众号 计算人数接口
    def test_AllWechatCustomized(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":29,"categoryName":"WxPublicChannel","categoryViewName":"微信圈人","dateRange":"NO","level":2,"orderSort":1,"parentId":28,"parentName":"特定圈人","values":[{"dataType":"ENUM","id":178,"label":"所属公众号","showType":"SELECTED","tag":"OfficialAccountSource","tagId":178,"values":["wx59ff50e404b28528","wxec56ce9f40f391cc"]},{"label":"标签名称","showType":"WECHAT","value":[{"dataType":"DATE_NESTED","dateRange":"NO","disabled":"false","id":179,"showType":"UNLIMITED_DATE","tag":"SubscriptionDate","tagName":"关注时间","accountDisable":"false"},{"dataType":"ENUM_NESTED","dateRange":"NO","disabled":"false","id":180,"showType":"MULTIPLE_SELECT","tag":"WechatCustomizedTags","tagName":"公众号标签","accountDisable":"true"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":181,"showType":"SELECTED","tag":"WechatGender","tagName":"微信性别","accountDisable":"false"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":190,"showType":"SELECTED","tag":"SubscribeScene","tagName":"微信关注渠道来源","accountDisable":"false"}],"tag":"SubscriptionDate","tagId":179,"dataType":"DATE_NESTED","showValues":[{"dataType":"DATE_NESTED","dateRange":"NO","disabled":"false","id":179,"showType":"UNLIMITED_DATE","tag":"SubscriptionDate","tagName":"关注时间","accountDisable":"false"},1],"values":[360]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #特定圈人-微信圈人-解客营销云 计算人数接口
    def test_JieKeMarketingCloud(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":29,"categoryName":"WxPublicChannel","categoryViewName":"微信圈人","dateRange":"NO","level":2,"orderSort":1,"parentId":28,"parentName":"特定圈人","values":[{"dataType":"ENUM","id":178,"label":"所属公众号","showType":"SELECTED","tag":"OfficialAccountSource","tagId":178,"values":["wx59ff50e404b28528"]},{"label":"标签名称","showType":"WECHAT","value":[{"dataType":"DATE_NESTED","dateRange":"NO","disabled":"false","id":179,"showType":"UNLIMITED_DATE","tag":"SubscriptionDate","tagName":"关注时间","accountDisable":"false"},{"dataType":"ENUM_NESTED","dateRange":"NO","disabled":"false","id":180,"showType":"MULTIPLE_SELECT","tag":"WechatCustomizedTags","tagName":"公众号标签","accountDisable":"false"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":181,"showType":"SELECTED","tag":"WechatGender","tagName":"微信性别","accountDisable":"false"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":190,"showType":"SELECTED","tag":"SubscribeScene","tagName":"微信关注渠道来源","accountDisable":"false"}],"tag":"SubscriptionDate","tagId":179,"dataType":"DATE_NESTED","showValues":[{"dataType":"DATE_NESTED","dateRange":"NO","disabled":"false","id":179,"showType":"UNLIMITED_DATE","tag":"SubscriptionDate","tagName":"关注时间","accountDisable":"false"},1],"values":[360]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #特定圈人-微信圈人-会飞的小熊熊 计算人数接口
    def test_FlyingBear(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":29,"categoryName":"WxPublicChannel","categoryViewName":"微信圈人","dateRange":"NO","level":2,"orderSort":1,"parentId":28,"parentName":"特定圈人","values":[{"dataType":"ENUM","id":178,"label":"所属公众号","showType":"SELECTED","tag":"OfficialAccountSource","tagId":178,"values":["wxec56ce9f40f391cc"]},{"label":"标签名称","showType":"WECHAT","value":[{"dataType":"DATE_NESTED","dateRange":"NO","disabled":"false","id":179,"showType":"UNLIMITED_DATE","tag":"SubscriptionDate","tagName":"关注时间","accountDisable":"false"},{"dataType":"ENUM_NESTED","dateRange":"NO","disabled":"false","id":180,"showType":"MULTIPLE_SELECT","tag":"WechatCustomizedTags","tagName":"公众号标签","accountDisable":"false"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":181,"showType":"SELECTED","tag":"WechatGender","tagName":"微信性别","accountDisable":"false"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":190,"showType":"SELECTED","tag":"SubscribeScene","tagName":"微信关注渠道来源","accountDisable":"false"}],"tag":"SubscriptionDate","tagId":179,"dataType":"DATE_NESTED","showValues":[{"dataType":"DATE_NESTED","dateRange":"NO","disabled":"false","id":179,"showType":"UNLIMITED_DATE","tag":"SubscriptionDate","tagName":"关注时间","accountDisable":"false"},1],"values":[360]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0



    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()