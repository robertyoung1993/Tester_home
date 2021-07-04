

class Student():
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    def watch_video(self):
        if self.age < 18:
            print('%s只能观看<<熊出没>>.' % self.name)
        else:
            print('%s正在观看不可描述的片子' % self.name)

def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('yangyang', 25)
    # 给对象发study消息
    stu1.study('测试之道')
    # 给对象发送watch_video消息
    stu1.watch_video()

    # 新创建对象stu2
    stu2 = Student('mingming', 15)
    stu2.study('music')
    stu2.watch_video()

if __name__ == '__main__':
    main()