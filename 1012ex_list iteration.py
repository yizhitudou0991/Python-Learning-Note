# 迭代就是遍历整个数据结构
ages = [23,18,21,30]

for index,age in enumerate(ages,1):   # 返回索引和年龄的列表,索引的起始值为1
    print(f'{index}-{age}')

# iterator(迭代器) 是一个用来遍历目标数据的工具，使用iter()函数来得到

it = iter(ages)
print(type(it))
print(next(it))

for age in it:
    print(age)