# 异常不是语法错误，而是在程序运行中，python解释器不能处理的问题
'''
try:
    可能会产生异常的代码部分
except:
    如果上面的代码出现了异常，则运行这个部分
else:
    代码没有异常，则运行这个部分
'''

num = input('enter a number：')
try:
    ss = int(num)
    res2 = 10/ss
    res = 10/2 #如果不放在try下面，则会报错，division by zero
    print(res)
except ValueError as e:    # 输入的值为字符串的时候的错误
    print('please input i integer number')
    print('found problem')
except ZeroDivisionError as e:  # 输入的数字为0时的错误
    print('please input a non-zero number')
else: # try下面的部分正常运行，则运行这一部分
    print('run successfully')
finally: # 任何时候都会运行
    print('game over')

"""
合并多个异常
try:
    可能产生异常的代码部分
except(exception1,exception2,exception3):
"""

