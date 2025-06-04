# 放在set集合里面的元素不能重复，数据具有唯一,数据没有顺序
# 使用{}定义一个set
# names = {'jack','tom','leon'}
# empty_set = set() 定义一个空的set
name_set = {'tony','philip','bob'}
name_set.add('william')
name_set.remove('tony')
name_set.discard('mary') # 使用discard方法删除不存在的元素不会报错，会忽略
print(name_set)
# 使用in判断元素在不在set里面

print('tom' in name_set)
# 使用set.add()方法添加元素
# names.add('william')
# 使用pop()会随机删除一个元素，并且返回删除的元素
# new_set = frozenset(set) # frozenset 不可改变，没有add，remove等方法

frozenset_1 = frozenset(name_set)

for name,item in enumerate(name_set,1): # 从索引1开始遍历集合name_set
    print(f'{name}-{item}')