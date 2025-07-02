# 大象放冰箱：开门 放入 关门
# 蛇放冰箱：开门 放入 关门
# 老虎放冰箱：开门 放入 关门
# 定义函数（x）：开门(x) 放入（x）关门（x）
# 定义类：
# class 装冰箱
#     def 开门（self，x）
#     def 放入（self，x）
#     def 关门（self，x）  这3个函数又叫实例对象
# 对象1 = 类名（大象）
# 对象2 = 类名（蛇）
# 对象3 = 类名（老虎）
#面向对象（魔法方法，又名构造函数）
# 在python中，__xx__()的函数叫做魔法方法，指的是具有特殊功能的函数。
# 一、__init__()方法的作用：初始化对象
# 1、在创建一个对象时默认被调用，不需要手动调用
# 2、__init__(self)参数，不需要开发者传递，python解释器会自动把当前的对象引用传递过去
# 3、一个类可以创建多个对象，对不同的对象设置不同的初始化属性需要传参数
# 【self = 对象名】
# self指的是调用该函数的对象，由于打印对象名和打印self得到的内存地址相同，所以self值得时调用该函数的对象
# 一个类可以船舰多个对象，但是self地址不相同，因为不同的对象存储的地址不一样
# 和类关联在一起的变量名叫类变量
# 和对象关联在一起的变量叫实例变量
from tkinter.font import names


class Class1():
    def __init__(self,name,age):
        #添加实例属性
        self.name = name
        self.age = age
    def shilifangfa(self):
        print(f'我的姓名是{self.name}，年龄是{self.age}岁')

duixiang1 = Class1('孙兴华',20)
duixiang1.shilifangfa()
duixiang2 = Class1('赵丽颖',33)
duixiang2.shilifangfa()
duixiang3 = Class1('李小龙',80)
duixiang3.shilifangfa()

# 二、__str__()当使用print输出对象的时候，默认打印对象的内存地址。
# 如果类定义了__str__方法，那么就会打印在这个方法中的return的数据。
# 做月饼;
# (1)烤3分钟以下是生的，3-5分钟是半生不熟的，5-8分钟的是熟的，8分钟以上是糊的

class Mooncake():
    def __init__(self):
        #靠月饼的时间
        self.time = 0
        #月饼烤的状态
        self.zhuangtai = '生的'
        #调料列表
        self.tiaoliao_list = []
    def cooktime(self,time):
        #1.先计算月饼烤的时间
        self.time += time
        #2.用整体月饼考过的实际按再判断月饼的状态
        if 0<= self.time < 3:
            self.zhuangtai = '生的'
        elif 3 <= self.time < 5:
            self.zhuangtai = '半生不熟'
        elif 5 <= self.time < 8:
            self.zhuangtai = '熟了'
        else:
            self.zhuangtai = '糊了'

    def add_tiaoliao(self,*tiaoliao):
        self.tiaoliao_list.extend(tiaoliao)
        #书写str魔法方法，用于输出对象状态
    def __str__(self):
        return f'这批月饼被烤过的时间是{self.time}分钟,状态是{self.zhuangtai},调料有{self.tiaoliao_list}'
duixiang4 = Mooncake()
duixiang4.cooktime(2)
duixiang4.add_tiaoliao('蔓越莓','豆沙')
print(duixiang4)

duixiang4.cooktime(4)
duixiang4.add_tiaoliao('蛋黄','蛋液')
print(duixiang4)



