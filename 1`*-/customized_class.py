"""
定制类

"""

from collections.abc import Iterable

# __str__

class Student():
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.__name

    # 调试模式打印
    # def __repr__(self):
    #     return 'try'

    __repr__ = __str__

s = Student('herry')

print(Student('Mary'))


# __iter__
# 如果一个类想被用于for...in循环，类似list或者tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
# 然后，python的for循环就会不断调用该迭代对象的__next__() 方法拿到循环的下一个值，直到遇到StopIteration错误推出循环

class Fib():
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self   # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)

# __getitem__
# Fib实例虽然能够作用for循环，看起来和list有点像，但是把它当成list来使用还是不行，比喻取第5个元素
print(isinstance(Fib(), Iterable))

# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法

class Fib1():
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            # print(x)
            a, b = b, a+b
            # print(a)
        return a

print(isinstance(Fib1(), Iterable))    # False
f = Fib1()
print(f[100])

# __getattr__

# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时吗，我们用instance.method()来调用
# 能不能在实例本身上调用呢
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用

class Student3():

    def __init__(self, name):
        self.name = name

    # 直接对实例进行调用
    def __call__(self):
        print('My name is %s' % self.name)

s3 = Student3('LIU')

# 直接调用实例
s3()

# callable() 函数，我们可以直接判断一个对象是否是"可调用对象"
print(callable(s3))
print(callable(Student3))
print(callable(s))












