"""
高阶函数：既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
map/reduce/filter/sorted
"""

# map()接收两个参数，一个是函数，一个Iterable, map将传入的函数一次作用序列的每个元素，并把结果作为新的Iterator返回
# def f(x):
#     return x ** 2
#
# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(r))
#
# print(list(map(str, [1, 2, 3, 4 ,5, 6, 7, 8, 9])))
#
# # reduce把一个函数作用在一个序列上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个做累积计算
#
# from functools import reduce
#
# def add(x, y):
#     return x + y
#
# print(reduce(add, [1, 3, 5 ,7 ,9]))

# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 3, 4 ,5, 6, 7, 8, 9 ])))

# 把一个序列中的空字符串删掉
def not_empty(s):
    return  s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '   '])))


# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序

print(sorted([36, 5, -12, 9, -21], key=abs))














