#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
from common.public import *
from common.login import *
import os
from requests_toolbelt import MultipartEncoder

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers_fileUpload
        self.host = host
        self.path = "/api/icem-resource/file/upload"
        print("----------开始测试----------")


    #文件上传接口
    def test_fileUpload(self):
        self.url = self.host + self.path
        # data = {"file":"","module":""}
        parpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # 定位当前文件夹
        pngpath = os.path.join(parpath, 'couponManagement', '2.jpg')  # “testdata”：存放文件的文件夹
        f = {
            "module": ("couponDetail", "1.png"),
            "file": ("1.png", open("D:\\autoInterfaceTest\\test_interface\\MA\\loyaltyManagement\\couponManagement\\1.png", "rb"), "image/png")
        }
        # print(self.url)
        # m = MultipartEncoder(f)
        # self.headers['Content-Type'] = m.content_type
        response = requests.post(url=self.url,data=f,headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()