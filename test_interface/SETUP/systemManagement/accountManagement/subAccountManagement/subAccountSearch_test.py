#!/usr/bin/python
# coding=utf-8
import unittest
from mysqlHandle.common_mysql import *


class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-system/system/users?page=0&size=20"
        print("----------开始测试----------")


    #子账户查询接口
    def test_subAccount_search(self):
        self.url = self.host + self.path
        data = {"page":0,"size":20}
        print(self.url)
        print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['content'] != "null"


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()