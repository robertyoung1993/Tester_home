'''
继承与多态
'''

class Person():
    '''人'''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play(self):
        print('%s正在愉快的玩耍.' % self.name)

    def watch_av(self):
        if self.age >= 18:
            print("%s正在观看不可描述的片子" % self.name)
        else:
            print("%s只能观看<熊出没>" % self.name)
class Student(Person):
    '''
    学生
    '''

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def study(self, course):
        print("%s的%s正在学习%s." % (self.grade, self.name, course))
class Teacher(Person):
    """
    老师
    """
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title

    def teach(self, course):
        print("%s%s正在讲%s." % (self.name, self.title, course))

def main():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_av()
    t = Teacher('罗通', 36, '副教授')
    t.teach('java')
    t.watch_av()

if __name__ == '__main__':
    main()


