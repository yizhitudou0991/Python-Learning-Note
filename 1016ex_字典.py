# 字典这种数据结构存放的数据是键值对（key-value)
# empty_dict = {}
# student = {
#     'name':'jack',
#     'age':23,
#     'hobbies':['basketball','football']
# }

student = { # key键值不能重复
    'name':'tom',
    'age':23,
    'hobbies':['game','travel','swimming']
}
student['gender'] = 'male'
student['gender'] = 'famale' # 修改gender的值

print(student['name'])
print(student.get('name')) # get可以叫student的成员方法

print(student['gender']) # gender如果不存在，会报错
print(student.get('gender')) # 不会报错，返回none
print(student.get('school','A')) # A 叫缺省值，如果没有school，就返回A

# del student['name'] # 使用del删除键值

for data in (student.items()):
    print(type(data))
    print(data[1])
for key in student.keys():
    print(student.get(key))
for s in student.keys():
    print(s)
for value in student.values():
    print(value)
