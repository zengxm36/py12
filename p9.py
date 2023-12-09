#!/usr/bin/env python3
# -*- coding: utf-8 -*-

score = 'D'

match score:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B.')
    case 'C':
        print('score is C.')
    case _: 
        print('score is:', score)

age = 15

match age:
    case x if x<10:
        print("age is under 10")
    case 10:
        print("age is 10")
    case 20|21|22|23:
        print('age is over 20')    
    case _:
        print('else')

#模式匹配可用于列表list，而且可以将列表中的元素赋值至特定变量
#可以对list中的元素进行模式匹配
args = ['gcc', 'hello.c', 'world.c']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' 'file1,', ','.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')

#.join的用法，将序列中的元素以指定的字符连接生成一个新的字符串
symbol = "-";
seq = ("a", "b", "c"); # 字符串序列
print(symbol.join(seq))
print(','.join(seq))