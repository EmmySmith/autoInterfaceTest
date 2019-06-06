#coding=utf-8
def replace(env):
    if env == "qa":
        data = ''
        with open('./common/public.py', 'r+',encoding='UTF-8') as f:
          for line in f.readlines():
            if(line.find('host') == 0):
              # line = 'host_test=%s' % ('https://icem-qa-fix.jiekecloud.cn',) + '\n'
              line = "host = 'https://icem-qa-fix.jiekecloud.cn'" + '\n'
            data += line
        with open('./common/public.py', 'r+') as f:
          f.writelines(data)
    else:
        data = ''
        with open('./common/public.py', 'r+',encoding='UTF-8') as f:
          for line in f.readlines():
            if(line.find('host') == 0):
              # line = 'host_test="%s"' % ('https://icem-dev-fix.jiekecloud.cn',) + '\n'
              line ="host = 'https://icem-dev-fix.jiekecloud.cn'" + '\n'
            data += line
        with open('./common/public.py', 'r+') as f:
          f.writelines(data)

