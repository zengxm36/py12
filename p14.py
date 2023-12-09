#位置参数
def power(x):
    return x**2

power(2)

def power(x,n):
    return x**n

power(3,3)


def power(x,n):
    a=x
    while n>1:
        x=x*a
        n=n-1
    return x

power(2,3)

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


#默认参数
def power(x,n=2): #设置默认参数
    a=x
    while n>1:
        x=x*a
        n=n-1
    return x

power(5)

def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)

enroll(1,2)


def enroll(name, gender,city='canton',age=7):
    print('name:', name)
    print('gender:', gender)
    print('city:',city)
    print('age:',age)

enroll(1,2,'shandong',4)



##默认参数的坑
def add_end(L=[]):
    L.append('END')
    return L

add_end(["1","2"])
add_end([1,2,3])

add_end() ##
#如果反复调用add_end()的话就会出问题
#定义默认参数要牢记一点：默认参数必须指向不变对象！
#这里的list是一个可变的对象，每次调用的时候默认参数都会发生修改！


def add_end(L=None):  #将默认参数定义为None这个不变对象
    if L is None:
        L = []
    L.append('END')
    return L
add_end()



def cal(number=(1,2)):   #设置一个变量名number，默认参数number=(1,2)，然后输入可以输入一个list或者tuple
    sum=0
    for num in number:
        sum = sum + num**2
    return sum 

cal()
cal([1,2,3]) 

#可变参数
def cal(*number): #可变参数不能设置默认值
    sum=0
    for num in number:
        sum = sum + num**2
    return sum 

cal(1,2) #这样输入就不用是一个list或者tuple了
cal()

#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号
#函数内部收到的是一个tuple

num=(1,2,3)
cal(num[0],num[1],num[2]) #如果你已经有一个list或者tuple，想把tuple的元素都变成可变参数传进去
cal(*num)  #可以在list/tuple前面加一个*来解决这个问题

#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用


#关键词参数 **kw是习惯写法
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person(1,2)

person('jason', 33 ,  city='guangzhou' ) #关键词参数输入后识别为字典 dict

person('jason', 33 ,  city='guangzhou', job = 'engineer' ) #可以传入任意多的关键词参数

extra_dict = {'city':'guangzhou', 'job':'engineer'}

person('jasion',12, city=extra_dict['city'], job=extra_dict['job'])
person('jason',12, **extra_dict ) #简单写法

#关键词参数可以是任意的

person('jason',23, apple= "happy" )


#命名关键词参数
#限定关键词参数名字
#加一个*作为特殊分隔符,*后面是关键词参数
def person(name, age, *,city,job):
    print(name,age,city,job)

person(1,2,city='a',job='b')
 
#这个函数，前两个是必须要填的，第三个是可变参数，可以直接填各种东西，最后两个是关键词参数
def person(name, age, *kb,city,job):  
    print(name,age,kb,city,job)

#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
person('jason',12,'happy','sad',city='canton',job='engineer')


#使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符

def person(name, age, *, city, job):
    print(name, age, city, job)

person(1,2,job=4) #报错：TypeError: person() missing 1 required keyword-only argument: 'city'

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person(1,2,job=4) #只有在city有默认参数的情况下，这个才可以不填


#函数的参数存在特定的顺序
#必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f2(a, b, c=0, *args, d, **kw):
    print(a,b,c,args,d,kw)

f2(1,2,3,4,5,d=(1,2),e='1',f=[1,2])

#记住上面的顺序，并说出上面的代码是怎么来的，各个对应什么意思

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)


## https://zhuanlan.zhihu.com/p/412273465