# {表达式 for 元素 in set if条件}
grade_set = {50,70,66}

new_grade_set = {grade * 1.2 for grade in grade_set if grade >= 60}
print(new_grade_set)

# 并集方法：
# union或者|

grade_set1 = {50,70,66}
grade_set2 = {55,66,78}
res_1 = grade_set1.union(grade_set2)
print(grade_set1)
print(grade_set2)
print(res_1)
# 集合的union()方法合并的对象可以是集合以外的可迭代对象，|只能对两个set集合进行运算

# 交集：求两个集合的共同部分，intersection（）方法，或者&，同样，&只能对set集合进行运算
