#!/usr/bin/python
# coding=utf-8
import unittest
from mysqlHandle.common_mysql import *
import random


class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-system/system/user/save"
        self.random = random.randint(1000,99999)
        print("----------开始测试----------")


    #创建子账户接口接口
    def test_create_subAccount(self):
        self.url = self.host + self.path
        self.userName = "自动化" + str(self.random)
        data = {"userName":self.userName,"password":"0192023a7bbd73250516f069df18b500","realName":"自动化","mobile":"13511111111","status":"TAKE","number":"000007","remark":"000007","roles":[{"createTime":1546063037000,"createUser":"超级管理员","description":"超级管理员-不能删除","id":1,"isDelete":"N","roleName":"root","updateTime":1558082892000}],"merchantId":"1000","merchantName":"林清轩","sellerId":"1000","sellerName":"林清轩"}
        print(self.url)
        print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        self.deleteId = response.json()['id']
        assert response.json()['error'] == 0


    def tearDown(self):
        self.deletePath = "/api/icem-system/system/user/delete"
        self.deleteUrl = self.host + self.deletePath
        deleteData = {"ids":[self.deleteId]}
        res = requests.post(url=self.deleteUrl, data=json.dumps(deleteData), headers=self.headers)
        print(res.text)
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()