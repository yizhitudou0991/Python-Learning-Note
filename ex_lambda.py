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