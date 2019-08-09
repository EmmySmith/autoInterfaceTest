# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 10:05
# @Author  : renming
# @File    : sendDingDingMessage.py
#!/usr/bin/python
# coding=utf-8

import requests,json


def ddRobot(message):
    #研发中心
    # url = 'https://oapi.dingtalk.com/robot/send?access_token=9e4321caf5329425fe869ec76d5501770c90cd526b1cb805834cc01d34bf0ba5'
    #测试组内部
    # url = 'https://oapi.dingtalk.com/robot/send?access_token=df8d1780fa8ca96c11c95573f452e36729080e2036dc81b390922b06a2606095'
    #调试用
    url = 'https://oapi.dingtalk.com/robot/send?access_token=c08b936af7bc08a69a9fc347099ada832059c999736dfd42a9bb8670d6af3dbb'

    HEADERS = {"Content-Type": "application/json;charset=utf-8"}

    String_textMsg = {
	"msgtype": "text",
        "at": {
            "isAtAll": "true"
        },
	"text": {
		"content": message
	}
}

    String_textMsg = json.dumps(String_textMsg)

    res = requests.post(url, data=String_textMsg, headers=HEADERS)

    print(res.text)

# ddRobot("测试组机器人驾到，请大家欢迎我，谢谢！")