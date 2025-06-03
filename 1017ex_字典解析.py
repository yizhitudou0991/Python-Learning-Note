# 字典解析类似于列表解析
# new_dict = {key:value for (key,value) in dict.items()}
grades = { # 成绩的字典
    'jack':70,
    'tom':30,
    'bob':60
}

new_grades = {name: int(grade * 1.1) for (name,grade) in grades.items() if grade >= 60} # 成绩大于60乘以1.1

print (new_grades)

# 字典合并
# {**dict1,**dict2}
student = {
    'name':'jack',
    'gender':'male',
    'math':80
}
ext = {
    'math':78,
    'english':90
}
new_student = {**student,**ext}
print(new_student) # math的值为后面的字典ext里面的值78