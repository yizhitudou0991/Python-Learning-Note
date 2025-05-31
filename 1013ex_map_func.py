# map()函数通过遍历每一个集合中的元素并对每一个元素执行给定的操作，返回一个迭代器让使用者取得一个结果集
# iterator = map(function,list)

# 把一个列表中的所有工资全部提高10%
salaries = [5000,8000,7500,4000]
result = []
for s in salaries:
    result.append(s * 1.1)

print(result)

result = list(map(lambda s: s * 1.1,salaries))

print(result)

students = [
    ('jack',23),
    ('tom',21),
    ('mary',20)
]
ages =sorted(list(map(lambda s: s[1],students)))
print(ages)