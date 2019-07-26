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
        self.path_infoByStatistic = "/api/icem-crowd/crowd/infoByStatistic"
        self.path_list = "/api/icem-report/crowd/job/list"
        self.path_getViews = "/api/icem-report/crowd/getViews"
        self.path_views = "/api/icem-report/crowd/charts/views"
        self.sql = "SELECT id FROM t_crowd WHERE crowd_name = '嘎嘎嘎';"
        self.sql_jobId = "SELECT id FROM t_crowd_statistic_job WHERE crowd_id = '1519';"
        self.dbname = "geek_dmp_api"
        print("----------开始测试----------")


    #静态人群绩效基本信息接口
    def test_staticCrowdAchievementsInfoByStatistic(self):
        '''静态人群绩效基本信息接口'''
        self.url = self.host + self.path_infoByStatistic
        self.crowd_id = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"id":self.crowd_id}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    #静态人群绩效列表接口
    def test_staticCrowdAchievementsList(self):
        '''静态人群绩效列表接口'''
        self.url = self.host + self.path_list
        self.crowd_id = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"crowdId":self.crowd_id}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #静态人群画像基础信息标签接口
    def test_staticCrowdAchievementsTags_1(self):
        '''静态人群画像基础信息标签接口'''
        self.url = self.host + self.path_getViews
        self.crowd_id = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"jobId":40,"crowdId":self.crowd_id,"endTime":"2018-06-30","startTime":"2018-06-01"}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #静态人群画像客户价值标签接口
    def test_staticCrowdAchievementsTags_2(self):
        '''静态人群画像客户价值标签接口'''
        self.url = self.host + self.path_views
        self.crowd_id = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"jobId":40,"crowdId":1519,"endTime":"2018-06-30","startTime":"2018-06-01"}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #静态人群画像购物偏好标签接口
    def test_staticCrowdAchievementsTags_3(self):
        '''静态人群画像购物偏好标签接口'''
        self.url = self.host + self.path_infoByStatistic
        self.crowd_id = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"id":self.crowd_id}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()