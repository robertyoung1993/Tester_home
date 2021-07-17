"""
多继承
"""

class Food:
    """食物类"""

    def __init__(self, name):
        print("%s是食物" % name)

class Vegetables(Food):
    """蔬菜类"""

    def __init__(self, Vname):
        print("%s是蔬菜" % Vname)
        super().__init__(Vname)

class Fruit(Food):
    """水果类"""

    def __init__(self, Fname):
        print("%s是水果" % Fname)
        super(Fruit, self).__init__(Fname)

class Tomato(Fruit, Vegetables):
    """西红柿类"""

    def __init__(self, Tname):
        print("西红柿既是蔬菜又是水果")
        super(Tomato, self).__init__(Tname)

print(Tomato.__mro__)

tomato = Tomato("西红柿")