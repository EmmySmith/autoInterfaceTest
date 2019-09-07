# -*- coding: utf-8 -*-
# @Time    : 2019-06-17 18:09
# @Author  : Emmy
# @File    : materialGroupSave_test.py


#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import time,random
from common.public import *
from common.commonData import *
from mysqlHandle.common_mysql import *

class CAP_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.sql1 ='select group_id from t_material where is_deleted=0 ORDER BY  id desc LIMIT 1;'
        self.dbname = "geek_icem_component"
        self.path = "/api/icem-component/material/save?appid=2019031863584181"
        print("----------开始测试----------")


    def test_savemicropage(self):
        """保存图片素材"""
        self.url = self.host + self.path
        self.group_id =str(DB_ICEM_proc(self.dbname).get_vslues(self.sql1))
        data = {
            "type": "image",
            "title": "9469669_142840860000_2.jpg",
            "group_id": self.group_id,
            "url": "https://geek-icem.oss-cn-beijing.aliyuncs.com/release/1000/material/d1db5171c5b64e5291026c40d9f97afe.jpg"
        }

        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()