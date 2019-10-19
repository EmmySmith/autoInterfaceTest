#coding=utf-8

import time
import os
import sys,importlib
importlib.reload(sys)
# sys.setdefaultencoding('utf8')
import unittest
from HTMLTestRunner import HTMLTestRunner     #引入HTMLTestRunner模板
from sendEmail.sendEmail_new import SendMail
from common.replaceFile import *
from common.getReportResult import *
from common.clearCoupon import *


project = sys.argv[1]
env = sys.argv[2]

def testRun(project,env):
    #根据接收到的env参数来替换相应的环境配置和数据库配置
    replace(env)
    # sys.path.append('./test_interface')
    if project == "ALL":
        # 指定当前文件夹下的Interface目录
        test_dir = "./test_interface/"
    else:
        #指定当前文件夹下的Interface目录
        test_dir = "./test_interface/" + project + "/"
    file = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')  # 匹配结尾为test的py文件
    now = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))  # 取当前时间
    public_path = os.path.dirname(os.path.abspath(sys.argv[0])) # 获取当前运行的.py文件所在的绝对路径
    filename = public_path + "/Report/" +  now + "-" + project+ "-" + env + "-report.html"   #保存的报告路径和名称
    reportName = now + "-" + project+ "-" + env + "-report.html"
    fp = open(filename, 'wb')
    # print("fp is :",fp)
    runner = HTMLTestRunner(stream=fp,
                            title="ICEM系统接口自动化测试报告",
                            description="详细描述如下：\
                                        <<------详细执行结果无法查看,请下载附件用谷歌浏览器访问!------>>"
                            )

    runner.run(file)
    fp.close()
    # path = "./Report/" + reportName
    print(reportName)
    SendMail().send()
    time.sleep(3)
    is_result_pass(reportName,env)
    clear_Coupon()

testRun(project,env)