#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
from common.public import *
from mysqlHandle.common_mysql import *

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path_baseDate = "/api/icem-report/portrait/query/get/portrait/date"
        self.path_categorys = "/api/icem-report/portrait/category/categorys"
        self.path_tags = "/api/icem-report/portrait/category/tags"
        self.sql = "SELECT crowd_id from t_crowd WHERE type = 'UPLOAD' ORDER BY id DESC LIMIT 1;"
        self.dbname = "geek_icem_crowd"
        print("----------开始测试----------")


    #静态人群画像基本信息接口
    def test_staticCrowdPortraitBaseDate(self):
        '''静态人群画像基本信息接口'''
        self.url = self.host + self.path_baseDate
        self.crowd_id = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"crowdId":self.crowd_id}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0
        assert response.json()['body']['crowdId'] == self.crowd_id


    #静态人群画像分类接口
    def test_staticCrowdPortraitCategorys(self):
        '''静态人群画像分类接口'''
        self.url = self.host + self.path_categorys
        self.crowd_id = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"crowdId":self.crowd_id,"init":"ENTER_THE"}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0
        assert response.json()['body'][0]['name'] == "基础信息"

    #静态人群画像基础信息标签接口
    def test_staticCrowdPortraitTags_1(self):
        '''静态人群画像基础信息标签接口'''
        self.url = self.host + self.path_tags
        self.crowd_id = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"crowdId":self.crowd_id,"categoryId":1}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #静态人群画像客户价值标签接口
    def test_staticCrowdPortraitTags_2(self):
        '''静态人群画像客户价值标签接口'''
        self.url = self.host + self.path_tags
        self.crowd_id = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"crowdId":self.crowd_id,"categoryId":2}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #静态人群画像购物偏好标签接口
    def test_staticCrowdPortraitTags_3(self):
        '''静态人群画像购物偏好标签接口'''
        self.url = self.host + self.path_tags
        self.crowd_id = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"crowdId":self.crowd_id,"categoryId":3}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #静态人群画像活动数据标签接口
    def test_staticCrowdPortraitTags_4(self):
        '''静态人群画像活动数据标签接口'''
        self.url = self.host + self.path_tags
        self.crowd_id = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"crowdId":self.crowd_id,"categoryId":4}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #静态人群画像自定义标签接口
    def test_staticCrowdPortraitTags_5(self):
        '''静态人群画像自定义标签接口'''
        self.url = self.host + self.path_tags
        self.crowd_id = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"crowdId":self.crowd_id,"categoryId":5,"page":0,"size":10}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0



    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()