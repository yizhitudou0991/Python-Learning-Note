# 组合
class 叶问(object):
    def __init__(self,x):
        self.功夫 = x
class 李小龙(object):
    def __init__(self,x):
        self.功夫 = x

class 香港(object):
    def __init__(self,x,y):
        self.叶问 = 叶问(x)
        self.李小龙 = 李小龙(y)
    def 次数(self):
        print(f'在香港，叶问使用功夫{self.叶问.功夫}次，李小龙使用功夫{self.李小龙.功夫}次')

对象 = 香港(1,10)
对象.次数()

# 私有权限
# 1、作用：如果在继承关系中，某些属性或方法不想继承给子类时，我们把这些属性和方法添加私有权限
# 2、设置私有权限的方式：在属性名和方法名前面加上两个下划线__
# 3、私有属性和方法只能在类里面进行访问和修改
# 4、在python中，一般定义函数名get_xx用来获取私有属性，定义set_xx用来修改私有属性值。用get和set是工作习惯，可以改名，
# 但是看到这两个单词大家都知道是获取和修改
# 5、先获取后修改
class 叶问(object):
    def __init__(self):
        self.功夫 = '咏春'
    def 实例方法(self):
        print(f'使用{self.功夫}')
class 李小龙(object):
    def __init__(self):
        self.功夫 = '截拳道'
    def 实例方法(self):
        print(f'使用{self.功夫}')
class 华帝(李小龙,叶问):
    def __init__(self):
        self.功夫 = '健身'
        self.__武器 = '屠龙刀' #将武器设置为华帝的私有属性
        self.武器2 = '倚天剑' #武器2是共有属性
    # 获取
    def get_武器(self):
        return self.__武器
    # 修改
    def set_武器(self):
        self.__武器 = '天魔琴'
    def 公有方法(self):
        print('公有方法')

    def __私有方法(self): #将方法设置为私有方法
        print('私有方法')
    def 实例方法(self):
        self.__init__()  #如果是先调用了父类的属性和方法，父类的属性会覆盖子类属性，故在调用前，先调用自己子类的初始化
        print(f'使用{self.功夫}')
    def 叶问_实例方法(self):
        叶问.__init__(self)
        叶问.实例方法(self)
    def 李小龙_实例方法(self):
        李小龙.__init__(self)
        李小龙.实例方法(self)
class 大宝(华帝):
    pass

对象2 = 大宝()
# 对象2.__武器 #武器是华帝的私有属性，大宝无法继承，运行时会报错
print(对象2.武器2)
对象2.公有方法()
# 对象2.__私有方法() #运行会报错
对象3 = 华帝()
# 调用get_武器函数获取私有属性武器的值
print(对象2.get_武器())
# 调用set_武器函数修改私有属性武器值
对象2.set_武器()
# 查看修改后的武器值
print(对象2.get_武器())

# super方法：调用父类方法
class 叶问(object):
    def __init__(self):
        self.功夫 = '咏春'
    def 实例方法(self):
        print(f'使用{self.功夫}')

class 李小龙(叶问):
    def __init__(self):
        self.功夫 = '截拳道'
    def 实例方法(self):
        print(f'使用{self.功夫}')
        super().__init__() #在李小龙的实例方法下面加super
        super().实例方法() #在李小龙的实例方法下面加super
class 孙兴华(李小龙):
    def __init__(self):
        self.功夫 = '健身'
    def 实例方法(self):
        self.__init__()  #如果是先调用了父类的属性和方法，父类的属性会覆盖子类属性，故在调用前，先调用自己子类的初始化
        print(f'使用{self.功夫}')
    def 叶问_实例方法(self):
        叶问.__init__(self)
        叶问.实例方法(self)
    def 李小龙_实例方法(self):
        李小龙.__init__(self)
        李小龙.实例方法(self)

# # 一次性调用叶问和李小龙的同名属性和方法
#     def 叶问和李小龙实例方法(self):
#         叶问.__init__(self)
#         叶问.实例方法(self)
#         李小龙.__init__(self)
#         李小龙.实例方法(self)
# 对象4 = 孙兴华()
# 对象4.叶问和李小龙实例方法()
    def 叶问和李小龙实例方法(self):
        super().__init__()
        super().实例方法()

对象4 = 孙兴华()
对象4.叶问和李小龙实例方法()