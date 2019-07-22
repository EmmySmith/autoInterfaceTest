# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 5:25 PM
# @Author  : Emmy

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
        self.path = "/api/icem-interaction/activity/info"
        self.sql = 'select id from t_interact_activity t where t.defl=0 ORDER BY id desc limit 1'
        self.dbname = "geek_icem_interaction"
        print("----------开始测试----------")


    def test_materialDelete(self):
        """删除活动"""
        self.url = self.host + self.path
        activityId = str(DB_ICEM_proc(self.dbname).get_vslues(self.sql))

        data = {
            "id":activityId
        }
        print(activityId)

        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0



    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()