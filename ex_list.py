# list是一个链表数据结构的实现，可以存放多个数据再一个list中
# empty_list = []
# name_list = ['Jack','Tom','Mary']
# age_list = [20,30,12,34]
# coordinates = [[0,1],[1,2],[3,3]]

name_list = ['Jack','Tom','Mary']

print(name_list)

print(name_list[1]) # 查：列表里面索引为1的数据
print(name_list[-1])

for name in name_list:
    print(f'>{name}')

name_list.append('Bob') # 再列表里面扩充一个元素 Bob
print(name_list)

name_list.insert(1,'Jeff') # 在列表索引为1的位置插入元素 Jeff

# del name_list[3] # 删除列表下标为3的元素

# name_list.pop() # 删除末尾的元素
# name_list.pop(0) # 删除索引为0的元素
# name_list.remove('Bob') # 删除Bob
# name_lis[3] = 'ruby' # 把索引为3的元素改为ruby
