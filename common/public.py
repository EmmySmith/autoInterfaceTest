#coding=utf-8
import requests
import json
from common.login import login



host = 'https://icem-qa-fix.jiekecloud.cn'
userName = "lqx:admin_lqx"
password = "0192023a7bbd73250516f069df18b500"
# host_dev = 'https://icem-dev-fix.jiekecloud.cn'
headers = {'content-type': "application/json;charset=UTF-8",
				'Authorization': login(host,userName,password)}

headers_fileUpload = {'content-type': "multipart/form-data; boundary=----WebKitFormBoundaryzzZ5MqJKTjSzisxe",
				'Authorization': login(host,userName,password)}

DBHOST = u'10.10.10.44'
DBUSERNAME = u'root'
DBUSERPASSWD = u'jieke123'
DBPORT = 3306
# DBNAME = u'geek_icem_resource'
# DBNAME = u'geek_icem_system'
# DBNAME = u'geek_icem_sms'
# DBNAME = u'geek_icem_log'
# DBNAME = u'geek_icem_crowd'
# DBNAME = u'geek_icem_component'
# DBNAME = u'geek_icem_activity'









