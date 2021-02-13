""""




Python-作业代码








1、在pycharm的控制台里输入以下内容，并且以如下格式输出到控制台
2、现在有字符串：str1 = 'python hello aaa 123123aabb'
1）请取出并打印字符串中的'python'
2）请分别判断 'o a' 'he' 'ab' 是否是该字符串中的成员
3）替换python为“lemon”
4) 找到aaa的起始位置
"""

"""name = input("请输入你的名字：")
age = input("请输入你的年龄：")
gender = input("请输入你的性别：")
print('''********************
    姓名：{}
    年龄：{}
    性别：{}
********************'''.format(name,age,gender))
str1 = 'python hello aaa 123123aabb'
print(str1[0:6:1])
print("o a" in str1)
print("he" in str1)
print(str1.replace("python","lemon"))
print(str1.find("aaa"))
print(str1.index("aaa"))
"""


"""
1：a=[1,2,'6','summer'] 请用成员运算符判断 i是否在这个列表里面 -- if 
2：dict_1={"class_id":45,'num':20} 请判断班级上课人数是否大于5 
注：num表示课堂人数。如果大于5，输出人数。 
3、list1 = ['肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬'] 
列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。并且把字典都存在新的 list中，最后打印最终的列表。
方法1： 手动扩充--字典--存放在列表里面；{} --简单 
方法2： 自动--dict（）--不强制-- for循环 ，list.append() --- 难度
4、for循环遍历其他的数据类型 --字典"""


varlist =['This', 'is', 3, 'demo', '!']
print(varlist[1:4:1])

a = [1,2,'6','summer']
if "i" in a:
    print("i是这个列表的成员！")
else:
    print("i不是列表的成员")


dict_1 = {"class_id":45,'num':20}
num = dict_1.get("num")  #字典的取值
if num > 5:
    print("这个班级的人数是：{}".format(num))
else:
    print("班级人数少于5人")


list1 = ['肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬']
dict1 = {"name":"肥兔","gender":"male","age":18,"city":"深圳"}
dict2 = {"name":"鹿鹿","gender":"male","age":18,"city":"深圳"}
dict3 = {"name":"Freestyle","gender":"male","age":18,"city":"深圳"}
dict4 = {"name":"等","gender":"male","age":18,"city":"深圳"}
dict5 = {"name":"地球","gender":"male","age":18,"city":"深圳"}
dict6 = {"name":"阑珊","gender":"male","age":18,"city":"深圳"}
dict7 = {"name":"柠檬","gender":"male","age":18,"city":"深圳"}
list2 = [dict1,dict2,dict3,dict4,dict5,dict6,dict7]
print(list2)

list1 = ['肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬']
list3 = ['male', 'male', 'male', 'male', 'male', 'female', 'female']
list4 = [18,19,20,21,22,23,24]
list5 = ["北京","深圳","成都","重庆","北京","北京","北京"]
list2 = []
for i in range(len(list1)):
    dict1 = dict(name=list1[i],gender=list3[i],age=list4[i],city=list5[i])
    list2.append(dict1)
print(list2)

for item in list1:
    dict1 = dict(name=item,gender="female",age=18,city="北京")
    list2.append(dict1)
print(list2)


"""
1. 把字符串转成列表 - list() 
2. 完成任意整数序列的相加 - 生成一个整数序列，里面全是数字。求里面所有数字的和 
3. 定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。"""

def object(subject):
    if type(subject) == list or type(subject) == dict or type(subject) == str:
        length = len(subject)
        if length >= 5:
            print("Ture")
        else:
            print("False")
    else:
        print("数据类型不能计算长度！")

object([1,2,3,4])
object(12)



num1 = int(input("please input a num :"))
sum1 = 0
for i in range(num1):
    sum1 += i
print(sum1)


def add_fun(num):
    sum1 = 0
    for i in range(num):
        sum1 += i
    return sum1
result = add_fun(100)
print("这个整数序列相加的和是：{}".format(result))


str1 = "hello python lemon"
list1 = list(str1)
print(list1)


# 扩展：["hello","python","lemon"]  split(str,num): 将一个字符串以一个符号截断,返回列表num截取次数,默认-1---最后
list2 = str1.split(" ",1)
print(list2)



"""
print(sum(range(1,101,1)))

a = int(input("请输入一个数："))

if not a % 2:
    print("{}这个数是偶数".format(a))
else:
    print("{}这个数是奇数".format(a))


  
1. 某比赛需要获取你的个人信息，设计一个程序，运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据存储起来，
2、数据存储完了，然后输出个人介绍，格式如下:  我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
3. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
4, 平台为了保护你的隐私，需要你删除你的联系方式；"""

dict1 = dict(
    name = input("请输入你的名字："),
    age = input("请输入你的年龄："),
    gender = input("请输入你的性别："))
print('''我的名字{}，今年{}岁，性别{}，喜欢敲代码'''.format(dict1.get("name"),dict1.get("age"),dict1.get("gender")))
dict1["身高"]="170"
dict1["联系方式"]="13555667788"
print(dict1)
dict1.pop("联系方式")
print(dict1)

# 设计一个函数，获取一个100以内偶数的纯数字序列，并存到列表里， 然后求这些偶数数字的和。
def data_func(data):
    list1 = []
    for i in range(0,data,2):
        list1.append(i)
        print(list1)
    print(sum(list1))

data_func(100)



varlist = ['This', 'is', 3, 'demo', '!']
print(varlist[1:4:1])

