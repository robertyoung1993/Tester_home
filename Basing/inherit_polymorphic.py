"""
继承和多态
继承：
多态：
"""

class Animal():
    def run(self):
        print("Animal is running...")


class Dog(Animal):

    # def run(self):
    #     print("Dog is running...")

    def eat(self):
        print("Eating meat...")

class Cat(Animal):

    def run(self):
        print("Cat is running...")

    def eat(self):
        print("Eating meat...")

# 继承的好处就是，子类获得了父类的全部功能

# dog = Dog()
# dog.run()
#
# cat = Cat()
# cat.run()

class Tortoise(Animal):

    def run(self):
        print("Tortoise is running slowly...")


# 多态：多态是指一类事物有多种形态
# 多态性是指具有不同功能的函数可以使用相同的函数名，这样就可以用一个函数名调用不同内容的函数。
# 在面向对象方法中一般是这样表述多态性：向不同的对象发送同一条消息，不同的对象在接收时会产生不同的行为（即方法）。
# 也就是说，每个对象可以用自己的方式去响应共同的消息。所谓消息，就是调用函数，不同的行为就是指不同的实现，即执行不同的函数。


def run_twice(ins):
    ins.run()
    ins.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())


#
# 静态语言 vs 动态语言
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
#
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
#
# class Timer(object):
#     def run(self):
#         print('Start...')
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
#
# Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，
# 都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象









