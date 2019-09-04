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

class CAP_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-wechat/media/sync/wx90d8a37adac76a84/record"
        print("----------开始测试----------")

    #微信图片素材同步接口
    def test_wechatVoiceSync(self):
        """微信图片素材同步接口"""
        self.url = self.host + self.path
        self.data = {"syncType":"IMAGE"}
        print(self.url)
        response = requests.post(url=self.url,data=json.dumps(self.data),headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    #微信多媒体素材同步接口
    def test_wechatImageSync(self):
        """微信多媒体素材同步接口"""
        self.url = self.host + self.path
        self.data = {"syncType":"MEDIA"}
        print(self.url)
        response = requests.post(url=self.url,data=json.dumps(self.data),headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #微信音频素材同步接口
    def test_wechatMediaSync(self):
        """微信音频素材同步接口"""
        self.url = self.host + self.path
        self.data = {"syncType":"VOICE"}
        print(self.url)
        response = requests.post(url=self.url,data=json.dumps(self.data),headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #微信视频素材同步接口
    def test_wechatVideoSync(self):
        """微信视频素材同步接口"""
        self.url = self.host + self.path
        self.data = {"syncType":"VIDEO"}
        print(self.url)
        response = requests.post(url=self.url,data=json.dumps(self.data),headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #微信图文素材同步接口
    def test_wechatNewsSync(self):
        """微信图文素材同步接口"""
        self.url = self.host + self.path
        self.data = {"syncType":"NEWS"}
        print(self.url)
        response = requests.post(url=self.url,data=json.dumps(self.data),headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()