from commen import method   # 导入公共方法
from test_data import test_data
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)

url = test_data.data["url"]
username = test_data.data.get("username")
password = test_data.data.get("password")
key = test_data.data.get("key")

num = method.sear_func(driver,url,username,password,key)
if key in num:
    print("搜索用例通过的！")
else:
    print("搜索失败！")
