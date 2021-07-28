"""
匿名函数:lambda
"""
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

a = lambda x:x ** 2
for i in range(3):
    print(a(i))