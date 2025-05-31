num_list = [2,4,8,6,1]

num_list.sort()

print(num_list)

students = [
    ('Jack',12),
    ('Tom',13),
    ('Mary',11)
]

def student_sort_key(student):
    return student[1]

students.sort(key=student_sort_key,reverse=True) # 按照年龄倒序排列

print(students)

#sorted（）函数
age_list=[22,35,10,18]
new_age_list = sorted(age_list,reverse=True) #sorted()函数获取一个新的列表
print(new_age_list)