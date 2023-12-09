#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

#for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句
num = [1,2,3,4,5,6]
for nums in num:
    print(nums)

num = list(range(1,11))
for nums in num:
    print(nums)

num = list(range(1,11))
sum = 0
for nums in num:
    sum = sum + nums
print(sum)


num = list(range(1,101))
sum = 0
for nums in num:
    sum= sum+ nums
print(sum)


sum = 0
n=100
while n>0:
    sum = sum+n
    n=n-1
print(sum)

sum = 0
n=100
while n>0:
    if n<10:
        break
    sum = sum + n
    n = n-1
print(sum)

sum = 0
n=100
while n>0:
    if n<10:
        break
    print(n)
    n = n-1
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for names in L:
    print('Hello',names ,'!')