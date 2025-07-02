# 面向对象-单继承
# 继承的概念：如果两个类存在父子级继承关系，子类即便没有任何的属性和方法，那么用子类继承了某一个父类，
# 并且此子类创建了一个对象，那么这个对象就拥有父类当中的所有属性和方法的使用权。

# 父类-小头爸爸
class 小头爸爸(object): #python3新式类写法，是基类，最高类
    def __init__(self):
        self.age = 30

    def 实例方法(self):
        print(f'小头爸爸的年龄是{self.age}岁')

#子类-大头儿子
class 大头儿子(小头爸爸): #关联父类,大头儿子继承自小头爸爸
    pass #pass占位，不报错

对象 = 大头儿子()
对象.实例方法()

# 面向对象-多继承：同一个类继承了多个父类，当一个类有多个父类的时候，默认使用第一个父类的同名属性和方法

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
class 孙兴华(李小龙,叶问):
    pass

对象2 = 孙兴华()
对象2.实例方法()

# 面向对象-拓展：mro顺序
# 再python中，所有类默认继承自object类，object类是顶级类或基类，其他子类叫做派生类

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
class 土豆(李小龙,叶问):
    pass

对象3= 土豆()
对象3.实例方法()
print(土豆.__mro__) #手动查找继承的顺序

# 子类和父类具有同名的属性和方法那么默认使用子类的同名的属性和方法

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
class 老王(李小龙,叶问):
    def __init__(self):
        self.功夫 = '健身'
    def 实例方法(self):
        print(f'使用{self.功夫}')

对象4= 老王()
对象4.实例方法()

# 需求:既能调用子类的，又能调用父类的
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
class 周老师(李小龙,叶问):
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

对象5 = 周老师()
对象5.实例方法()
对象5.叶问_实例方法()
对象5.李小龙_实例方法()

# 多层继承：
# 多层继承容易导致代码混乱，所以当不确定是否必须使用的时候，尽量避免使用它，因为有些时候会出翔不可预见的bug
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

对象6 = 大宝()
对象6.实例方法()
对象6.叶问_实例方法()
对象6.李小龙_实例方法()





