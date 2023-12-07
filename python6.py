#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('中文测试')


#格式化字符串
#f-string
s1 = 72
s2 = 85
improved = (s2-s1)/s1

#以f开头的字符串，称之为f-string，它和普通字符串不同之处在于
#字符串如果包含{xxx}，就会以对应的变量替换
print(f'The scored was improved for: {improved}')     #直接替换improved变量
print(f'The scored was improved for: {improved:.1f}') #保留一位小数

#普通的格式化字符串 %s 表示字符串替换 %f 表示浮点数替换 %d 表示整数替换
print('Age: %d. Gender: %s' % (25, 'male'))  

#要替换的内容在括号的里面，在引号的外面，如果只有一个要替换则不用加括号，直接 % 后面跟即可
print('age: %d' % 22) 