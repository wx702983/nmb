"""

Python基础语法&Python常用数据类型
1、什么是自动化测试
2、Python的基础语法
3、Python的常用数据类型
4、格式化输出


测试--敏捷开发模型1天2个版本--临近发布--回归测试--1000+用例--繁琐、重复、枯燥===自动化测试--提高测试效率
工具：Jmeter(加密数据--Java--二次开发)、QTP、RF--都是别人开发好的、使用简单
代码：自动化--灵活、满足自己的需求===搭建自动化框架--Python Java JS PHP

1、项目什么阶段做自动化
回归测试（稳定的功能）--覆盖率80%+
冒烟测试（主流程）--覆盖率30%+
2、脚本实现在什么时候完成
项目结束后、新的功能（用例）添加--丰富自动化框架--下一个项目测试
3、自动化测试方向
接口自动化---最多==接口不怎么变化
UI自动化---维护成本高===界面经常变化
APP自动化（小程序H5）

Python的基础语法
什么是Python及其优势
编程语言、简单好入门--高级、高封装
需求：C语言1000行代码、Java语言200行、Python语言10行

环境
Python.exe 2.x/3.x
Pycharm--集成开发环境（IDE）--编辑、调试

Python的基础语法
Pycharm创建项目--创建Python Package--创建Python File
Python文件--Python Package--Python File等标识符命名规则
单行注释、多行注释
Python Package--项目目录--存放代码文件--代码归类
Directory--目录--文件夹、存放图片信息、背景文件

 标识符：Python里凡是自己取的名字--Project--Python Package--Python File--变量、函数
 命名规则：
 1、只能包含字母、数字、下划线
 2、不能以数字开头
 3、不能使用关键字

关键字：
import keyword
print(keyword.kwlist)

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
 'try', 'while', 'with', 'yield']
 
 注意：
 Python区分大小写 True不等于true
 print input 不是关键字
 不同数字与字母之间用下划线隔开--方便阅读
 取名字--见名知义
 
 运行
 1、右键Run
 注释：
 1、单行注释: #
 2、多行注释: """ """  ''' '''
 3、快捷键注释: Ctrl + / ===注释、取消注释
 
 
 print()---Python内置函数---打印内容到控制台
 
 常用数据类型：
 整型int 浮点型float 字符串str 布尔型bool（True=1、False=0）列表 元组 字典 集合
 确认数据类型的内置函数：
 1、type()--直接输出数据的类型--P1
 2、isinstance()--判断数据类型--True、False--P2

print(type(3.14))
print(isinstance(12,bool))
整型int：整数
浮点型：小数
布尔型：True=1、False=0
字符串：成对引号括起来的内容 ''  ""  """ """
1、引号的嵌套使用
2、''' ''' 三引号仅保持格式作用--所见即所得

print('''-----fafa的基本信息-----
    name:fafa
        gender:female
            hobby:柠檬
''')

变量：存储任何数据类型的容器
变量名：遵循标识符命名规则、变量一定要先声明才能使用

name = "fafa"
print('''-----'''+name+'''的基本信息-----
    name:fafa
        gender:female
            hobby:柠檬
''')
 
 需求：要在字符串里面传入变量、不想截断字符串、占位置===格式化输出.format()
占位符：{}---传变量的地方、占位置、几个占位符传几个变量
1、可以为空---按照默认位置顺序传参
2、指定位置传参---{}--索引
不能混用
3、占位符：%s--字符串==万能  %d--整型 %f--小数  P2拓展
传入变量--%()
name = "fafa"
gender = "female"
hobby = "柠檬"
print('''-----{}的基本信息-----
    name:{}
        gender:{}
            hobby:{}
'''.format(name,name,gender,hobby))

name = "fafa"
gender = "female"
hobby = "柠檬"
print('''-----{0}的基本信息-----
    name:{1}
        gender:{2}
            hobby:{3}
'''.format(name,name,gender,hobby))
 
 

"""

