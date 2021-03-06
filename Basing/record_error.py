"""
记录错误
内置logging模块可以非常容易的记录错误信息
"""

import logging


# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#
# main()
# print('END')

"""
抛出错误
"""
class FooError(ValueError):
    pass

def fooo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s ' % s)
    return 10 / n

def bar():
    try:
        fooo('0')
    except ValueError as e:
        print('ValueError!')
        raise
bar()

# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型
