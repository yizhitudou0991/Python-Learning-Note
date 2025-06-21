# 闭包的作用：
# 1、外部函数中定义了内部函数
# 2、外部函数是有返回值的
# 3、返回值是：内部函数名
# 4、内部函数使用了外部函数的变量值


def a1(a,b):
    c = 1
    def a2():
        s = a+ b + c
        print(f'相加的结果是{s}')
    return a2

n = a1(2,3)
n()

def b1(x):
    def b2(*args,**kwargs):
        print('开始')
        x(*args,**kwargs)
        print('结束')
    return b2

@b1
def b3(name,time):
    print(f'{name}开始吃饭,现在{time}点了')
b3('孙兴华',18)

@b1
def b4(age):
    print(f'我的年龄是{age}岁')
b4(20)

@b1
def b5(name,time,**kwargs):
    print(f'我叫{name},现在{time}了')
    print(kwargs)
b5('孙兴华',18,姓名='李小龙',年龄='80',性别='男')

# 使用装饰器之前，有以下条件：
# 1、存在闭包
# 2、存在需要被装饰的函数
# 3、理解函数地址值的概念，函数的地址值类似于人类的身份证号码
# 闭包：
# 在一个函数中嵌套定义了一个函数
# 1、存在函数的嵌套关系
# 2、内层函数引用了外层函数的变量
# 3、外层函数返回内层函数的地址值

def out_func(num):
    def in_func(in_num): #1、嵌套内层函数
        print(f'外部函数的变量{num}') #2、内层函数引用外层函数变量
        print(f'内部函数的变量{in_num}')
    return in_func # 3、函数名存放着地址值，外层函数返回内层函数
result = out_func(10) #result接收了out_func的地址值
print(result) # 打印结果为in_func的地址值,result = in_func
result(5) #调用函数in_func

# 添加装饰器，需要：
# 1、存在闭包
# 2、存在需要被装饰的函数

def welcome(func):
    def in_func2():
        print('欢迎光临')
        func()
    return in_func2

# 添加装饰
# @闭包的外层函数名
# 装饰器会把login()函数自动传递给welcome
@welcome
def login():
    print('登录成功')
# login == in_func2 ,func == login

login()

# sunxinghua1007@163.com  孙兴华老师邮箱
