#coding=utf-8
import requests
import json

#接口公共参数
host = 'https://icem-qa-fix.jiekecloud.cn'
host_dev = 'https://icem-dev-fix.jiekecloud.cn'
headers = {'content-type': "application/json;charset=UTF-8",
				'Authorization': "Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1aWQiOjEsInBzIjoiJUU4JUI2JTg1JUU3JUJBJUE3JUU3JUFFJUExJUU3JTkwJTg2JUU1JTkxJTk4IiwiZXhwIjoxNTYwMzA4ODEzLCJzaWQiOjEwMDAsImNyIjoxNTU5NzA0MDEzNjk5fQ.QCfAZ0Kq5yjDtQ5CXSGlF7dh5VvEw0jMAT6H8KseRcAtREI_BdDycdLzc8amz4lT64t6NxIZQYXeHKtK0r_vDQ"}

#公共POST请求方法
# def api_method(path, data):
# 	response = requests.post(url=path, data=json.dumps(data), headers=headers)
# 	print (response.text)


#SMS一期数据库参数
DBHOST = u'10.10.10.44'
DBUSERNAME = u'root'
DBUSERPASSWD = u'jieke123'
DBNAME = u'geek_icem_resource'
DBNAME_SYSTEM = u'geek_icem_system'
DBPORT = 3306




#Foxmail邮箱参数
foxmail_info = {
	"from_addr": "renming@missfresh.cn",
	"to_addr": "renming@missfresh.cn",
	"password": "KVoKY5C7ggWufsco",
	"subject": "SMS项目接口自动化执行报告"
}


#QQ邮箱参数
# from_addr = u'980808536@qq.com'
# to_addr = u'375631939@qq.com'
# password = u'nohsvznifllybjgd'
# subject = u'SMS项目接口自动化执行报告'


#原料
material = u'1000094'