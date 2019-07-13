# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 19:54
# @Author  : renming
# @File    : getReportResult.py
#!/usr/bin/python
# coding=utf-8

from bs4 import BeautifulSoup
from common.sendDingDingMessage import *
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

def is_result_pass(reportName,env):
    reportPath = "./Report/" + reportName
    try:
        with open(reportPath, "r",encoding='UTF-8') as fp:
            f = fp.read()  # 读报告
        soup = BeautifulSoup(f, "html.parser")
        status = soup.find_all(class_="attribute")
        result = status[2].contents[-1] # 获取报告结果
        reportPath = "http://10.10.10.40/download/autotest/Report/"
        if "错误" in result or "失败" in result:
            message = "各位观众：\n【测试组】接口自动化测试结果：" + result + "\n" + "被测环境：" + env + "\n" + "报告名称：" + reportName + "\n" + "报告地址：" + reportPath + reportName + "\n"
            ddRobot(message)
        else:
            # message = "各位观众：\n【测试组】接口自动化测试所有接口全部通过：" + result + "\n" + "被测环境：" + env + "\n" + "报告名称：" + reportName + "\n" + "报告地址：" + reportPath + reportName + "\n"
            # ddRobot(message)
            return "全部通过"

    except Exception as msg:
        return "尴尬：\n【测试组】接口测试执行完成，钉钉消息通知异常：" + str(msg) + "\n"

# if __name__ == "__main__":
#     res = is_result_pass("201907081625-ALL-qa-report.html")
#     print(res)