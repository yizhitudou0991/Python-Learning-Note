# # tuple其实是一个内容不能改变的list。定义tuple使用的是（）,tuple中的元素可以是不同的类型
# empty_tuple = ()
# one_element_tuple = (2,)
# normal_tuple = (2,3,4)
# default_tuple = 3,4,5

num_tuple = 3,4,5

print(type(num_tuple))

def my_func():
    return True,'I finished it successfully'

t = my_func()
print(type(t))

# tuple的访问方式和list相同
nums = (2,3,4,5)
print(nums[:3])

print(max(nums))
print(min(nums))

extend_tuple = (2,3) + (5,6)
print(extend_tuple)

nn = (2,3) * 3
print(nn)

print(2 in nn)

