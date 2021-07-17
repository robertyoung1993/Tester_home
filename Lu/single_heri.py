"""
单继承
"""

class Animal:
    """动物类"""
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s正在吃食物" % self.name)

    def play(self):
        print("%s正在玩" % self.name)

    def sleep(self):
        print("%s正在休息" % self.name)

class Dog(Animal):
    """狗类"""
    def __init__(self, name):
        super().__init__(name)
        print("这是一只%s" % self.name)

    def eat(self):
        print("%s正在吃狗粮" % self.name)

    def bark(self):
        print("%s会汪汪叫" % self.name)

dog = Dog("哈士奇")
dog.eat()
dog.play()
dog.bark()


