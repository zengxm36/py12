#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

def my_abs_pro(x):
    if not isinstance(x,(int,float)):
        print('not legal')
        return
    if x>=0:
        print(x)
    else:
        print(-x)
        return

my_abs_pro(1)
my_abs_pro('a')

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

move(1, 2 , 3 , math.pi / 6) #返回的值不是两个，而是一个元组 tuple 

a = move(1, 2 , 3 , math.pi / 6)

print(a)

quadratic(a, b, c) #定义一个包含三个参数的函数，返回一元二次方程ax**2+bx+c=0的解

def quadratic(a,b,c):
    if not isinstance(a,(int,float)) or isinstance(b,(int,float)) or isinstance(c,(int,float)) :
        print('not legal input')
        return
    elif b**2-4*a*c<0:
        print('no legal solve')
        return
    elif b**2-4*a*c>0:
        x1 = (-b + math.sqrt(b**2-4*a*c))/2*a
        x2 = (-b - math.sqrt(b**2-4*a*c))/2*a
        print(x1,x2)
    else:
        x = (-b + math.sqrt(b**2-4*a*c))/2*a
        print('x1=x2=',x)
    return

quadratic(1,1,1) #方程组无解
quadratic(1,2,-4)
quadratic(1,2,1)
quadratic(1,'2',2)

isinstance('a',(int,float)) and isinstance('b',(int,float)) == False

False and False == False