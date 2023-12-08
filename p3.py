#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#\转义符号,在enter键上面qwq
print('hello')
print("hello","\"")
print('hello\nuser')

# \\表示\ 对\转义，输出一个\，\n表示换行，然后再输出一个\
print('\\\n\\')
#r''表示内部的字符不再进行转义
print(r'\\\n\\')


#用'''...'''的格式表示多行内容
#请在交互式命令行中输入print('''1 

print('''1
2''')

#'''...'''表示可以自己换行，r'''...'''表示r内部的字符不再进行转义，\n直接输出，不表示换行
print(r'''hello,\n
world''')