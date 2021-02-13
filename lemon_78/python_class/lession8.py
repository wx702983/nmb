


"""

UI自动化基础


在已有的框架下实现自动化脚本
完整的自动化框架：
1、基础代码
2、测试数据
3、报告、日志


自动化类型：
接口自动化---接口最多、稳定、性价比高===回归测试
UI自动化---不稳定、维护成本高===冒烟测试
APP自动化（小程序H5）

UI自动化：
人-----浏览器
代码-----翻译(中间件)-----浏览器：驱动可以把代码的指令翻译给浏览器、浏览器可以做相应的操作
浏览器驱动：
chromdriver(71版本稳定)
geckodriver
ieserverdriver
谷歌驱动：http://npm.taobao.org/mirrors/chromedriver/
火狐：https://github.com/mozilla/geckodriver/releases
IE：http://selenium-release.storage.googleapis.com/index.html
Edge：https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
safari：https://developer.apple.com/safari/download/
注意：选择与浏览器对应版本的驱动、否则不兼容
步骤：
1、下载好驱动、解压后得到.exe文件
2、放到Python安装目录下即可


selenium工具包：UI自动化工具、包括三个部分---第三方库---Python、Java
ide:录制脚本工具---少、不好用
webdriver:库---提供了对网页操作的方法、提供各种语言、---Python、Java
grid:分布式---同时对多个浏览器执行并发操作

1、selenium安装
2、驱动下载---Python对应安装目录
3、导入selenium webdriver


通讯原理：
1、chromedriver启动服务，IP+端口 监听
2、webdrier webdriver 跟 chromedriver建立连接，发送的http请求
3、chromedriver 收到指令之后，驱动浏览器执行指令
4、chromedriver 要结果返回给 webdriver
后续指令重复步骤

Python-UI自动化第二节课：Python的元素定位

"""







import time
from selenium import webdriver #从selenium这个工具导入webdriver库
driver = webdriver.Chrome() #初始化一个浏览器---会话session
driver.get("https://www.baidu.com")#打开浏览器对应网址
driver.maximize_window() #浏览器最大化
#返回上一个页面、前进、刷新
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh
time.sleep(2)

# 关闭浏览器
#close():关闭窗口、不会退出浏览器
#quit():退出当前会话、关闭浏览器、清除缓存