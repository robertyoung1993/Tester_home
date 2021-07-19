"""
列表生成式
"""

import os

# 1
print(list(range(1, 11)))

# 2
l = [x  for x in range(1, 11)]
print(l)

# 3
l1 = [x ** 2  for x in range(1, 11) if x % 2 == 0]
print(l1)

# 4
l2 = [m + n for m in 'ABC' for n in 'XYZ']
print(l2)

# 5
l3 = [d for d in os.listdir('.')]
print(l3)

# 6
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
l4 = [k + '=' + str(v) for k, v in d.items()]
print(l4)