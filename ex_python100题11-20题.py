# 11.组合数字：用1、2、3、4四个数字能组成多少个互不相同且无重复数字的三位数，各是多少？
for i in range(1,5):
    for j in range(1,5):
        for m in range(1,5):
            if (i != j) and (i != m) and (j != m):
                print(f'{i}{j}{m}')


# 12.打印乘法口诀表
for i in range(1, 10):
    for j in range(1,i+1):
        print(f'{j}x{i} = {j*i:<2}',end='\t')
    print()

# 13.水仙花数，找出三位数的水仙花数
result = []
for i in range(100,1000):
    a = i % 10
    b = i // 10 % 10
    c = i // 100
    if a ** 3 + b ** 3 + c ** 3 == i:
        result.append(i)
print(f'三位数的水仙花数有{result}')

# 14.反向输出四位数：编写程序，输入一个四位整数，反向输出对应四位数

a = int(input('请输入一个四位整数： '))

a = str(a)
a = a[::-1]
a = int(a)
print(a)

# 15.判断字母：编写程序，输入字符，判断是否为字母
a = input('请输入内容： ')
result = a.isalpha()
if result:
    print(f'{a}是字母')
else:
    print(f'{a}不是字母')


# 16.判断三角形：输入三组数据，判断能否构成三角形的三条边
a = int(input('请输入第一条边： '))
b = int(input('请输入第二条边： '))
c = int(input('请输入第三条边： '))

if a <= 0 or b <= 0 or c <= 0:
    print('输入的数据不合法！')
if a+b > c and a+c >b and b+c >= a:
    print(f'这三条边可以是三角形的边')
else:
    print(f'这三条边不能构成三角形')

# 17.完数：找出1000以内的完数，一个数如果签好等于除了他自身以外的因子之和，这个数就成为完数，如6
for i in range(1,1000):
    summary = 0
    for j in range(1,i):
        if i % j == 0:
            summary += j
    if summary == i:
        print(f'{i}是完数')

# 18.找质数因子：输入一个正整数，输出它的所有质数因子
a = int(input('请输入一个自然数： '))
y = 2
list = []
while a >= y:
    if a % y == 0:
        list.append(y)
        a //= y
    else:
        y += 1
for i in list:
    print(i,end=' ')

# 19.海伦公式求三角形面积：p = (a+b+c)/2  s = (p*(p-a)(p-b)(p-c))**0.5
import math
a = int(input('请输入第一条边： '))
b = int(input('请输入第二条边： '))
c = int(input('请输入第三条边： '))

p = (a + b + c)/2
s = math.sqrt(p*(p-a) * (p-b) * (p-c))

print('三角形的面积是%.2f'%s)

# 20.判断某年某天：输入某年某月某天，判断这一天是这一年的第几天
import datetime

year,month,day = map(int,input().split(' '))

yuandan = datetime.datetime(year,1,1)
now = datetime.datetime(year,month,day)
print((now - yuandan).days + 1)
