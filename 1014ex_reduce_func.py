# reduce()函数用于对一个list进行求解，并得到一个唯一的结果，reduce的目的是计算，从列表里面拿2个元素给function计算，得到的结果
# 再和另一个元素进行计算

# result = reduce(function,list)

from functools import reduce

nums = [5,2,3,9]

def f(a, b):
    res = a + b
    print(f'{a},{b} = {res}')
    return res


result = reduce(f, nums)

# result = reduce(lambda a, b: a+b,nums)

print(result)

