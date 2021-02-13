

"""

Python-UI自动化第二节课：Python的元素定位


web页面的基本组成：html+css+js(JavaScript)
html:定义页面呈现的内容---标签语言---<>值</>
css:控制页面如何呈现---布局设置、字体颜色、字体大小
js:可以让页面在不同情形做不同的事


页面元素定位：能唯一标识这个元素的内容
元素定位八大方法：
id、name、xpath---常用
css、class、tag、link、partial_link



通过id name 可以找到这个元素、大部分元素没有这两个属性  xpath
找到元素后的操作：
点击：click
输入内容：send_keys
获取文本：text
获取属性：attribute---id属性



xpath元素定位
1、绝对路径/相对路径
标签名+属性
//标签名[@属性名=属性值]
//input[@id="username"]
绝对路径---复制xpath---/html/body/div/div/div[1]/a/b---从根开始一级一级往下继承---页面变化、不好用、少

相对路径---//b---//input[@id="username"]



2、层级定位
//标签名[@属性名=属性值]//标签名[@属性名=属性值]
//div[@class="login-logo"]//b

3、文本属性定位
//b[text()="柠檬ERP"]---值不变、唯一标识

4、包含属性值
//标签名[contains(@属性名/text(),属性值)]
//input[contains(@class,"username")]
//span[contains(text(),"零售出库")]

5、轴定位
//input[@id='rememberUserCode']/following-sibling::ins").click()


Python三大等待:打开新页面---click操作之后---页面刷新时间--等待
1、强制等待---sleep()：设置等待时长没有到期就算元素出现了、也还要等待---速度慢
2、智能制等待：
隐形等待---默认等待时间、只要元素出现了直接继续执行---一个会话只执行一次---有些地方不生效+强制等待
显示等待---复杂

"""














from selenium import webdriver #从selenium这个工具导入webdriver库
import time

driver = webdriver.Chrome() #初始化一个浏览器---会话session
driver.implicitly_wait(10)   # 隐性等待
driver.maximize_window() #浏览器最大化
driver.get("http://erp.lemfix.com")
page_title = driver.title #获取页面标题
if page_title == "柠檬ERP":
    print("这个页面的标题：{}".format(page_title))
else:
    print("这个用例不通过")
























driver.find_element_by_id("username").send_keys("test123")#输入用户名
driver.find_element_by_id("password").send_keys("123456")#输入密码
driver.find_element_by_id("btnSubmit").click()#点击登录按钮
# driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
time.sleep(2)
# 确认登录用户名
page_name = driver.find_element_by_xpath("//p").text   # 获取这个元素的文本内容
if page_name == "测试用户":
    print("这个登录用户是：{}".format(page_name))
else:
    print("这个用例不通过！")

driver.find_element_by_xpath("//span[text()='零售出库']").click()

time.sleep(2)

# id是变化的、不能直接用
# driver.switch_to.frame("tabpanel-a2f50eac53-frame")

id_li = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id") #找到元素、获取id
id_frame = id_li + "-frame"  # 得到iframe的id

driver.switch_to.frame(id_frame)   # 通过iframe的id进行切换

#对页面进行操作、找到搜索输入框
driver.find_element_by_id("searchNumber").send_keys("712")
driver.find_element_by_id("searchBtn")

# 获得单据编码的号码
num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
if "841" in num:
    print("搜索用例通过的！")
else:
    print("搜索失败！")








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
    driver.find_element_by_id("searchBtn")
    time.sleep(2)
    # 获得单据编码的号码
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return num


data = {"url":"http://erp.lemfix.com",
        "username":"test123",
        "password":"123456",
        "key":"841"
        }

"""Python-UI自动化第三节课：Python的iframe切换

HTML里面嵌套了HTML---子页面---直接定位元素不会成功、先切换页面
1、frame名字---唯一标识---id、name
2、元素定位识别---次
3、下标

"""