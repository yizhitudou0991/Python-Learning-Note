# 可以认为每一个py程序文件就是一个模块，模块里面可以包含函数，类等多种信息
# from 模块名 import 函数/类名 as 别名
# import 模块名 as 别名
import utils_1023 as utils

res = utils.add(2,3)

print(res)

# from utils_1023 import * # *表示引入utils_1023中的全部函数、类，尽量不要用*，避免混淆
import sys
for path in sys.path:
    print(path)
"""
# __name__变量
1、当直接执行一个程序文件时，__name__变量的内容就是'__main__'
2、当一个程序文件被其他文件引入时，__name__变量的内容就是模块名

包的使用：
1.包对应着文件夹
2.每一个包文件夹下面必须有一个__init__.py文件 # 新版本的python不需要有这个文件
3.可以使用from ... import ...来引入不同包中的模块
"""