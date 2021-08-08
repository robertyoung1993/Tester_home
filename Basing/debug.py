"""
调试
"""

# print


# 断言 assert

# def  foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n
# 
# def main():
#     foo('0')
#
# main()

# logging 和assert相比，logging不会抛出错误，而且可以输出到文件

import logging

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

