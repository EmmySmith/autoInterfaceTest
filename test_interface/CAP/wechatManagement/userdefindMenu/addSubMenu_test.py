# -*- coding: utf-8 -*-
# @Time    : 2019-07-10 10:05
# @Author  : renming
# @File    : materialGroup_test.py


#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json,random
from common.public import *

class CAP_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-wechat/menu/wx90d8a37adac76a84/common"
        self.random = random.randint(1000,99999)
        print("----------开始测试----------")

    #添加子菜单接口(发送消息)
    def test_addSubMenu_sendMessage(self):
        """添加子菜单接口(发送消息)"""
        self.url = self.host + self.path
        self.name_sendMessage = "发送消息" + str(self.random)
        self.data = {"buttons":[{"key":"image","mediaId":"DOAWRCrqeMpRgLFG2vz59JllAQc5-5FMvdKjyBGfT5U","name":"活动","pagePath":"{\"authorizerAppid\":\"wx59ff50e404b28528\",\"createTime\":1556576612000,\"deleted\":0,\"digest\":\"2121\",\"groupId\":0,\"materialId\":11,\"mediaId\":\"DOAWRCrqeMpRgLFG2vz59JllAQc5-5FMvdKjyBGfT5U\",\"merchantId\":1000,\"tags\":\"21\",\"title\":\"video_01\",\"type\":\"video\",\"updateTime\":\"2019-04-30 06:23:50\",\"url\":\"http://203.205.158.76/vweixinp.tc.qq.com/1007_7941e33e0734409a81497a8cfd5a5589.f10.mp4?vkey=D0561C290EA8B185FFD1666DE46018AC6EAAAF7CA5DF53F3094E18A5B901DDB6FE28FE7CB6664561728370E3667303EDDF5A2CB86701F58BA1E7064E2F71A9A27B9EB65BF563ABB2C2AB55202E41F232ABFF6FF8F3192861&sha=0&save=1\"}","subButtons":[{"key":"news","mediaId":"DOAWRCrqeMpRgLFG2vz59A4xYTi3TZeoVeSyqZoijH8","name":"新建子菜单","pagePath":"{\"author\":\"\",\"cardIds\":[\"pCcPm1S9QQcjUrkLus5hfJJ32VmI\"],\"contentSourceUrl\":\"\",\"createTime\":1563221072000,\"digest\":\"\\n\",\"index\":0,\"materialId\":96,\"mediaId\":\"DOAWRCrqeMpRgLFG2vz59A4xYTi3TZeoVeSyqZoijH8\",\"merchantId\":1000,\"needOpenComment\":false,\"newsId\":30,\"onlyFansCanComment\":false,\"showCoverPic\":false,\"thumbMediaId\":\"DOAWRCrqeMpRgLFG2vz59E-cPhKWZBHgAJHc4FNMcYg\",\"thumbUrl\":\"http://mmbiz.qpic.cn/mmbiz_jpg/6t02nhib99h9At3Su0XeYibG6DoLCV19icbst167Cq1O9Vq5XXnUQPcbItbicwZH8OAwsa4Z1ZRwGt3Oia2ia3ctWLIg/0?wx_fmt=jpeg\",\"title\":\"715测试\",\"updateTime\":1563221072000,\"url\":\"http://mp.weixin.qq.com/s?__biz=MzU4ODY3MDIxNw==&mid=100000085&idx=1&sn=75d8ca1d8a184accc6d5653ec7a5a02e&chksm=7dd875334aaffc25fe869a528f4e8b621a9e817d192777557e7e2d1461ac1247352eca4502ff#rd\"}","subButtons":[],"type":"view","url":"https://icem-qa-fix.jiekecloud.cn/modular/#/micropage/5d3fbd56e506653f42a74dae?sid=1000&appid=wx59ff50e404b28528"}],"type":"media_id","url":"https://icem-dev-fix.jiekecloud.cn/modular/#/micropage/5d1b2f69e506651307314149?sid=1000&appid=wx59ff50e404b28528"},{"key":"news","mediaId":"DOAWRCrqeMpRgLFG2vz59JFqFThPStZLfNjxuCHT0mk","name":"我的","pagePath":"{\"author\":\"\",\"cardIds\":[\"pCcPm1cOTkPokozXHq2RPTUTOWLU\"],\"contentSourceUrl\":\"\",\"createTime\":1563318204000,\"digest\":\"\\n\",\"index\":0,\"materialId\":97,\"mediaId\":\"DOAWRCrqeMpRgLFG2vz59JFqFThPStZLfNjxuCHT0mk\",\"merchantId\":1000,\"needOpenComment\":false,\"newsId\":31,\"onlyFansCanComment\":false,\"showCoverPic\":false,\"thumbMediaId\":\"DOAWRCrqeMpRgLFG2vz59P6CmHthWv51cikxbW9OoBU\",\"thumbUrl\":\"http://mmbiz.qpic.cn/mmbiz_png/6t02nhib99h8qicHou7DFwvR4w4tgE9HGDQtniam6q3A2ALqiaNmfwjdQichqXxDpRhUV3CPadBNxbPZIjb9m1Gs0Fg/0?wx_fmt=png\",\"title\":\"716测试\",\"updateTime\":1563318204000,\"url\":\"http://mp.weixin.qq.com/s?__biz=MzU4ODY3MDIxNw==&mid=100000086&idx=1&sn=73f248a4d059ea8454ac5b77506fa6cd&chksm=7dd875304aaffc26872746c28c06283fff54b73a78d22a146363a8b9c5f48f48e9461ad6a020#rd\"}","subButtons":[{"key":"image","name":"新建子菜单","subButtons":[],"type":"view","url":"https://icem-qa-fix.jiekecloud.cn/modular/#/micropage/5d3bfe9be506653f42a74d9f?sid=1000&appid=wx59ff50e404b28528"},{"appId":"","key":"news","mediaId":"","name":"测试授权","pagePath":"","subButtons":[],"type":"view","url":"https://icem-qa-fix.jiekecloud.cn/modular/micropage/5d639eaae506657d4dad2b5b?sid=1000&appid=wx90d8a37adac76a84&channelCode=guanfang&channelName=通用渠道"}],"type":"media_id"},{"type":"","name":"新建菜单","key":"news","mediaId":"","appId":"","pagePath":"","subButtons":[{"type":"media_id","name":self.name_sendMessage,"key":"news","mediaId":"l9Nxln_NQF5SG96148pY4HoQ_wBTqDqP7cv_oW7huDU","appId":"","pagePath":""}]}]}
        print(self.url)
        response = requests.post(url=self.url,data=json.dumps(self.data),headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #添加子菜单接口(跳转网页)
    def test_addSubMenu_jumpPages(self):
        """添加子菜单接口(跳转网页)"""
        self.url = self.host + self.path
        self.name_jumpPages = "跳转网页" + str(self.random)
        self.data = {"buttons":[{"key":"image","mediaId":"DOAWRCrqeMpRgLFG2vz59JllAQc5-5FMvdKjyBGfT5U","name":"活动","pagePath":"{\"authorizerAppid\":\"wx59ff50e404b28528\",\"createTime\":1556576612000,\"deleted\":0,\"digest\":\"2121\",\"groupId\":0,\"materialId\":11,\"mediaId\":\"DOAWRCrqeMpRgLFG2vz59JllAQc5-5FMvdKjyBGfT5U\",\"merchantId\":1000,\"tags\":\"21\",\"title\":\"video_01\",\"type\":\"video\",\"updateTime\":\"2019-04-30 06:23:50\",\"url\":\"http://203.205.158.76/vweixinp.tc.qq.com/1007_7941e33e0734409a81497a8cfd5a5589.f10.mp4?vkey=D0561C290EA8B185FFD1666DE46018AC6EAAAF7CA5DF53F3094E18A5B901DDB6FE28FE7CB6664561728370E3667303EDDF5A2CB86701F58BA1E7064E2F71A9A27B9EB65BF563ABB2C2AB55202E41F232ABFF6FF8F3192861&sha=0&save=1\"}","subButtons":[{"key":"news","mediaId":"DOAWRCrqeMpRgLFG2vz59A4xYTi3TZeoVeSyqZoijH8","name":"新建子菜单","pagePath":"{\"author\":\"\",\"cardIds\":[\"pCcPm1S9QQcjUrkLus5hfJJ32VmI\"],\"contentSourceUrl\":\"\",\"createTime\":1563221072000,\"digest\":\"\\n\",\"index\":0,\"materialId\":96,\"mediaId\":\"DOAWRCrqeMpRgLFG2vz59A4xYTi3TZeoVeSyqZoijH8\",\"merchantId\":1000,\"needOpenComment\":false,\"newsId\":30,\"onlyFansCanComment\":false,\"showCoverPic\":false,\"thumbMediaId\":\"DOAWRCrqeMpRgLFG2vz59E-cPhKWZBHgAJHc4FNMcYg\",\"thumbUrl\":\"http://mmbiz.qpic.cn/mmbiz_jpg/6t02nhib99h9At3Su0XeYibG6DoLCV19icbst167Cq1O9Vq5XXnUQPcbItbicwZH8OAwsa4Z1ZRwGt3Oia2ia3ctWLIg/0?wx_fmt=jpeg\",\"title\":\"715测试\",\"updateTime\":1563221072000,\"url\":\"http://mp.weixin.qq.com/s?__biz=MzU4ODY3MDIxNw==&mid=100000085&idx=1&sn=75d8ca1d8a184accc6d5653ec7a5a02e&chksm=7dd875334aaffc25fe869a528f4e8b621a9e817d192777557e7e2d1461ac1247352eca4502ff#rd\"}","subButtons":[],"type":"view","url":"https://icem-qa-fix.jiekecloud.cn/modular/#/micropage/5d3fbd56e506653f42a74dae?sid=1000&appid=wx59ff50e404b28528"}],"type":"media_id","url":"https://icem-dev-fix.jiekecloud.cn/modular/#/micropage/5d1b2f69e506651307314149?sid=1000&appid=wx59ff50e404b28528"},{"key":"news","mediaId":"DOAWRCrqeMpRgLFG2vz59JFqFThPStZLfNjxuCHT0mk","name":"我的","pagePath":"{\"author\":\"\",\"cardIds\":[\"pCcPm1cOTkPokozXHq2RPTUTOWLU\"],\"contentSourceUrl\":\"\",\"createTime\":1563318204000,\"digest\":\"\\n\",\"index\":0,\"materialId\":97,\"mediaId\":\"DOAWRCrqeMpRgLFG2vz59JFqFThPStZLfNjxuCHT0mk\",\"merchantId\":1000,\"needOpenComment\":false,\"newsId\":31,\"onlyFansCanComment\":false,\"showCoverPic\":false,\"thumbMediaId\":\"DOAWRCrqeMpRgLFG2vz59P6CmHthWv51cikxbW9OoBU\",\"thumbUrl\":\"http://mmbiz.qpic.cn/mmbiz_png/6t02nhib99h8qicHou7DFwvR4w4tgE9HGDQtniam6q3A2ALqiaNmfwjdQichqXxDpRhUV3CPadBNxbPZIjb9m1Gs0Fg/0?wx_fmt=png\",\"title\":\"716测试\",\"updateTime\":1563318204000,\"url\":\"http://mp.weixin.qq.com/s?__biz=MzU4ODY3MDIxNw==&mid=100000086&idx=1&sn=73f248a4d059ea8454ac5b77506fa6cd&chksm=7dd875304aaffc26872746c28c06283fff54b73a78d22a146363a8b9c5f48f48e9461ad6a020#rd\"}","subButtons":[{"key":"image","name":"新建子菜单","subButtons":[],"type":"view","url":"https://icem-qa-fix.jiekecloud.cn/modular/#/micropage/5d3bfe9be506653f42a74d9f?sid=1000&appid=wx59ff50e404b28528"},{"appId":"","key":"news","mediaId":"","name":"测试授权","pagePath":"","subButtons":[],"type":"view","url":"https://icem-qa-fix.jiekecloud.cn/modular/micropage/5d639eaae506657d4dad2b5b?sid=1000&appid=wx90d8a37adac76a84&channelCode=guanfang&channelName=通用渠道"}],"type":"media_id"},{"appId":"","key":"news","mediaId":"","name":"新建菜单","pagePath":"","subButtons":[{"appId":"","key":"news","mediaId":"l9Nxln_NQF5SG96148pY4HoQ_wBTqDqP7cv_oW7huDU","name":"得低调点","pagePath":"","subButtons":[],"type":"media_id"},{"type":"view","name":self.name_jumpPages,"key":"news","mediaId":"","appId":"","pagePath":"","url":"https://icem-qa-fix.jiekecloud.cn/modular/micropage/5d6cb1e3e506653d7aefaa6f?sid=1000&appid=wx90d8a37adac76a84&channelCode=guanfang&channelName=通用渠道"}],"type":""}]}
        print(self.url)
        response = requests.post(url=self.url,data=json.dumps(self.data),headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = CAP_Interface()