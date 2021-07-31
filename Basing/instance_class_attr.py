"""
实例属性和类属性
给实例绑定属性的方法是通过实例变量，或者通过self变量
"""

class Student():

    class_name = 'Student'

    def __init__(self, name):
        self.name = name

# 定义了一个类属性后，这个属性虽然归类所有，但是类的所有实例都可以访问到

s = Student('Bob')
s.score = 90
print(s.name, s.score)
print(dir(s))
print(s.class_name)
print(s.name)
print(Student.class_name)
del s.name
print(s.class_name)



