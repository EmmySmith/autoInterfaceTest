# # coding=utf-8
#
# from common.operate_Excel import *
# from common.api_test_pubilc import testApi
# import unittest
# # import requests
# import json
#
#
# class SMSInterface(unittest.TestCase):
#
#     def test_allApi_test(self):
#         '''物流产研部SMS微仓管理系统接口。'''
#         for sheetNumber in range(3):
#             print("\n")
#             print(u'开始执行Sheet{}的测试用例：'.format(sheetNumber+1))
#             # print(sheetNumber)
#             # excel = readExcel(r'../testCases/case_test.xlsx')
#             excel = readExcel(r'D:\automation_testcase\case_test.xlsx',sheetNumber)
#             # counts = excel.getSheet()
#             # print("counts is:",counts)
#             name = excel.getName()
#             data = excel.getData()
#             url = excel.getUrl()
#             method = excel.getMethod()
#             # uid = excel.getUid()
#             code = excel.getCode()
#             row = excel.getRows()
#             for i in range(0, row-1):
#                 try:
#                     api = testApi(method[i], url[i], data[i]).testApi()
#                     apicode = api.json()['code']
#                     apitext = api.text
#                     if apicode == code[i]:
#                         print("\n")
#                         # print(u'{}、{}:测试成功-*-Pass-*-。"\n"返回数据为:{}'.format(i + 1, name[i],apitext))
#                         print(u'{}、{}:测试成功-*-Pass-*-。\n '.format(i + 1, name[i]))
#                     else:
#                         print("\n")
#                         print(u'{}、{}:测试失败-*-Fail-*-。\n返回数据为:{}'.format(i + 1, name[i],apitext))
#                 except Exception as e:
#                     print("执行失败！")
#
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)