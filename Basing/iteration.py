"""
给定一个list or tuple, 可以使用for循环来遍历这个list or tuple，这种遍历称为迭代
"""

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for key in d:
#     print(key)
#
# for value in d.values():
#     print(value)

for key, value in d.items():
    print(key, value)

for i, value in enumerate(['a', 'b', 'c', 'd']):
    print(i, value)