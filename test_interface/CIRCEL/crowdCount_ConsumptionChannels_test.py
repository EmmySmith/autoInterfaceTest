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


    #以场圈人-消费渠道 计算人数接口
    def test_ConsumptionChannels(self):
        self.url = self.host + self.path
        data = {"list":[{"categoryId":13,"categoryName":"ConsumeChannel","categoryViewName":"消费渠道","dateRange":"YES","level":2,"orderSort":1,"parentId":12,"parentName":"以场圈人","values":[{"dataType":"ENUM","id":148,"label":"消费渠道","showType":"CONSUMPTION_CHANNEL","tag":"ConsumptionChannel","value":[{"id":6272,"name":"全部门店","tag":"ConsumptionChannel","value":0},{"id":6273,"name":"望京门店","tag":"ConsumptionChannel","value":1},{"id":6274,"name":"三里屯门店","tag":"ConsumptionChannel","value":2},{"id":6275,"name":"不限","tag":"ConsumptionChannel","value":3},{"id":6276,"name":"淘宝旗舰店","tag":"ConsumptionChannel","value":4},{"id":6277,"name":"支付宝小程序","tag":"ConsumptionChannel","value":5},{"id":6278,"name":"不限","tag":"ConsumptionChannel","value":6},{"id":6279,"name":"微信公众号","tag":"ConsumptionChannel","value":7},{"id":6280,"name":"微信小程序","tag":"ConsumptionChannel","value":8},{"id":6281,"name":"不限","tag":"ConsumptionChannel","value":9},{"id":6282,"name":"苹果","tag":"ConsumptionChannel","value":10},{"id":6283,"name":"安卓","tag":"ConsumptionChannel","value":11},{"id":6284,"name":"其他","tag":"ConsumptionChannel","value":12},{"id":6285,"name":"京东","tag":"ConsumptionChannel","value":13},{"id":6286,"name":"其他","tag":"ConsumptionChannel","value":14}],"tagId":148,"showValues":[],"values":[]},{"dataType":"REGION_NESTED","id":146,"label":"频次","showType":"INPUT","tag":"BuyCount","value":[{"id":6265,"maxValue":999,"minValue":0,"name":"不限","tag":"BuyCount"},{"id":6266,"maxValue":999,"minValue":0,"name":"大于","tag":"BuyCount"},{"id":6267,"maxValue":999,"minValue":0,"name":"区间","tag":"BuyCount"}]},{"dataType":"REGION_NESTED","id":147,"label":"消费金额","showType":"RANGE","tag":"BuyValue","value":[{"id":6268,"maxValue":999999,"minValue":0,"tag":"BuyValue"},{"id":6269,"maxValue":999999,"minValue":0,"name":"不限","tag":"BuyValue"},{"id":6270,"maxValue":999999,"minValue":0,"name":"大于","tag":"BuyValue"},{"id":6271,"maxValue":999999,"minValue":0,"name":"区间","tag":"BuyValue"}],"tagId":147,"regionType":"GT","values":[1]},{"dataType":"DATE","id":-1,"label":"时间","showType":"DATE","tag":"JiekeDateTime","value":[{"dataType":"DATE","id":-1,"showType":"DATE"}],"tagId":-1,"showValues":["1"],"values":[360]}]}]}
        print(self.url)
        # print(data)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0



    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()