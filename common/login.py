#!/usr/bin/python
# coding=utf-8

import requests
import json

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
    token = r.json()['body']['token']
    Authorization = "Bearer " + token
    # print(Authorization)
    return Authorization

# login("https://icem-qa-fix.jiekecloud.cn","admin_lqx","0192023a7bbd73250516f069df18b500")