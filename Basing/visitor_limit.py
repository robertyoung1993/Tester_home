"""
私有属性，访问限制
如果要内部属性不被外部访问，可以把属性的名称前加上两个下划线__，就变成了一个私有变量，只有内部可以访问
"""

class Student():

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

# bart = Student('young', 98)

# 外部代码要访问name和score

class Student1():

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


Dart  =Student1('Young', 100)

# print(Dart.get_name())
# print(Dart.get_score())


# 允许外部代码修改score
# 非私有变量也可以直接修改属性，为啥要定义一个方法，因为在方法中，可以对参数做检查，避免输入无效的参数

class Student2():

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('unsafe score')

    def set_name(self, name):
        if len(name) > 0:
            self.__name = name
        else:
            raise ValueError('name is not allowed to be empty!!! ')

part = Student2('liuchong', 83)

print(part.get_name())
print(part.get_score())

part.set_score(100)
part.set_name('chenmeng')

print(part.get_name())
print(part.get_score())

# part.set_score(101)
# part.set_name('')
#
# print(part.get_name())
# print(part.get_score())