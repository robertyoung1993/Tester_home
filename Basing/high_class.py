"""
使用__slots__
"""

from types import MethodType

class Student():
    pass

s = Student()
# 动态给实例绑定一个属性
s.name = 'Miky'
print(s.name)

# 给实例绑定一个方法
def set_age(self, age):
    self.age = age

# 给实例绑定一个方法
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# 但是给一个实例绑定的方法，对另一个实例是不起作用的
# s2 = Student()
# s2.set_age(25)

# 为了给所有实例都绑定方法，可以给class绑定方法

def set_score(self, score):
    self.score = score

Student.set_score = set_score
s.set_age(34)
print(s.age)

# 使用__slots__
# 但是我们想要限制实例的属性怎么办，比喻只允许对Student实例添加name和age属性
# 为了达到限制的目的，python允许在定义class的时候，定义一个特殊的__slot__变量，来限制class实例添加的属性
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。

class Student1():
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

s1 = Student1()
s1.name = 'Michael'
s1.age = 23
# s1.score = 100

print(s1.name)
print(s1.age)
# print(s1.score)





































