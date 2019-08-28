#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json,time,random
from common.public import *
from mysqlHandle.common_mysql import *

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-sms/template/update"
        # self.random = random.randint(1000,99999)
        self.sql = "SELECT id FROM t_workflow_node_define WHERE node_name = '发短信' ORDER BY id DESC LIMIT 1;"
        self.sql_templete = "SELECT id FROM t_sms_template WHERE `status` = '0' ORDER BY id DESC LIMIT 1;"
        self.dbname = "geek_icem_activity"
        self.dbname_templete = "geek_icem_sms"
        print("----------开始测试----------")


    #更新发短信节点接口
    def test_updateSmsNode(self):
        '''更新发短信节点接口'''
        self.url = self.host + self.path
        self.nodeDefineId = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        self.smsTemplete = DB_ICEM_proc(self.dbname_templete).get_vslues(self.sql_templete)
        # print(self.nodeDefineId)
        data = {"id":self.nodeDefineId,"name":"发短信","signId":2,"templateId":self.smsTemplete,"testNumbers":"13522773597"}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()