# 找出100到999范围内的所有水仙花数
# 在数论中，水仙花数（narcissistic number）也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个n
# 位非负整数，其各位数字的n次方和刚好等于该数本身，利用python中的//和%运算符很容易做到。

for num in range(100,1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

# 找出1到任意不超过6位数的正整数中的水仙花数(遍历方法）
def find_narcissistic_numbers(n):
    narcissistic_numbers = []
    for num in range(1,n + 1):
        num_str = str(num)
        power = len(num_str)
        total = sum(int(digit) ** power for digit in num_str)
        if total == num:
            narcissistic_numbers.append(num)
    return narcissistic_numbers


n = int(input('请输入一个任意的不超过6位数的正整数： '))
f = find_narcissistic_numbers(n)
print(f'1到{n}之间的水仙花数为{f}')


# 找出1到任意正整数之间的水仙花数（while循环，取余和整除方法）
def find_narcissistic_numbers2(m):
    nar_numbers = []
    for num1 in range(1,m+1):
        temp = num1
        digits = []
        while temp > 0:
            digits.append(temp % 10)
            temp //= 10
        power = len(digits)
        total = sum(i ** power for i in digits)
        if total == num1:
            nar_numbers.append(num1)
    return nar_numbers

m = int(input('请输入任意正整数： '))
result = find_narcissistic_numbers2(m)
print(f'1到{m}之间的水仙花数是：{result}')