                                        **~~解客科技ICEM系统接口自动化框架~~**


一：基于Python + unittest + requests 接口自动化框架

    python版本python3.7.3
    
二：代码结构

    common文件夹下存放一些公共的方法和一些固定的参数
    mysqlHandle文件夹下存放操作数据库相关的代码
    Report文件夹用于存放测试报告
    sendEmail文件夹存放发送邮件及报告附件的方法
    test_interface文件夹下存放业务接口，接口自动化框架代码存放处
    testData用于存放测试数据，测试用例
    HTMLTestRunner为html格式的报告模板
    run_test.py文件为自动化的入口文件
    
三：run_test.py参数介绍
    
    项目参数：根据需要可筛选不同的业务模块测试用例来执行，目前支持"CPD"，"MA","SETUP"
    环境参数：开发人员可选择开发环境来执行接口自动化，测试人员可以选择测试环境来执行，目前支持"dev","qa"
    
四：执行run_test.py

    执行python run_test.py "项目参数" "环境参数"  就可执行自动化程序
    例如：python run_test.py MA qa
    例如：python run_test.py CDP qa
    例如：python run_test.py SETUP dev
    
五：设置收件人邮箱接收测试报告邮件

     def send(self):
        self.take_messages()
        self.msg['from'] = 'renming@jiekecloud.com'  # 发送邮件的人
        _# self.toadder = 'wangsijia@jiekecloud.com,renming@jiekecloud.com'  # 多个收件人
        self.toadder = 'renming@jiekecloud.com'  # 单个收件人
        
六：查看报告
    
    在Report文件夹下查看最新生成的报告，格式例如：2019-06-11 11-10-37 report.html
    报告文件为html格式，建议在谷歌浏览器下打开，其它浏览器兼容性可能不好