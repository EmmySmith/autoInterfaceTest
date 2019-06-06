#coding=utf-8
import requests
import json

host = 'https://icem-qa-fix.jiekecloud.cn'


# host_dev = 'https://icem-dev-fix.jiekecloud.cn'
headers = {'content-type': "application/json;charset=UTF-8",
				'Authorization': "Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1aWQiOjEsInBzIjoiJUU4JUI2JTg1JUU3JUJBJUE3JUU3JUFFJUExJUU3JTkwJTg2JUU1JTkxJTk4IiwiZXhwIjoxNTYwMzA4ODEzLCJzaWQiOjEwMDAsImNyIjoxNTU5NzA0MDEzNjk5fQ.QCfAZ0Kq5yjDtQ5CXSGlF7dh5VvEw0jMAT6H8KseRcAtREI_BdDycdLzc8amz4lT64t6NxIZQYXeHKtK0r_vDQ"}

DBHOST = u'10.10.10.44'
DBUSERNAME = u'root'
DBUSERPASSWD = u'jieke123'
DBNAME = u'geek_icem_resource'
DBNAME_SYSTEM = u'geek_icem_system'
DBPORT = 3306




