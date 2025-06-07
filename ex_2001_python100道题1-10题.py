# 2.找出100以内偶数
list = []
for i in range(1,100):
    if i % 2 == 0:
        list.append(i)
print(list)

# 3.找出100以内的奇数
list2 = []
for b in range(1,100):
    if b % 2 != 0:
        list2.append(b)
print(list2)

# 4.判断素数
# 在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数叫素数，素数也叫质数。
a = 37
flag = False

for i in range(2,a):
    if a % i == 0:
        flag = True
        break
if flag:    #flag本身的布尔值为True
    print('是合数')
else:
    print('是素数')

# 5.求阶乘
# 一个正整数的阶乘是所有小于以及等于该数的正整数的积，并且0的阶乘为1，自然数n的阶乘写作n！

def jiecheng(n):
    result = 1
    for i in range(1,n+1):
        result = i * result
    return result

n = int(input('输入一个正整数： '))
f = jiecheng(n)
print(f)

# 递归法
def jiecheng2(num):
    if num == 1:
        return 1
    else:
        return num * jiecheng2(num - 1)
print(jiecheng2(6))

# 方法3：使用math标准库(最简单的方法）
import math
n = int(input('输入一个正整数：'))
print(f'{n}!={math.factorial(n)}')

# 6.求圆的周长=2Πr = Πd
pi = 3.14
r = float(input('请输入半径： '))
c = 2 * pi * r
print(f'圆的周长是: {c}')

# 7.求圆的面积 = Πr*r
pi = 3.14
r = float(input('请输入半径: '))
s = pi * r *r
print(f'圆的面积是：{s}')

# 8.求直角三角形斜边长
# 勾股定理： a^2 + b^2 = c^2
import math
a = int(input('请输入第一条直角边长：'))
b = int(input('请输入第二条直角边长：'))
m = a * a + b * b
c = math.sqrt(m)    # math.sqrt方法求根
print(f'直角三角形斜边长为{c}')

# 9.比较三个数的大小
a = int(input('请输入第一个数字： '))
b = int(input('请输入第二个数字： '))
c = int(input('请输入第三个数字： '))

list = [a,b,c]
list1 = sorted(list)
print(f'三个数字从小到大分别是：{list1[0]}，{list1[1]}，{list1[2]}')

# 10.找出区间内的素数
# 编写程序，输入整数a、b表示一个闭区间，找出该区间内的所有的素数并打印
def prime(n):
    if n < 2:
        return False
    for h in range(2,n):
        if n % h == 0:
            return False
    return True

a = int(input('请输入左端点：'))
b = int(input('请输入右端点：'))
list3 = []
for h in range(a,b+1):
    if prime(h):
        list3.append(h)
print(list3)