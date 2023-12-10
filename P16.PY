#比如构造一个1, 3, 5, 7, ..., 99的列表，可以通过循环实现

n=1
L=[]
while n<=99:
    L.append(n)
    n=n+2
print(L)



list99 = list(range(1,100))
L=[] 
for num in list99:
    if num%2 == 0:
        continue
    L.append(num)

print(L)


#切片 取一个list或tuple的部分元素是非常常见的操作
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
newL = [L[0],L[1],L[2]]
print(newL)

list(range(3))

r=[]
n=list(range(1,4))
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
for num in n: 
    r.append(L[num])
r

##开始切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L[0:3]
L[0:1]
L[0:4]
L[-3:-1]
L[-1]

list99 = list(range(1,100))
list10 = list99[0:10]
print(list10)

list99[1:10]   #1：10实际上就是 2到11，11取不到，所以是2-10，有多少个数字就是10-1
list99[1:10:2] #后面加一个 :2意思是隔两个数取一个
list99[:]      #取所有数
list99[::3]    #所有数隔三个取一个

#tuple也是一种list，唯一区别是tuple不可变，所以切片操作是一样的

t100 = tuple(range(1,101))
t100[0:80:2]

#字符串'xxx'也可以看成是一种list，每个元素就是一个字符
#字符串也可以切片
str1 = 'abcdefg'
str1[0:3]

str2 = ' a vcf '


def trim(str2):             ##错误的，记得原因是
    n = 100
    new_str = []
    for i in range(n):
        if str2[i] == ' ':
            continue
        elif i>len(str2):
            break
        else:
             new_str.append(str2[i])
    print(new_str)

trim(' a v cf ')

list(range(0,100))

range(0,100)

range(100)

range(len(str2))


def trim(str2):
    n = 100
    new_str = []
    for i in list(range(n)):
        if i>=len(str2):
            break
        elif str2[i] == ' ':
            continue
        else:
             new_str.append(str2[i])
    print(new_str)

trim(' a v cf ')

#更好的写法
def trim(str2):
    new_str = []
    for i in range(len(str2)):
        if i>=len(str2):
            break
        elif str2[i] == ' ':
            continue
        else:
             new_str.append(str2[i])
    new_str = ''.join(new_str)
    print(new_str)



trim(' a v cf ')
len(str2)
str2[7]

trim('a hd  dj si msn ')

def trim(str3):
    new_str3 = []
    for i in list(range(len(str3))):  
        if i ==0 and str3[i] == ' ':
            continue
        if i == len(str3)-1 and str3[i] == ' ':
            break 
        else:
            new_str3.append(str3[i])  #典型错误new_str3 = new_str3.append(str3[i]) append会修改L本身，并且返回None。不能把返回值再赋值给L
    result_str = ''.join(new_str3)
    print(f"\'{result_str}\'")
trim(' a hd  dj si msn  ') 
##如果首尾有很多空格就不行了

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


def trim(s):
    if s[-1:]==' ' :
        return trim(s[:-1])
    elif s[:1]==' ':
        return trim(s[1:])
    else:
        return s
