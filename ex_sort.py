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

students.sort(key=student_sort_key)

print(students)