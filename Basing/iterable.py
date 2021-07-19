"""
迭代器
可以直接作用于for循环的数据类型有以下几种
1、集合数据类型：list、tuple、dict、set、str
2、一类是生成器，包括生成器和生成器函数（带yield的函数）
"""

# 可以使用isinstance()判断一个对象是否是Iterable对象

from collections.abc import Iterable
from collections.abc import Iterator

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance((), Iterable))
print(isinstance('abc', Iterable))

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器
print(isinstance((x for x in range(10)), Iterator))

def fib(n):
    a, b = 0, 1
    for i in range(n):
        # print(b, end=' ')
        yield b
        a, b = b, a+b
    return 'done'

print(isinstance(fib(6), Iterator))

# 生成器都是Iterator对象，但是Iterable不一定是Iterator
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))