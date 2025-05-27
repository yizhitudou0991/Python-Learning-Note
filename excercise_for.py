tip = 'Enter a number'
str_num1 = input(tip + '1: ')
str_num2 = input(tip + '2: ')

num1 = int(str_num1)
num2 = int(str_num2)

result = 0
for num in range(num1,num2+1):
    result = result + num

print(result)