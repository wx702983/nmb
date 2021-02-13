
'''
Python的requests接口请求


第三方库的安装
pip安装
requests模块安装：pip install requests
切换源：pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple/ --user
加长超时时间：pip --default-timeout 100 install requests

修改pip源可以加快下载安装速度
pip默认使用pypi数据源、因为在国外网速受限、可以修改为国内镜像源、速度快很多
1、在系统用户目录下、新建pip文件夹---C:\User\Administrator\pip
2、再新增pip.ini文件、复制以下内容：
[global]
index-url=http://pypi.tuna.tsinghua.deu.cn/simple
[install]
trusted-host=http://pypi.tuna.tsinghua.edu.cn
3、此时pip源已修改永久生效、再执行pip命令就不会报错


Pycharm安装
File==》Settings==》Project==》Project Interpreter==》点击+搜索对应的库名字==》安装install package


接口测试：
第三方库：别人写好封装的、拿来直接用---request---Python里实现接口测试
requests方法的参数传入、除了url、其他都必须用字典格式传入
1、安装
2、导入--import
pprint---格式美化
登录返回结果
{'code': 0,
 'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved',
 'data': {'id': 10195843,
          'leave_amount': 19300.0,
          'mobile_phone': '15815541706',
          'reg_name': 'mengmeng',
          'reg_time': '2021-01-15 21:09:22.0',
          'token_info': {'expires_in': '2021-01-23 22:22:55',
                         'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjEwMTk1ODQzLCJleHAiOjE2MTE0MTE3NzV9.uHd3WXbnkuO2SSzdIDxayFy_YLF13Lcsjkj0c_zYj8OIWQjb-Wx6ZRxwqgN-aGEudsGlet9WnzpuADLk6CtITA',
                         'token_type': 'Bearer'},
          'type': 1},
 'msg': 'OK'}



# 注册接口
import requests

url_api_reg = "http://8.129.91.152:8766/futureloan/member/register"
data_api_reg = {
    "mobile_phone": "15549083142",
    "pwd": "12345678",
    "type": "1",
    "reg_name": "mengmeng"
}

head_reg = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
response = requests.post(url=url_api_reg, json=data_api_reg, headers=head_reg)
print(response.json())

# 登录接口

import pprint

url_api_log = "http://8.129.91.152:8766/futureloan/member/login"
data_api_log = {
    "mobile_phone": "15815541706",
    "pwd": "12345678",
}
head_log = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
response = requests.post(url=url_api_log, json=data_api_log, headers=head_log)
pprint.pprint(response.json())
res = response.json()

登录返回结果
{'code': 0,
 'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved',
 'data': {'id': 10195843,
          'leave_amount': 19300.0,
          'mobile_phone': '15815541706',
          'reg_name': 'mengmeng',
          'reg_time': '2021-01-15 21:09:22.0',
          'token_info': {'expires_in': '2021-01-23 22:22:55',
                         'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjEwMTk1ODQzLCJleHAiOjE2MTE0MTE3NzV9.uHd3WXbnkuO2SSzdIDxayFy_YLF13Lcsjkj0c_zYj8OIWQjb-Wx6ZRxwqgN-aGEudsGlet9WnzpuADLk6CtITA',
                         'token_type': 'Bearer'},
          'type': 1},
 'msg': 'OK'}

# 充值接口
# 字典取值--接口关联
# jsonpath--安装第三方库、导入---结果放列表里



member_id = res["data"]["id"]      #取id
token = res["data"]["token_info"]["token"]  #取token

import jsonpath

member_id = jsonpath.jsonpath(res, "$..id")[0]  # 取id
token = jsonpath.jsonpath(res, "$..token")[0]  # 取token

print(member_id)
print(token)
url_api_rec = "http://8.129.91.152:8766/futureloan/member/recharge"
data_api_rec = {
    "member_id": member_id,
    "amount": 6300,
}
head_rec = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json",
            "Authorization": "Bearer " + " " + token}
response = requests.post(url=url_api_rec, json=data_api_rec, headers=head_rec)
pprint.pprint(response.json())










访问百度请求---拓展
1、乱码--手动、指定解解码
2、不是正确的页面--爬虫--反爬机制--检测到你的请求不是浏览器发送过来的、不会正确响应
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400
https://www.baidu.com/s?wd=柠檬班
'''


import requests
url = "https://www.baidu.com/"
params = {"wd": "柠檬班"}
head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400"}
response = requests.get(url=url,headers=head,params=params)

print(response.text) #自动解码页面--乱码--优先
print(response.content.decode("utf-8"))#手动指定解码方式














































