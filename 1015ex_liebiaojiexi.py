# 列表解析是对一个列表进行操作生成一个新的列表的过程
# [输出表达式 for 元素 in 列表]
nums = [2,3,4]

print(list(map(lambda a: a * a,nums)))

print([a * a for a in nums]) # nums中的数取平方

# 带条件的列表解析
print([b * b for b in nums if b > 2])
