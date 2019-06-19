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
        self.path = "/api/icem-crowd/crowd/count"
        print("----------开始测试----------")


    #以场圈人-地理位置-省份 计算人数接口
    def test_Province(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":14,"categoryName":"Location","categoryViewName":"地理位置","dateRange":"NO","level":2,"orderSort":2,"parentId":12,"parentName":"以场圈人","values":[{"label":"标签名称","showType":"CITY","value":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":202,"showType":"CITY","tag":"Province","tagName":"省份"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":203,"showType":"CITY","tag":"City","tagName":"城市"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":204,"showType":"CITY","tag":"District","tagName":"区"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":205,"showType":"CITY","tag":"ProvinceOffline","tagName":"省份-线下"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":206,"showType":"CITY","tag":"CityOffline","tagName":"城市-线下"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":207,"showType":"CITY","tag":"ProvinceOnline","tagName":"省份-线上"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":208,"showType":"CITY","tag":"CityOnline","tagName":"城市-线上"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":209,"showType":"CITY","tag":"MainStore","tagName":"主要消费门店"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":210,"showType":"CITY","tag":"SecondaryStore","tagName":"次要消费门店"}],"tag":"Province","dataType":"ENUM","tagId":202,"showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":202,"showType":"CITY","tag":"Province","tagName":"省份"},110000,"","",[]],"values":[110000]}]}]}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #以场圈人-地理位置-城市 计算人数接口
    def test_City(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":14,"categoryName":"Location","categoryViewName":"地理位置","dateRange":"NO","level":2,"orderSort":2,"parentId":12,"parentName":"以场圈人","values":[{"label":"标签名称","showType":"CITY","value":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":202,"showType":"CITY","tag":"Province","tagName":"省份"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":203,"showType":"CITY","tag":"City","tagName":"城市"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":204,"showType":"CITY","tag":"District","tagName":"区"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":205,"showType":"CITY","tag":"ProvinceOffline","tagName":"省份-线下"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":206,"showType":"CITY","tag":"CityOffline","tagName":"城市-线下"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":207,"showType":"CITY","tag":"ProvinceOnline","tagName":"省份-线上"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":208,"showType":"CITY","tag":"CityOnline","tagName":"城市-线上"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":209,"showType":"CITY","tag":"MainStore","tagName":"主要消费门店"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":210,"showType":"CITY","tag":"SecondaryStore","tagName":"次要消费门店"}],"tag":"City","dataType":"ENUM","tagId":203,"showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":203,"showType":"CITY","tag":"City","tagName":"城市"},110000,110100,"",[]],"values":[110100]}]}]}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #以场圈人-地理位置-区 计算人数接口
    def test_District(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":14,"categoryName":"Location","categoryViewName":"地理位置","dateRange":"NO","level":2,"orderSort":2,"parentId":12,"parentName":"以场圈人","values":[{"label":"标签名称","showType":"CITY","value":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":202,"showType":"CITY","tag":"Province","tagName":"省份"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":203,"showType":"CITY","tag":"City","tagName":"城市"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":204,"showType":"CITY","tag":"District","tagName":"区"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":205,"showType":"CITY","tag":"ProvinceOffline","tagName":"省份-线下"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":206,"showType":"CITY","tag":"CityOffline","tagName":"城市-线下"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":207,"showType":"CITY","tag":"ProvinceOnline","tagName":"省份-线上"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":208,"showType":"CITY","tag":"CityOnline","tagName":"城市-线上"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":209,"showType":"CITY","tag":"MainStore","tagName":"主要消费门店"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":210,"showType":"CITY","tag":"SecondaryStore","tagName":"次要消费门店"}],"tag":"District","dataType":"ENUM","tagId":204,"showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":204,"showType":"CITY","tag":"District","tagName":"区"},110000,110100,110108,[]],"values":[110108]}]}]}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #以场圈人-地理位置-省份-线下 计算人数接口
    def test_ProvinceOffline(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":14,"categoryName":"Location","categoryViewName":"地理位置","dateRange":"NO","level":2,"orderSort":2,"parentId":12,"parentName":"以场圈人","values":[{"label":"标签名称","showType":"CITY","value":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":202,"showType":"CITY","tag":"Province","tagName":"省份"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":203,"showType":"CITY","tag":"City","tagName":"城市"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":204,"showType":"CITY","tag":"District","tagName":"区"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":205,"showType":"CITY","tag":"ProvinceOffline","tagName":"省份-线下"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":206,"showType":"CITY","tag":"CityOffline","tagName":"城市-线下"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":207,"showType":"CITY","tag":"ProvinceOnline","tagName":"省份-线上"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":208,"showType":"CITY","tag":"CityOnline","tagName":"城市-线上"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":209,"showType":"CITY","tag":"MainStore","tagName":"主要消费门店"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":210,"showType":"CITY","tag":"SecondaryStore","tagName":"次要消费门店"}],"tag":"ProvinceOffline","dataType":"ENUM","tagId":205,"showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":205,"showType":"CITY","tag":"ProvinceOffline","tagName":"省份-线下"},110000,110100,"",[]],"values":[110000]}]}]}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #以场圈人-地理位置-省份-线上 计算人数接口
    def test_ProvinceOnline(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":14,"categoryName":"Location","categoryViewName":"地理位置","dateRange":"NO","level":2,"orderSort":2,"parentId":12,"parentName":"以场圈人","values":[{"label":"标签名称","showType":"CITY","value":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":202,"showType":"CITY","tag":"Province","tagName":"省份"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":203,"showType":"CITY","tag":"City","tagName":"城市"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":204,"showType":"CITY","tag":"District","tagName":"区"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":205,"showType":"CITY","tag":"ProvinceOffline","tagName":"省份-线下"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":206,"showType":"CITY","tag":"CityOffline","tagName":"城市-线下"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":207,"showType":"CITY","tag":"ProvinceOnline","tagName":"省份-线上"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":208,"showType":"CITY","tag":"CityOnline","tagName":"城市-线上"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":209,"showType":"CITY","tag":"MainStore","tagName":"主要消费门店"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":210,"showType":"CITY","tag":"SecondaryStore","tagName":"次要消费门店"}],"tag":"ProvinceOnline","dataType":"ENUM","tagId":207,"showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":207,"showType":"CITY","tag":"ProvinceOnline","tagName":"省份-线上"},110000,110100,"",[]],"values":[110000]}]}]}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #以场圈人-地理位置-城市-线下 计算人数接口
    def test_CityOffline(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":14,"categoryName":"Location","categoryViewName":"地理位置","dateRange":"NO","level":2,"orderSort":2,"parentId":12,"parentName":"以场圈人","values":[{"label":"标签名称","showType":"CITY","value":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":202,"showType":"CITY","tag":"Province","tagName":"省份"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":203,"showType":"CITY","tag":"City","tagName":"城市"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":204,"showType":"CITY","tag":"District","tagName":"区"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":205,"showType":"CITY","tag":"ProvinceOffline","tagName":"省份-线下"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":206,"showType":"CITY","tag":"CityOffline","tagName":"城市-线下"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":207,"showType":"CITY","tag":"ProvinceOnline","tagName":"省份-线上"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":208,"showType":"CITY","tag":"CityOnline","tagName":"城市-线上"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":209,"showType":"CITY","tag":"MainStore","tagName":"主要消费门店"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":210,"showType":"CITY","tag":"SecondaryStore","tagName":"次要消费门店"}],"tag":"CityOffline","dataType":"ENUM","tagId":206,"showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":206,"showType":"CITY","tag":"CityOffline","tagName":"城市-线下"},110000,110100,"",[]],"values":[110100]}]}]}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #以场圈人-地理位置-城市-线上 计算人数接口
    def test_CityOnline(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":14,"categoryName":"Location","categoryViewName":"地理位置","dateRange":"NO","level":2,"orderSort":2,"parentId":12,"parentName":"以场圈人","values":[{"label":"标签名称","showType":"CITY","value":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":202,"showType":"CITY","tag":"Province","tagName":"省份"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":203,"showType":"CITY","tag":"City","tagName":"城市"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":204,"showType":"CITY","tag":"District","tagName":"区"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":205,"showType":"CITY","tag":"ProvinceOffline","tagName":"省份-线下"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":206,"showType":"CITY","tag":"CityOffline","tagName":"城市-线下"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":207,"showType":"CITY","tag":"ProvinceOnline","tagName":"省份-线上"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":208,"showType":"CITY","tag":"CityOnline","tagName":"城市-线上"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":209,"showType":"CITY","tag":"MainStore","tagName":"主要消费门店"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":210,"showType":"CITY","tag":"SecondaryStore","tagName":"次要消费门店"}],"tag":"CityOnline","dataType":"ENUM","tagId":208,"showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":208,"showType":"CITY","tag":"CityOnline","tagName":"城市-线上"},130000,130100,"",[]],"values":[130100]}]}]}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #以场圈人-地理位置-城市-主要消费门店 计算人数接口
    def test_MainStore(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":14,"categoryName":"Location","categoryViewName":"地理位置","dateRange":"NO","level":2,"orderSort":2,"parentId":12,"parentName":"以场圈人","values":[{"label":"标签名称","showType":"CITY","value":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":202,"showType":"CITY","tag":"Province","tagName":"省份"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":203,"showType":"CITY","tag":"City","tagName":"城市"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":204,"showType":"CITY","tag":"District","tagName":"区"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":205,"showType":"CITY","tag":"ProvinceOffline","tagName":"省份-线下"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":206,"showType":"CITY","tag":"CityOffline","tagName":"城市-线下"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":207,"showType":"CITY","tag":"ProvinceOnline","tagName":"省份-线上"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":208,"showType":"CITY","tag":"CityOnline","tagName":"城市-线上"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":209,"showType":"CITY","tag":"MainStore","tagName":"主要消费门店"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":210,"showType":"CITY","tag":"SecondaryStore","tagName":"次要消费门店"}],"tag":"MainStore","dataType":"ENUM","tagId":209,"showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":209,"showType":"CITY","tag":"MainStore","tagName":"主要消费门店"},110000,110100,"",[100003]],"values":[100003]}]}]}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    #以场圈人-地理位置-城市-次要消费门店 计算人数接口
    def test_SecondaryStore(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":14,"categoryName":"Location","categoryViewName":"地理位置","dateRange":"NO","level":2,"orderSort":2,"parentId":12,"parentName":"以场圈人","values":[{"label":"标签名称","showType":"CITY","value":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":202,"showType":"CITY","tag":"Province","tagName":"省份"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":203,"showType":"CITY","tag":"City","tagName":"城市"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":204,"showType":"CITY","tag":"District","tagName":"区"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":205,"showType":"CITY","tag":"ProvinceOffline","tagName":"省份-线下"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":206,"showType":"CITY","tag":"CityOffline","tagName":"城市-线下"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":207,"showType":"CITY","tag":"ProvinceOnline","tagName":"省份-线上"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":208,"showType":"CITY","tag":"CityOnline","tagName":"城市-线上"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":209,"showType":"CITY","tag":"MainStore","tagName":"主要消费门店"},{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":210,"showType":"CITY","tag":"SecondaryStore","tagName":"次要消费门店"}],"tag":"SecondaryStore","dataType":"ENUM","tagId":210,"showValues":[{"dataType":"ENUM","dateRange":"NO","disabled":"false","id":210,"showType":"CITY","tag":"SecondaryStore","tagName":"次要消费门店"},110000,110100,"",[100003]],"values":[100003]}]}]}
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0




    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()