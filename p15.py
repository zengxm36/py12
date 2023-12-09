#递归 计算阶乘n!
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

fact(1)
fact(19)
fact(1000) #递归调用的次数过多，会导致栈溢出


#要把每一步的乘积传入到递归函数中
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

fact_iter(2)


#汉诺塔的移动可以用递归函数非常简单地实现。

#请编写move(n, a, b, c)函数，它接收参数n
#n表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(5,'a','b','c')