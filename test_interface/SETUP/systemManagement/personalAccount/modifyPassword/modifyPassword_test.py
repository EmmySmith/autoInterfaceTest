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
        self.path = "/api/icem-system/system/user/reset"

        data = {"id":9999,"oldPassword":"0192023a7bbd73250516f069df18b500","password":"8857c228cef0331fea5621ab9153f4d4"}
        self.url = self.host + self.path
        r = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        # print(r.text)
        print("----------开始测试----------")


    #修改登录密码接口
    def test_modify_password(self):
        self.url = self.host + self.path
        data = {"id":9999,"oldPassword":"8857c228cef0331fea5621ab9153f4d4","password":"0192023a7bbd73250516f069df18b500"}
        print(self.url)
        print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()