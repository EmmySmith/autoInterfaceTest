# -*- coding: utf-8 -*-
# @Time    : 2019-07-10 10:05
# @Author  : renming
# @File    : materialGroup_test.py


#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
from common.public import *
from mysqlHandle.common_mysql import *

class CAP_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-wechat/material/wx90d8a37adac76a84/local?mediaId="
        self.sql = "SELECT media_id FROM t_media_material_news where deleted IS NULL ORDER BY news_id DESC LIMIT 1;"
        self.dbname = "geek_icem_component"
        print("----------开始测试----------")

    #s删除微信图文
    def test_deleteNews(self):
        """s删除微信图文接口"""
        self.mediaId = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        self.url = self.host + self.path + self.mediaId
        print(self.url)
        response = requests.delete(url=self.url,headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()