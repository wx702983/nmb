from selenium import webdriver #从selenium这个工具导入webdriver库
import time


#打开浏览器函数
def open_func(driver,url):
    driver.get(url)
    driver.maximize_window() #浏览器最大化

#登录函数
def login_func(driver,username,password):
    driver.find_element_by_id("username").send_keys(username)#输入用户名
    driver.find_element_by_id("password").send_keys(password)#输入密码
    driver.find_element_by_id("btnSubmit").click()#点击登录按钮


#搜索函数

def sear_func(driver,url,username,password,key):
    open_func(driver, url)
    login_func(driver, username, password)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    time.sleep(2)
    id_li = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id") #找到元素、获取id
    id_frame = id_li + "-frame"  # 得到iframe的id
    driver.switch_to.frame(id_frame)   # 通过iframe的id进行切换
    #对页面进行操作、找到搜索输入框
    driver.find_element_by_id("searchNumber").send_keys(key)
    driver.find_element_by_id("searchBtn").click()
    time.sleep(2)
    # 获得单据编码的号码
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return num