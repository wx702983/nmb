'''




Python内置函数及函数

函数：一段代码重复使用、将代码进行封装---调用这个函数
作用：提高代码复用率
格式：
注意：函数名命名规则遵循标识符规则、
     函数定义完后没有被调用不会被执行、
     写函数名调用函数、
     函数里可能变化的内容不建议写成参数


def 函数名():
    函数体(函数实现具体功能的代码)
    返回值
返回值：函数如果有数据给调用函数的人使用、把这个数据设置成函数返回值
1、返回值一定在最后、返回值后面的代码不会被执行---标志函数结束
2、返回值可以没有---None

def good_job():  #定义函数
    salary = 8000
    bonus = 2000
    subsidy = 500
    sum1 = salary + bonus + subsidy
    print(sum1)
good_job()    #调用函数




def good_job(salary,bonus,subsidy):  #定义函数、定义参数---形参
    sum1 = salary + bonus + subsidy
    print("工资总和是：{}".format(sum1))
good_job(8000,2000,500)    #调用函数、传参---实参



定义参数的类型：
1、必备参数：定义了就必须传入的参数、不传少传都会报错
2、默认参数：如果有些参数有大概率情况---值===默认值---可以不传
3、不定长的参数：不确定是否有、也不确定有多少的这种参数---
    *args：等前面必备参数和默认参数都接受完了之后、剩下的参数都会被这个不定长参数接受、并且以元组类型保存
    **kwargs:等前面必备参数和默认参数都接受完了之后、剩下的参数都会被这个不定长参数接受、并且以字典类型保存

参数传入方式：
1、位置传参方式：位置的顺序性---传错了位置、参数错了---简单、容易出错
2、关键字传参：指定参数名进行传参---精确点、不容易出错
3、混合传参：位置传参必须放在关键字传参前面

'''


def good_job(salary,bonus,subsidy=500,*args,**kwargs):  #定义函数、定义参数---形参
    print("参数salary：{}".format(salary))
    print("参数bonus：{}".format(bonus))
    print("参数subsidy：{}".format(subsidy))
    print("参数args：{}".format(args))
    sum1 = salary + bonus + subsidy
    for num in args:
        sum1 += num
    for i in kwargs:
        sum1 += kwargs[i]
    print("工资总和是：{}".format(sum1))
    return sum1 #定义函数返回值
good_job(8000,2000,800,200,500,600)    #调用函数、*args不定长传参---实参

good_job(8000,bonus=2000,subsidy=800)    #调用函数、关键字传参---实参

good_job(8000,2000,800,111,222,333,aa=200,bb=500,cc=600)    #调用函数、混合**kwargs传参---实参


result = good_job(8000,2000,800,111,222,333,aa=200,bb=500,cc=600)    #调用函数、混合**kwargs传参---实参
#函数定义返回值后、用变量接受函数调用---函数返回值
print(result)

if result >= 10000:
    print("我不是打工人")
else:
    print("我是打工人")




'''
断点调试：方便理解执行过程、寻找问题、调试问题
1、开始调试的这行---断点
2、debug
3、点击单行执行---一步一步执行

'''
'''
内置函数:
print()
input()
type()
isinstance()
len()
数据类型：str()，int()，float()，bool()，list()，tuple()，dict()，set()
字符串的内置函数：format，index，replace，find，count
列表内置函数：append，insert，pop，remove，extend，count
字典内置函数：pop，update，get
range{}:











'''







