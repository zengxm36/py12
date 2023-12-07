age=19
if age > 18:
    print('adult')
    print('your age is over 18')
    print('your age is', age)
else:
    print('your age is under 18')

if age>18:
    print('adult')
elif age> 10:
    print('teenager')

#if语句执行有个特点，它是从上往下判断
# 如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

#if判断简写
if 1: 
    print('True')

#input判断

#input输入是字符串，需要int函数将其转变为整数
age_input = input('your age is:', )
age_input
int_age_input = int(age_input)
if int_age_input > 18:
    print('adult')
else:
    print('not adult')

#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：



height = input('height:')
int_height = int(height)
weight = input('weight:')
int_weight = int(weight)

BMI = int_weight / int_height**2
print(BMI)
if BMI > 32:
    print('fat')
elif 32>BMI>20:
    print('123')
elif BMI < 20:
    print('345')

### int函数若输入为字符串，则必须为整数，否则报错




