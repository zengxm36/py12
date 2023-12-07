#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#列表 list

classmates = ['Michael', 'Bob', 'Tracy']
classmates

len(classmates)

#python索引默认从0开始捏
classmates[0]
classmates[1]
classmates[2]
classmates[3]

#最后一个索引
classmates[-1]

#list是一个可变的有序表，所以，可以往list中追加元素到末尾
#class好像不能用来做变量名？似乎会报错qwq...
classmates.append("adam")
classmates

classc = ["1","2","3"]
classc.append("2")
classc

#list可以把元素插入到指定位置（没有删掉原来的元素，只是把后面的都往后移）
classmates.insert(1,'happy')
classmates

#删除list末尾的元素或指定位置的元素
classmates.pop()
classmates.pop(0)

#直接通过赋值可以替换list中的元素
classmates[0] = 'happy_good'

#list里面可以有不同的数据类型
L = ["apple", 1 , True]
len(L)

#list里面可以有另外一个list
p = ['Jason','jesus']
Mix_list = ['apple', 'happy', ['Jason','jesus']]
Mix_list1 = ['apple', 'happy', p]
len(Mix_list)
Mix_list[2]
len(Mix_list[2])

Mix_list[2][1]

#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，不能往后面添加，不能中途插入或替代
classmates_tuple = ('Michael', 'Bob', 'Tracy')

t = (1,2)
t = ()

#如果要定义一个只有一个元素的tuple，要记得加括号，因为tuple的括号默认被识别为数学运算的小括号
t= (1,)
t
#tuble里面可以套一个list
t = ('a', 'b', ['A', 'B'])
t[2]
t[2][0]

#tuble定义了之后也是可以变的，不一定是完全不可变的，例如

t[2][0] = 'X'
t

#因此，tuble的“不变”指的是tuble每个元素的指向永远不变，指向一个list就不能指向其他对象，但是被指向的这个list本身就是可变的


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])