"""
多重继承
通过多重继承，一个子类就可以获得多个父类的所有功能
"""

class Animal():
    pass

# 大类
# 哺乳类
class Mammal(Animal):
    pass

# 鸟类
class Bird(Animal):
    pass

# 各种动物
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

# 动物行为
class Runnable():
    def run(self):
        print('Running...')

class Flyable():
    def fly(self):
        print('Flying...')

# 对于需要runnable功能的动物就多继承一个
class Tiger(Mammal, Runnable):
    pass

# 对于需要Flyable功能的动物，就多继承一个Flyable
class  Seagull(Bird, Flyable):
    pass

#

















