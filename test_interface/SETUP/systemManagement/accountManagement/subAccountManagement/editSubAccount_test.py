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
        self.dbname = "geek_icem_system"
        self.sql = "SELECT id FROM t_user WHERE is_delete != 'Y' AND real_name != '超级管理员' AND id != '9999' ORDER BY id DESC LIMIT 1;"
        print("----------开始测试----------")


    #编辑子账户接口接口
    def test_edit_subAccount(self):
        self.url = self.host + self.path
        self.userName = "自动化修改" + str(self.random)
        self.userId = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        data = {"prefix":"lqx","userName":self.userName,"password":"d41d8cd98f00b204e9800998ecf8427e","realName":"任明","mobile":"13500000000","status":"TAKE","number":"111111","remark":"111111","roles":[{"createTime":1546063037000,"createUser":"超级管理员","description":"超级管理员-不能删除","id":1,"isDelete":"N","roleName":"root","updateTime":1558082892000},{"createTime":1558331930000,"createUser":"超级管理员","description":"超级","id":8,"isDelete":"N","roleName":"超级","updateTime":1558331930000}],"merchantId":1000,"merchantName":"林清轩","sellerId":1000,"sellerName":"林清轩","id":str(self.userId)}
        print(self.url)
        print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()