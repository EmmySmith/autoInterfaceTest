# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 14:26
# @Author  : renming
# @File    : clearCoupon.py
#!/usr/bin/python
# coding=utf-8

from mysqlHandle.common_mysql import *

def clear_Coupon():
    try:
        for i in range(5):
            dbname = "geek_icem_resource"
            sql_select = '''SELECT id FROM t_coupon WHERE coupon_name LIKE '自动化%' ORDER BY id DESC LIMIT 1;'''
            conponId = DB_ICEM_proc(dbname).get_vslues(sql_select)
            sql_delete = '''DELETE FROM t_coupon WHERE id = %s'''%conponId
            DB_ICEM_proc(dbname).delete_data(sql_delete)
    except IndexError as e:
        print("geek_icem_resource数据库对应优惠券表无数据，无需删除！")

# clear_Coupon()