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


    #以货圈人-商品圈人-产品系列 计算人数接口
    def test_ProductSeries(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":11,"categoryName":"SelectedByProducts","categoryViewName":"商品圈人","dateRange":"YES","level":2,"orderSort":1,"parentId":10,"parentName":"以货圈人","values":[{"dataType":"ENUM_NESTED","id":100003,"label":"商品属性","showType":"SELECT_SELECT","tag":"Series","value":[{"id":8168,"name":"山茶花修复系列","tag":"Series","value":0},{"id":8169,"name":"芦荟系列","tag":"Series","value":1},{"id":8170,"name":"红石榴焕亮系列","tag":"Series","value":2},{"id":8171,"name":"香橙系列","tag":"Series","value":3},{"id":8172,"name":"海藻补水系列","tag":"Series","value":4},{"id":8173,"name":"睡莲系列","tag":"Series","value":5},{"id":8174,"name":"生姜系列","tag":"Series","value":6},{"id":8175,"name":"其他","tag":"Series","value":7}],"tagId":109,"showValues":[{"id":"series","name":"产品系列"},{"id":100003,"name":"山茶花时光修复系列(CC54)"}],"values":[100003]},{"dataType":"ENUM","id":141,"label":"购买渠道","showType":"CONSUMPTION_CHANNEL","tag":"ConsumptionChannel","value":[{"id":8354,"name":"全部门店","tag":"ConsumptionChannel","value":0},{"id":8355,"name":"望京门店","tag":"ConsumptionChannel","value":1},{"id":8356,"name":"三里屯门店","tag":"ConsumptionChannel","value":2},{"id":8357,"name":"不限","tag":"ConsumptionChannel","value":3},{"id":8358,"name":"淘宝旗舰店","tag":"ConsumptionChannel","value":4},{"id":8359,"name":"支付宝小程序","tag":"ConsumptionChannel","value":5},{"id":8360,"name":"不限","tag":"ConsumptionChannel","value":6},{"id":8361,"name":"微信公众号","tag":"ConsumptionChannel","value":7},{"id":8362,"name":"微信小程序","tag":"ConsumptionChannel","value":8},{"id":8363,"name":"不限","tag":"ConsumptionChannel","value":9},{"id":8364,"name":"苹果","tag":"ConsumptionChannel","value":10},{"id":8365,"name":"安卓","tag":"ConsumptionChannel","value":11},{"id":8366,"name":"其他","tag":"ConsumptionChannel","value":12},{"id":8367,"name":"京东","tag":"ConsumptionChannel","value":13},{"id":8368,"name":"其他","tag":"ConsumptionChannel","value":14}],"tagId":141,"showValues":[],"values":[]},{"dataType":"ENUM","id":143,"label":"商品ID","showType":"SELECT_INPUT","tag":"ProductID","value":[{"id":8380,"name":"所有商品","tag":"ProductID","value":0},{"id":8381,"name":"指定商品ID","tag":"ProductID","value":1}],"tagId":143,"values":[]},{"dataType":"REGION_NESTED","id":144,"label":"频次","showType":"INPUT","tag":"BuyCount","value":[{"id":8382,"maxValue":999,"minValue":0,"name":"不限","tag":"BuyCount"},{"id":8383,"maxValue":999,"minValue":0,"name":"大于","tag":"BuyCount"},{"id":8384,"maxValue":999,"minValue":0,"name":"区间","tag":"BuyCount"}]},{"dataType":"REGION_NESTED","id":145,"label":"消费金额","showType":"RANGE","tag":"BuyValue","value":[{"id":8385,"maxValue":999999,"minValue":0,"tag":"BuyValue"},{"id":8386,"maxValue":999999,"minValue":0,"name":"不限","tag":"BuyValue"},{"id":8387,"maxValue":999999,"minValue":0,"name":"大于","tag":"BuyValue"},{"id":8388,"maxValue":999999,"minValue":0,"name":"区间","tag":"BuyValue"}],"tagId":145,"regionType":"GT","values":[1]},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}],"tagId":-1,"showValues":["1"],"values":[360]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0



    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()