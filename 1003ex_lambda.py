# lambda :lambda 参数列表:表达式
def my_func(name):
    return f'hello {name}'
f = my_func
print(f("Tom"))

ff = lambda name:f'hello {name}'
print(ff('Jack'))

def display(name,greeting):
    result = greeting(name)
    print(result)

display('Mary',lambda name:f'Hello {name}')


def times(n):
    return lambda x: x * n


double = times(2) # double = lambda x: x * 2

print(double(2))
print(double(3))

callables = []
for i in range(1,4):
    callables.append(lambda:i)
for f in callables:
    print(f()) # 打印的结果为三个3，因为第28行循环变量i在循环结束后仍然存在，并且保留最后一个值，循环结束的时候i是3

callables = []
for i in range(1,4):
    callables.append(lambda a = i:a)
for f in callables:
    print(f())