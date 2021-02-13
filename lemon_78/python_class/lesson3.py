'''


Python经典数据类型：列表、元组、字典、集合
Python的控制流：if判断 for循环


列表：list[]
1、列表可以存放任意数据类型、包括列表、元素和元素之间用英文逗号隔开
2、列表统计元素个数：len()
3、取值：每个元素都有自己的位置---索引、从0开始---取多个值、切片
4、列表元素可以被改变：增加、删除、修改
5、列表嵌套取值---list[4][2]
6、列表元素可以重复 重复次数---count()

#增加
list1 = [20,3.14,True,"Freestyle",[1,2,4,5]] #定义一个列表
print(list1)
print(list1[3])
print(list1[4][2])
list1.append("等") #追加元素到末尾--P1
print(list1)
list1.insert(3,"露露") #指定位置添加元素--p1
print(list1)
list1.extend(["地球","柠檬"]) #合并、可以同时添加多个元素
print(list1)

list1.extend(["柠檬","柠檬"])
print(list1.count("柠檬")) #统计个数

#删除
list1.pop(5) #默认删除最后一个、可以指定元素索引删除
print(list1)
list1.remove(20) #指定元素本身删除
print(list1)
list1.clear() #清除、清空列表
print(list1)




元组：tuple()
1、元组可以存放任意数据类型、元素和元素之间用英文逗号隔开
2、元组统计元素个数：len()
3、取值：每个元素都有自己的位置---索引、从0开始---取多个值、切片
4、元组元素不可以被改变
5、元组元素可以重复 重复次数---count()
6、想要改变元组的元素---列表list()---元组tuple()

tuple1 = (20,3.14,True,"Freestyle") #定义一个元组
print(tuple1)

list2 = list(tuple1)
print(list2)
list2[0] = "简单"
print(list2)
print(tuple(list2))


字典：dict{}
1、元素是键值对的格式---key : value---一个键值对是一个元素、多个元素之间用英文逗号隔开
2、字典一般使用场景：描述一个物件的属性===人的属性：名字、性别、年龄
3、取值：通过key取value值
注意：字典3.6版本之前没有顺序，没有索引



dict1 = {"name":"fafa","gender":"male","age":"18"}
print(dict1["age"])
print(dict1.get("age"))
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(len(dict1))
# 增加/修改---一个键值对
dict1["hobby"]="女"
print(dict1)
dict1["gender"]="female"
print(dict1)





#删除---指定key删除
dict1.pop("hobby")
print(dict1)


集合: set{}
1、集合元素不重复===使用场景是给列表去重
2、无序的

list1 = [11,22,33,22,22,22]
print(list1)
set1 = set(list1)
print(set1)
list1 = list(set1)
print(list1)







控制流:if判断  for循环
if判断语法
if 条件:             ===判断这个条件成立的时候、进入下面的执行语句===分支==冒号、四个空格的缩进
    子代码(执行语句)
elif 条件:           ===判断这个条件成立的时候、进入下面的执行语句===分支
    子代码(执行语句)
elif 条件:           ===注意：elif可以没有、可以有多个
    子代码(执行语句)
    ...


    ...
else:               ===没有条件的
    子代码(执行语句)


money = int(input("请输入你的余额："))

if money >= 200:
    print ("做生意!")
elif money >= 100:
    print ("买房!")
elif money >= 50:
    print ("买车!")
elif money >= 20:
    print ("买点零食，吃吃")
else:
    print ("打工人好好工作，学习!")




for循环:重复执行某一块代码
1、使用场景:用来遍历某些数据对象的元素的---字符串，列表，元组，字典
2、缩进里面是for循环的循环体
循环次数由谁决定的---元素的个数
如何控制循环---if判断、break、continue

for循环结合使用的内置函数:range(start,stop,step)---生成一个整数序列
start:由谁开始生成、默认0开始
stop：到谁结束、不能省略
step：步长、默认值1


for i in range(0,11,2):
    print(i)

'''
list1 = [20,3.14,True,"Freestyle",[1,2,4,5]] #定义一个列表
for data in list1:
    # print(data)
    if data == "Freestyle" :
        break  #中断---跳出整个循环
        # continue 继续---跳出本次循环
    print(data)




