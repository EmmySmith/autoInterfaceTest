#coding=utf-8

# from operate_Excel import *
from common.operate_Excel import *
# import operate_Excel
from common.public import *
# import requests
import json


class testApi(object):
    def __init__(self, method, url, data):
        self.method = method
        self.url = url
        self.data = data


    def testApi(self):
        # 根据不同的访问方式来访问接口
        try:
            if self.method == 'post':
                try:
                    r = requests.post(self.url, data=json.dumps(eval(self.data)),headers=headers)
                    return r
                except Exception as e:
                    print("Fail")
            elif self.method == 'get':
                try:
                    r = requests.get(self.url,headers=headers)
                    return r
                except Exception as e:
                    print("Fail")
        except:
            print('失败')

    def getCode(self):
        # 获取访问接口的状态码
        code = self.testApi().json()['code']
        return code

    def getJson(self):
        # 获取返回信息的json数据
        json_data = self.testApi().text
        # json_data = json.dumps(json.loads(obj), ensure_ascii=False)
        return json_data