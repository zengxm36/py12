#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']


d1 = {'a':1, 'b':2, 'c':3}
d1['a']

#可以通过key放入字典
d1['f']=6
d1

#一个key只能对应一个value
#多次对一个key放入value，后面的值会把前面的值冲掉

d1['f']=7
d1 
d1['g'] # key 不存在时报错

'g' in d1  #检查key是否存在于字典中


d1.get('g',-1) # 如果key不存在于字典中，可以将其设置成返回特定值

#删除key
d1.pop('a')
d1

##要注意dict的key是一定不能变的
##字符串/整数不可变，可以作为key，但是list不行

d1['asd'] = 100

d1[['a',1,2,3]] = 1000 #提示报错，不能为list
list1 = [1,2,'a2']
d1[list1]

tubble1 = (1,2,3,'a') #元组可以放进dict里面
d1[tubble1] = 'cfd'
d1

tubble2 = (list1, 1, 2, '3')
d1[tubble2] = 2 #但是如果元组里面包含了list就不行


#set 
#set和dict的区别在于 set只有key，而没有对应的value
#因此要注意set和dict一样，都不可放入重复的对象

s = set([1,2,3,4]) #创建一个set需要提供一个list进行输入
s # set里面有1 2 3 4 这四个元素，不代表他们是有序的，只是储存着这四个元素而已

s1 = set([1,2,3,3,4,4])
s1  #set里面不能有重复元素，重复元素会被过滤

s1.add(8)
s1

s1.remove(0)
s1

#set可以看成数学意义上的无序和无重复元素的集合
s2 = s1 & s
s2  #求交集

s3 = s1 | s2
s3  #求并集


#关于对象的可变和不可变
#请注意str 字符串一定是一个 不可变的 对象！

a = 'abc' 

a.replace('a',"A") #对变量a进行replace操作，虽然返回的是Abc
#但是，这个操作实际上是对对象'abc'进行操作
#创建了一个新的字符串'Abc'并返回
a #因此 变量a 指向的 对象'abc' 是一直保持不变的
#字符串永远是一个不变的对象
#对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容
#这些方法会创建新的对象并返回，保证了不可变对象本身永远是不可变的

#可以理解为

a = 'abc'
b = a.replace('a','A')
print(b)
print(a)  