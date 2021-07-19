"""
生成器
列表生成式可以直接创建一个列表，但是受到内存的限制，列表容量有限
创建百万个元素的列表不仅占用很大的存储空间，如果仅仅访问前面几个元素，
那后面绝大多数元素占用的空间都白白浪费了
"""

# 1
# g = (x for x in range(10))
# print(g)
#
# for n in g:
#     print(n)

def fib(n):
    a, b = 0, 1
    for i in range(n):
        # print(b, end=' ')
        yield b
        a, b = b, a+b
    return 'done'

for i in fib(6):
    print(i)
