"""
元类
"""

# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的

# class Hello():
#     def hello(self, name='world'):
#         print('Hello, %s.' % name)
#
# h = Hello()
# print(type(Hello))   # <class 'type'>
# print(type(h))       # <class '__main__.Hello'>

# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比喻，我们可以通过type()函数创建Hello类，而无需通过class Hello() 的定义

# 定义函数
def fn(self, name='world'):
    print('Hello, %s.' % name)


# type(类名称(字符串), 基类(元组), 属性/方法(字典))
# 利用type创建一个Hello类
Hello = type('Hello', (object, ), dict(hello=fn))

h = Hello()
h.hello()
print(type(Hello))
print(type(h))

# 要创建一个class对象，type()函数一次传入3个函数
# 1、class名称
# 2、继承的父类集合，注意python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法
# 3、class的方法名称和函数绑定，这里我们把函数fn绑定到方法名hello上

# 通过type()函数创建的类和直接写class是完全一样的，因为python解释器遇到class定义时，仅仅是扫描一下class定义的语法，
# 然后调用type()函数创建出class


# metaclass
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
# 元类：当我们定义了元类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例
# 但是如果我们想要创建出类呢？那就必须根据metaclass创建出类，所以先定义metaclass，然后创建类
# 连接起来就是：先定义metaclass,就可以创建类，最后创建实例
# 所以metaclass允许你创建类会或者修改类。换句话说你可以把类看成是metaclass创建出来的实例









