# # 解包列表
nums = [3,5,6,8]
n1 = nums[0]
n2 = nums[1]
n3 = nums[2]

n1,n2,*n3 = nums # *n3包含了剩余的变量

print(n1)
print(n2)
print(n3)   # 是个列表

data = ['jack',23,'this is a strong guy','he is a gay']
name,age,*desc = data

print(age)
print(desc)

