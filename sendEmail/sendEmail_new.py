# coding:utf-8

import os, sys
import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# reportPath = os.path.join(os.getcwd(), 'report')  # 测试报告的路径
#
# print("打印路径：")
#
# print(reportPath)

now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))  # 取当前时间
public_path = os.path.dirname(os.path.abspath(sys.argv[0]))  # 获取当前运行的.py文件所在的绝对路径
reportPath = public_path + "/Report/"  # 保存的报告路径和名称

# reportPath = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),'report')

class SendMail(object):
    def __init__(self, recver=None):
        """接收邮件的人：list or tuple"""
        if recver is None:
            self.sendTo = ['jieke@jiekecloud.com']  # 收件人这个参数，可以是list，或者tulp，以便发送给多人
        else:
            self.sendTo = recver

    def get_report(self):  # 该函数的作用是为了在测试报告的路径下找到最新的测试报告
        dirs = os.listdir(reportPath)
        dirs.sort()
        newreportname = dirs[-1]
        # print('The new report name: {0}'.format(newreportname))
        return newreportname  # 返回的是测试报告的名字

    def take_messages(self):  # 该函数的目的是为了 准备发送邮件的的消息内容
        newreport = self.get_report()
        self.msg = MIMEMultipart()
        self.msg['Subject'] = 'ICEM系统接口自动化测试报告'  # 邮件的标题
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        with open(os.path.join(reportPath, newreport), 'rb') as f:
            mailbody = f.read()  # 读取测试报告的内容
        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')  # 将测试报告的内容放在 邮件的正文当中
        self.msg.attach(html)  # 将html附加在msg里

        # html附件    下面是将测试报告放在附件中发送
        att1 = MIMEText(mailbody, 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="ICEM_interface_report.html"'  # 这里的filename可以任意写，写什么名字，附件的名字就是什么
        self.msg.attach(att1)

    def send(self):
        self.take_messages()
        self.msg['from'] = 'report@jiekecloud.com'  # 发送邮件的人
        self.toadder = 'wangsijia@jiekecloud.com,renming@jiekecloud.com,hongxiangqian@jiekecloud.com,zhangmin@jiekecloud.com,fengxiaoli@jiekecloud.com'  # 多个收件人
        # self.toadder = 'renming@jiekecloud.com'  # 单个收件人
        self.toadders = self.toadder.split(',')
        # self.msg['to'] = self.toadder.split(',')     # 收件人和发送人必须这里定义一下，执行才不会报错。
        smtp = smtplib.SMTP_SSL('smtp.jiekecloud.com', 465)  # 连接服务器
        # smtp = smtplib.SMTP()
        # smtp = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
        # smtp.connect('smtp.exmail.qq.com')
        smtp.login('report@jiekecloud.com', 'Jieke1234')  # 登录的用户名和密码（注意密码是设置客户端授权码，因为使用用户密码不稳听，有时无法认证成功，导致登录不上，故无法发送邮件。）
        smtp.sendmail(self.msg['from'], self.toadders, self.msg.as_string())  # 发送邮件
        smtp.close()
        print('sendmail success')


if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()