"""
@property的使用
在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是没有办法检查参数，导致可以把成绩随便改
"""
# 比喻修改成绩为999，这显然是不合理的

class Student():

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError("score must be an integer!")
        if score < 0 or score > 100:
            raise ValueError('score must be range 0 to 100!')
        else:
            self.__score = score

s = Student('Young', 98)
print(s.get_score())

s.set_score(99)
print(s.get_score())

# s.set_score(9100)
# print(s.get_score())

# 但是上面的调用方法有点复杂，没有直接用属性这么直接简单
# 有没有既能检查参数又可以用类似属性这样的简单的方式来访问类的变量
# 装饰器是可以给函数动态的加上功能  @property装饰器就是负责把一个方法变成属性调用的


class Student2():

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    # score有读写权限
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer!')
        if score < 0 or score > 100:
            raise ValueError('score must be range 0 to 100')
        else:
            self.__score = score

    # 只有读权限
    @property
    def name(self):
        return self.__name


s2 = Student2('yao', 87)
print(s2.score)
s2.score = 100
print(s2.score)
# s2.name = 'ou'




























