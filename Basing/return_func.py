"""
函数作为返回值
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
"""

# 函数的求和，不想得到求和的结果，之前拿到求和的函数

def lazzy_sum(*args):
    def sum():
        s = 0
        for n in args:
            s += n
        return s
    return sum

print(lazzy_sum(1, 3, 5, 7, 9))