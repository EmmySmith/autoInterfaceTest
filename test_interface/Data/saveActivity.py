# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 11:10 AM
# @Author  : Emmy
# @File    : saveActivity.py


import requests
import unittest
import json
from common.public import *
from mysqlHandle.common_mysql import *

class Data_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = "http://10.10.10.53:7042"
        print("----------开始测试----------")


    def test_deleteRole(self):
        """数据接入，活动事实数据"""
        self.path = "/dataAccess/saveActivity"
        self.url = self.host + self.path
        print(self.url)
        data = {
            "actionId": "0",
            "actionName": "1",
            "vtime": 0,
            "ds": "20190920",
            "params": "{\"mobile\":\"18500389830\"}",

        }
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    def test_saveActivityDimension(self):     #缺少activityId、activityName、startTime、endTime 参数必填项
        """数据接入，营销活动维度数据"""
        self.path = "/dataAccess/saveActivityDimension"
        self.url = self.host + self.path
        print(self.url)
        data = {
            "activityId": "1",
            "activityName": "test",
            "startTime": "1568965452000",
            "endTime": "1569051852000",
            "ds": "20190920"
        }
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_saveActivityDimensionDetailn(self):     #缺少activityId、attributeName、attributeValue 参数必填项
        """数据接入，营销活动维度扩展数据"""
        self.path = "/dataAccess/saveActivityDimensionDetail"
        self.url = self.host + self.path
        print(self.url)
        data = {
            "activityId": "1",
            "attributeName":"test",
            "attributeValue":"1",
            "ds": "20190920"
        }
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_saveActivityInfo(self):  # 缺少activityId、time、 参数必填项
        """数据接入，营销活动信息数据"""
        self.path = "/dataAccess/saveActivityInfo"
        self.url = self.host + self.path
        print(self.url)
        data = {
            "activityId": "1",
            "time": "1568965452000",
            # "ds": "20190920"
        }
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_saveConsumerDimension(self):
        """数据接入，存入消费者维度数据"""
        self.path = "/dataAccess/saveConsumerDimension"
        self.url = self.host + self.path
        print(self.url)
        data = {
            "id": "1",
            "cid": "1",
            "crmUid": "1",
            "crmLevel": "1",
            "mobile": "15210046789",
            "macAddress": "1",
            "openId": "1",
            "email": "1",
            "age": 10,
            "sex": "0",
            "birthday": "1996-09-12",
            "province": "beijing",
            "city": "北京",
            "area": "北京",
            "deailAddress": "北京",
            "longitude": 0.0,
            "latitude": 0.0,
            "officialAccounts": "解客",
            "joinChannel": "微信",
            "shopId": "1",
            "activityId": "1",
            "joinDate": "2019-09-12",
            "historyIntegral": 0,
            "integral": 0,
            "wechatCountry": "中国",
            "wechatProvince": "北京",
            "wechatCity": "北京",
            "wechatFocusTime": "2019-09-11",
            "wechatSex": "1",
            "wechatGroup": "1",
            "wechatLanguage": "中文",
            "wechatSource": "搜索",
            "ds": "20190920"
        }
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_saveConsumer(self):
        """数据接入，存入电商平台消费者ID数据"""
        self.path = "/dataAccess/saveConsumer"
        self.url = self.host + self.path
        print(self.url)
        data = {
            "id": "1",
            "cid": "1",
            "platformId": "1",
            "platformUid": "1",
            "mobile": "15210036789",
            "macAddress": "1",
            "openId": "1",
            "email": "1",
            "ds": "20190920"
        }
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_saveConsumerDimensionDetail(self):
        """数据接入，存入消费者扩展维度数据"""
        self.path = "/dataAccess/saveConsumerDimensionDetail"
        self.url = self.host + self.path
        print(self.url)
        data = {
            "id": "1",
            "cid": "1",
            "attributeName": "1",
            "attributeValue": "1",
            "ds": "20190920"
        }
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_saveGoodsDimension(self):
        """数据接入，存入商品维度数据"""
        self.path = "/dataAccess/saveGoodsDimension"
        self.url = self.host + self.path
        print(self.url)
        data = {
            "id": "1",
            "goodsId": "1",
            "goodsSKU": "12",
            "goodsName": "香蕉",
            "categoryId": "1",
            "brand": "Jobn",
            "series": "12",
            "price": 12.0,
            "producingArea": "英国",
            "specifications": "M",
            "ds": "20190920"
        }
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_saveGoodsDimensionDetail(self):
        """数据接入，存入商品扩展维度数据"""
        self.path = "/dataAccess/saveGoodsDimensionDetail"
        self.url = self.host + self.path
        print(self.url)
        data = {"id":"1","goodsId":"1","attributeName":"苹果","attributeValue":"10","ds":"20190920"}
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_saveCategory(self):
        """数据接入，存入品类字典数据"""
        self.path = "/dataAccess/saveCategory"
        self.url = self.host + self.path
        print(self.url)
        data = {"id":"1","categoryId":"1","categoryName":"种类","categoryLevel":"1","categoryLevel1":"1","categoryLevel2":"2","categoryLevel3":"3","categoryLevel4":"4","categoryLevel5":"5","ds":"20190920"}
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_saveOfflineChannelDimension(self):
        """数据接入，存入线下消费渠道维度数据"""
        self.path = "/dataAccess/saveOfflineChannelDimension"
        self.url = self.host + self.path
        print(self.url)
        data = {"shopId":"1","shopName":"雅士利","province":"北京","city":"北京","area":"北京","address":"1","shopCategory":"1","longitude":0.0,"latitude":0.0,"ds":"20190920"}
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_saveOfflineChannelDimensionDetail(self):
        """数据接入，存入线下消费渠道扩展维度数据"""
        self.path = "/dataAccess/saveOfflineChannelDimensionDetail"
        self.url = self.host + self.path
        print(self.url)
        data = {"id":"1","shopId":"1","attributeName":"test","attributeValue":"10","ds":"20190920"}
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_saveOnlineChannelDimension(self):
        """数据接入，存入线上消费渠道维度数据"""
        self.path = "/dataAccess/saveOnlineChannelDimension"
        self.url = self.host + self.path
        print(self.url)
        data = {"channelId":"1","channelName":"test","channelCategory1":"1","channelCategory2":"2","ds":"20190920"}
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_saveOnlineChannelDimensionDetail(self):
        """数据接入，存入线上消费渠道扩展维度数据"""
        self.path = "/dataAccess/saveOnlineChannelDimensionDetail"
        self.url = self.host + self.path
        print(self.url)
        data = {"id":"1","channelId":"1","attributeName":"test","attributeValue":"10","ds":"20190920"}
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_savePurchases(self):
        """数据接入，存入交易事实数据"""
        self.path = "/dataAccess/savePurchases"
        self.url = self.host + self.path
        print(self.url)
        data = {
                "id": "1",
                "channelId": "1",
                "source": "1",
                "price": 0.0,
                "discountPrice": 0.0,
                "payType": "2019-09-20 00:00:00",
                "ticketId": "1",
                "discountType": "1",
                "activityId": "1",
                "payTime": "2019-09-20 00:00:00",
                "uid": "1",
                "name": "1",
                "province": "1",
                "city": "1",
                "area": "1",
                "address": "1",
                "mobile": "1",
                "ds": "20190920"
            }
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_savePurchaseDetail(self):
        """数据接入，存入交易明细事实数据"""
        self.path = "/dataAccess/savePurchaseDetail"
        self.url = self.host + self.path
        print(self.url)
        data = {"id":"1","orderId":"1","goodsId":"1","price":10.0,"payAmount":10.0,"discountAmount":5.0,"count":0,"ds":"20190920"}
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_saveRefound(self):
        """数据接入，存入退单事实数据"""
        self.path = "/dataAccess/saveRefound"
        self.url = self.host + self.path
        print(self.url)
        data = {"id":"1","refoundId":"1234321","orderId":"1234321","refoundSource":"线上","channelId":"1","goodsAmount":10.0,"refoundAmount":5.0,"startTime":"2019-09-01","endTime":"2019-09-11","uid":"1","ds":"20190920"}
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_saveRefoundDetail(self):
        """数据接入，存入退单明细事实数据"""
        self.path = "/dataAccess/saveRefoundDetail"
        self.url = self.host + self.path
        print(self.url)
        data = {"id":"1","refoundId":"1234321","goodsId":"1234321","count":1,"goodsAmount":10.0,"refoundAmount":5.0,"refoundDesc":"1","ds":"20190920"}
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_saveMemberIntegral(self):
        """数据接入，存入积分兑换事实数据"""
        self.path = "/dataAccess/saveMemberIntegral"
        self.url = self.host + self.path
        print(self.url)
        data = {"orderId":"1234321","source":"线上","channelId":"168686","consumeIntegral":10.0,"time":"2019-09-01","uid":"12","ds":"20190920"}
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_saveMemberIntegralDetail(self):
        """数据接入，存入积分兑换明细事实数据"""
        self.path = "/dataAccess/saveMemberIntegralDetail"
        self.url = self.host + self.path
        print(self.url)
        data = {"id":"1","orderId":"1","goodsId":"1","goodsName":"1","count":0,"consumeIntegral":0.0,"ds":"20190920"}
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_saveCrowdData(self):
        """数据接入，存入人群包对应数据"""
        self.path = "/dataAccess/saveCrowdData"
        self.url = self.host + self.path
        print(self.url)
        data = {"id":"1","crowdId":"1","uid":"1","ds":"20190920"}
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_saveTicketDimension(self):
        """数据接入，存入优惠券维度数据"""
        self.path = "/dataAccess/saveTicketDimension"
        self.url = self.host + self.path
        print(self.url)
        data = {"ticketId":"15858","ticketName":"14545","activityId":"1","channelId":"1","channelName":"线上","expirdStartTime":"2019-09-01","expirdEndTime":"2019-12-01","ticketType1":"-1","ticketType2":"-2","cid":"1","status":"1","ds":"20190920"}
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_saveTicketDimensionDetail(self):
        """数据接入，存入优惠券扩展维度数据"""
        self.path = "/dataAccess/saveTicketDimensionDetail"
        self.url = self.host + self.path
        print(self.url)
        data = {"id":"1","ticketId":"1","attributeName":"线上","attributeValue":"1","ds":"20190920"}
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0

    def test_saveConsumerService(self):
        """数据接入，存入客服联络事实数据"""
        self.path = "/dataAccess/saveConsumerService"
        self.url = self.host + self.path
        print(self.url)
        data = {"id":"1","cid":"1","cs1":"1","cs2":"2","cs3":"3","cs4":"4","cs5":"5","cs6":"6","cs7":"7","cs8":"8","cs9":"9","cs10":"10","time":"2019-09-01","channelName":"1","goodsId":"1","orderId":"1","satisfactionDegree":"1","handleType":"1","status":"1","ds":"20190920"}
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0




    def tearDown(self):
        pass

if __name__ == "__main__":
    Send = Data_Interface()