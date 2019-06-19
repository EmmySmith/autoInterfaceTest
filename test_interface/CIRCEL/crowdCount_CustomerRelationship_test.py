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


    #属性圈人-客户关系-客户生命周期 计算人数接口
    def test_CustomerLifeCycleStage(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":3,"categoryName":"CustomerRelationship","categoryViewName":"客户关系","dateRange":"YES","level":2,"orderSort":3,"parentId":1,"parentName":"属性圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":184,"showType":"SELECTED","tag":"CustomerLifeCycleStage","tagName":"客户生命周期"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":187,"showType":"SELECTED","tag":"CRMMembershipLevel","tagName":"CRM会员等级"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":23,"showType":"SELECTED","tag":"MembershipLevel","tagName":"消费者价值等级"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":24,"showType":"DATE_RANGE","tag":"MemberDate","tagName":"会员注册日期"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":186,"showType":"DATE_RANGE","tag":"LastInteraction","tagName":"最后互动时间"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":1,"showType":"SELECTED","tag":"CustomerIntimacy","tagName":"老客亲密度"},{"dataType":"REGION","dateRange":"NO","disabled":"false","id":16,"showType":"INPUT","tag":"CurrentPoints","tagName":"会员当前积分"}],"tag":"CustomerLifeCycleStage","tagId":184,"dataType":"ENUM","id":6346,"showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":184,"showType":"SELECTED","tag":"CustomerLifeCycleStage","tagName":"客户生命周期"},{"createTime":1560845310000,"id":6346,"modifyTime":1560845310000,"sellerId":1000,"tag":"CustomerLifeCycleStage","tagId":184,"value":1,"valueName":"I（互动未购买）"}],"values":[1]},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #属性圈人-客户关系-CRM会员等级 计算人数接口
    def test_CRMMembershipLevel(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":3,"categoryName":"CustomerRelationship","categoryViewName":"客户关系","dateRange":"YES","level":2,"orderSort":3,"parentId":1,"parentName":"属性圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":184,"showType":"SELECTED","tag":"CustomerLifeCycleStage","tagName":"客户生命周期"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":187,"showType":"SELECTED","tag":"CRMMembershipLevel","tagName":"CRM会员等级"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":23,"showType":"SELECTED","tag":"MembershipLevel","tagName":"消费者价值等级"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":24,"showType":"DATE_RANGE","tag":"MemberDate","tagName":"会员注册日期"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":186,"showType":"DATE_RANGE","tag":"LastInteraction","tagName":"最后互动时间"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":1,"showType":"SELECTED","tag":"CustomerIntimacy","tagName":"老客亲密度"},{"dataType":"REGION","dateRange":"NO","disabled":"false","id":16,"showType":"INPUT","tag":"CurrentPoints","tagName":"会员当前积分"}],"tag":"CRMMembershipLevel","tagId":187,"dataType":"ENUM","id":6354,"showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":187,"showType":"SELECTED","tag":"CRMMembershipLevel","tagName":"CRM会员等级"},{"createTime":1560845310000,"id":6354,"modifyTime":1560845310000,"sellerId":1000,"tag":"CRMMembershipLevel","tagId":187,"value":0,"valueName":"绿钻"}],"values":[0]},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    #属性圈人-客户关系-消费者价值等级 计算人数接口
    def test_MembershipLevel(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":3,"categoryName":"CustomerRelationship","categoryViewName":"客户关系","dateRange":"YES","level":2,"orderSort":3,"parentId":1,"parentName":"属性圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":184,"showType":"SELECTED","tag":"CustomerLifeCycleStage","tagName":"客户生命周期"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":187,"showType":"SELECTED","tag":"CRMMembershipLevel","tagName":"CRM会员等级"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":23,"showType":"SELECTED","tag":"MembershipLevel","tagName":"消费者价值等级"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":24,"showType":"DATE_RANGE","tag":"MemberDate","tagName":"会员注册日期"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":186,"showType":"DATE_RANGE","tag":"LastInteraction","tagName":"最后互动时间"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":1,"showType":"SELECTED","tag":"CustomerIntimacy","tagName":"老客亲密度"},{"dataType":"REGION","dateRange":"NO","disabled":"false","id":16,"showType":"INPUT","tag":"CurrentPoints","tagName":"会员当前积分"}],"tag":"MembershipLevel","tagId":23,"dataType":"ENUM","id":5553,"showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":23,"showType":"SELECTED","tag":"MembershipLevel","tagName":"消费者价值等级"},{"createTime":1560845278000,"id":5553,"modifyTime":1560845278000,"sellerId":1000,"tag":"MembershipLevel","tagId":23,"value":2,"valueName":"V3"}],"values":[2]},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #属性圈人-客户关系-会员注册日期 计算人数接口
    def test_MemberDate(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":3,"categoryName":"CustomerRelationship","categoryViewName":"客户关系","dateRange":"YES","level":2,"orderSort":3,"parentId":1,"parentName":"属性圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":184,"showType":"SELECTED","tag":"CustomerLifeCycleStage","tagName":"客户生命周期"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":187,"showType":"SELECTED","tag":"CRMMembershipLevel","tagName":"CRM会员等级"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":23,"showType":"SELECTED","tag":"MembershipLevel","tagName":"消费者价值等级"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":24,"showType":"DATE_RANGE","tag":"MemberDate","tagName":"会员注册日期"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":186,"showType":"DATE_RANGE","tag":"LastInteraction","tagName":"最后互动时间"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":1,"showType":"SELECTED","tag":"CustomerIntimacy","tagName":"老客亲密度"},{"dataType":"REGION","dateRange":"NO","disabled":"false","id":16,"showType":"INPUT","tag":"CurrentPoints","tagName":"会员当前积分"}],"tag":"MemberDate","tagId":24,"dataType":"DATE","id":5553,"showValues":[{"dataType":"DATE","dateRange":"NO","disabled":"false","id":24,"showType":"DATE_RANGE","tag":"MemberDate","tagName":"会员注册日期"},{"createTime":1560845278000,"id":5553,"modifyTime":1560845278000,"sellerId":1000,"tag":"MembershipLevel","tagId":23,"value":2,"valueName":"V3"}],"values":["20190601","20190630"]},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #属性圈人-客户关系-最后互动时间 计算人数接口
    def test_LastInteraction(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":3,"categoryName":"CustomerRelationship","categoryViewName":"客户关系","dateRange":"YES","level":2,"orderSort":3,"parentId":1,"parentName":"属性圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":184,"showType":"SELECTED","tag":"CustomerLifeCycleStage","tagName":"客户生命周期"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":187,"showType":"SELECTED","tag":"CRMMembershipLevel","tagName":"CRM会员等级"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":23,"showType":"SELECTED","tag":"MembershipLevel","tagName":"消费者价值等级"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":24,"showType":"DATE_RANGE","tag":"MemberDate","tagName":"会员注册日期"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":186,"showType":"DATE_RANGE","tag":"LastInteraction","tagName":"最后互动时间"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":1,"showType":"SELECTED","tag":"CustomerIntimacy","tagName":"老客亲密度"},{"dataType":"REGION","dateRange":"NO","disabled":"false","id":16,"showType":"INPUT","tag":"CurrentPoints","tagName":"会员当前积分"}],"tag":"LastInteraction","tagId":186,"dataType":"DATE","id":5553,"showValues":[{"dataType":"DATE","dateRange":"NO","disabled":"false","id":186,"showType":"DATE_RANGE","tag":"LastInteraction","tagName":"最后互动时间"},{"createTime":1560845278000,"id":5553,"modifyTime":1560845278000,"sellerId":1000,"tag":"MembershipLevel","tagId":23,"value":2,"valueName":"V3"}],"values":["20190601","20190630"]},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #属性圈人-客户关系-老客亲密度 计算人数接口
    def test_CustomerIntimacy(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":3,"categoryName":"CustomerRelationship","categoryViewName":"客户关系","dateRange":"YES","level":2,"orderSort":3,"parentId":1,"parentName":"属性圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":184,"showType":"SELECTED","tag":"CustomerLifeCycleStage","tagName":"客户生命周期"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":187,"showType":"SELECTED","tag":"CRMMembershipLevel","tagName":"CRM会员等级"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":23,"showType":"SELECTED","tag":"MembershipLevel","tagName":"消费者价值等级"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":24,"showType":"DATE_RANGE","tag":"MemberDate","tagName":"会员注册日期"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":186,"showType":"DATE_RANGE","tag":"LastInteraction","tagName":"最后互动时间"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":1,"showType":"SELECTED","tag":"CustomerIntimacy","tagName":"老客亲密度"},{"dataType":"REGION","dateRange":"NO","disabled":"false","id":16,"showType":"INPUT","tag":"CurrentPoints","tagName":"会员当前积分"}],"tag":"CustomerIntimacy","tagId":1,"dataType":"ENUM","id":5504,"showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":1,"showType":"SELECTED","tag":"CustomerIntimacy","tagName":"老客亲密度"},{"createTime":1560845274000,"id":5504,"modifyTime":1560845274000,"sellerId":1000,"tag":"CustomerIntimacy","tagId":1,"value":2,"valueName":"MP（会员购买）"}],"values":[2]},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #属性圈人-客户关系-会员当前积分 计算人数接口
    def test_CurrentPoints(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":3,"categoryName":"CustomerRelationship","categoryViewName":"客户关系","dateRange":"YES","level":2,"orderSort":3,"parentId":1,"parentName":"属性圈人","values":[{"label":"标签名称","showType":"TAG_AND_VALUE","value":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":184,"showType":"SELECTED","tag":"CustomerLifeCycleStage","tagName":"客户生命周期"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":187,"showType":"SELECTED","tag":"CRMMembershipLevel","tagName":"CRM会员等级"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":23,"showType":"SELECTED","tag":"MembershipLevel","tagName":"消费者价值等级"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":24,"showType":"DATE_RANGE","tag":"MemberDate","tagName":"会员注册日期"},{"dataType":"DATE","dateRange":"NO","disabled":"false","id":186,"showType":"DATE_RANGE","tag":"LastInteraction","tagName":"最后互动时间"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":1,"showType":"SELECTED","tag":"CustomerIntimacy","tagName":"老客亲密度"},{"dataType":"REGION","dateRange":"NO","disabled":"false","id":16,"showType":"INPUT","tag":"CurrentPoints","tagName":"会员当前积分"}],"tag":"CurrentPoints","tagId":16,"dataType":"REGION","id":5504,"showValues":[{"dataType":"REGION","dateRange":"NO","disabled":"false","id":16,"showType":"INPUT","tag":"CurrentPoints","tagName":"会员当前积分"},{"createTime":1560845274000,"id":5504,"modifyTime":1560845274000,"sellerId":1000,"tag":"CustomerIntimacy","tagId":1,"value":2,"valueName":"MP（会员购买）"}],"values":[1],"regionType":"GT"},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0



    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()