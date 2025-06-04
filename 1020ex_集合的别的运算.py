# 差集：使用difference（）方法，或者减号-
set_1 = {2,3,4}
set_2 = {3,4,5}
print(set_1.difference(set_2))
print(set_1 - set_2)

# 对称差集：去掉a和b共同的部分，剩下的部分合在一起，使用symmetric_difference()方法或者^操作符
print(set_1.symmetric_difference(set_2))
print(set_1 ^ set_2)

# 子集：判断a是不是b的子集，使用issubset或者<=操作符，超集用>=或者issuperset（）方法

# 不相交：isdisjoint（）方法
print(set_1.isdisjoint(set_2))