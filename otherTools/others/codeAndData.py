#!/usr/bin/python
# coding=utf-8
import unittest

from parameterized import parameterized

from common.public import *


# from test_demo import test

class SMS_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("----------开始测试----------")
        self.url = "/sms/internal/returnGoods/listByPage"
        pass


    @parameterized.expand(input=search_baosundan.dates())
    #报损单查询接口
    def test_search_baosundan(self,pageNum,pageSize,isAsc,code,msg):
        data = {
        "pageNum": pageNum,
        "pageSize": pageSize,
        "isAsc": isAsc
        }
        # print(datas)
        # path,data = dongTaiPanDian_search()
        new_url = host + self.url
        print(new_url)
        response = requests.post(url=new_url, data=json.dumps(data), headers=headers)
        print(response.text)
        if response.json()['message'] == "操作成功":
            self.assertEqual(response.json()['code'],code)
            self.assertIn(msg,response.json()['message'])
        else:
            self.assertIn(msg,response.json()['message'])


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = SMS_Interface()
    # sms.test_AddBuHuoDan()