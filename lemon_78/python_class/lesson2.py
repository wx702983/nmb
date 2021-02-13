"""

字符串操作：
1、取值
每个元素都有位置--索引--从0开始
取最后一个元素：-1===负数的取法
2、取多个值
切片===指定[索引头：索引尾：步长]
取头不取尾、索引头默认值从0开始、索引尾默认值最后、步长默认值1
3、获取长度：len()---计算变量的长度、并返回这个数字
4、常用方法

str1 = "hello lemonban"
print(str1[4])
print(str1[-1])
print(str1[0:4:1])
print(str1[::])
print(str1[0:len(str1):1])

print(str1.index(y)) #获取某个元素的索引、没有找到元素会报错--代码会停止运行
print(str1.find(y)) #没有找到元素不会报错、返回-1---代码不会停止运行
print(str1.count("l")) #统计个数
print(str1.replace('lemonban','Python')) #元素替换

Python常见运算符
算术运算符：+-*/%
1、两个数字相加===数学、字符串的拼接
2、两个数字相减===数学、不支持字符串操作
3、两个数字相乘===数学、字符串与数字相乘
4、两个数字相除===数学、结果是float
num = 100
print(10+20)
print("tricy" + "lemon")
print(str(num) +"lemon")
数据类型的强制转换:str() int() float()

input()--获取从控制台输入的内容---输入的任何内容都是字符串

num1 = int(input("请输入一个数字："))
print(type(num1))
print(num1+1)

print(20-10)

print(2*3)
print("I love you" * 3000)

print(10/2)

赋值运算符：= += -=

a = 10
a += 5    # a = a + 5
a -= 10  # a = a - 10

比较运算符：== > < >= <= !=   运算结果是布尔型

print(4 >= 6)
print("登录成功" == "登录成功")



逻辑运算符： or与   and或   not非  运算结果是布尔型

print(not 5 < 9)

成员运算符: in not in   运算结果是布尔型

str2 = "hello Python"
print("P" in str2)












"""