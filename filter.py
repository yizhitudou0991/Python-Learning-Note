# filter 函数的用法

age = [25, 30, 19, 17]  # 定义一个年龄的列表

# 使用lambda函数，传入参数i，i的条件是i>20,在age中满足条件的i留下，不满足的i剔除

age1 = filter(lambda i: i > 20, age)

print(list(age1))  # 将返回值转换成列表打印出来:[25,30]

# 简写方式
# 将年龄大于20岁的列举出来

age = [19, 17, 25, 30]

print(list(filter(lambda x: x > 20, age)))  # 一行代码解决问题,打印的结果为[25,30]

students = [("周大大",23), ("王火山",22),("芋圆",18)]

"""
使用lambda函数，设置变量i，i是存在于students中元组，对于i的第二个值，如果值大于20则满足条件，保存下来，否则剔除，最后将返回值打印出来
"""
print(list(filter(lambda i: i[1] > 20, students)))

# 打印的结果：[("周大大"，23),("王火山，"22)]