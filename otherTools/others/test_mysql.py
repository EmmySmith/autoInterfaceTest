# # coding:utf-8
from mysqlHandle.common_mysql import *


sql = "SELECT province from t_province limit 1;"
dbname = "geek_dmp_api"
value = DB_ICEM_proc(dbname).get_vslues(sql)

print(value.decode('utf-8'))
