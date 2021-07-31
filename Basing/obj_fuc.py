"""
获取对象信息
type(): 判断对象类型
type()函数是返回的class类型
isinstance()
dir()
"""

# 判断一个对象是否是函数

import types

def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)   # 内建函数
print(type((x for x in range(10))) == types.GeneratorType)   # 判断是否是生成器


# 使用isinstance(), 用来判断class的类型
# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
# 并且还可以判断一个变量是否是某些类型中的一种

print(isinstance([1, 2, 3], (list, tuple)))

# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

# 获取一个对象的所有属性和方法，可以使用dir()函数,他会返回一个包含字符串的list
print(dir('ABC'))

print(len('ABC'))
print('ABC'.__len__())

# obj
class Mylen():

    def __len__(self):
        return 100


dog = Mylen()
print(dog.__len__())
print(dir(dog))

print('ABC'.__len__())

# 仅仅把属性和方法列出来是不够的，配合getattr(), setattr(), hasattr(), 我们可以直接操作一个对象的状态
class Myobject():

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = Myobject()

# 判断是否有属性
print(hasattr(obj, 'x'))
print(obj.x)

print(hasattr(obj, 'y'))

# 设置一个属性
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)

print(dir(obj))

# 可以传入一个default参数，如果属性不存在，就会返回默认值
print(getattr(obj, 'z', 500))

# 也可以获取对象的方法
print(hasattr(obj, 'power'))



























