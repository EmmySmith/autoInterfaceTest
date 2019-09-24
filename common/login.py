#!/usr/bin/python
# coding=utf-8

import requests
import json
import urllib.request,re


def login(host,userName,password):
    url = host + "/api/icem-system/system/user/login"
    data = {
	"userName": userName,
	"password": password
}
    headers = {
	"content-type": "application/json;charset=UTF-8"
}
    r = requests.post(url=url,data=json.dumps(data),headers=headers)
    # print(r.text)
    # response = urllib.request.urlopen(r)
    # data = response.read()
    # regx = '.*"token":"(.*)","ud"'
    # pm = re.search(regx, data)  # 取 token 匹配值
    # token = pm.group(1)  # 如果匹配到， 则返回 token 值

    token = r.json()['body']['token']
    Authorization = "Bearer " + token
    # print(Authorization)
    return Authorization

# login("https://icem-qa-fix.jiekecloud.cn","lqx:admin_lqx","0192023a7bbd73250516f069df18b500")