"""
切片
"""
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取L的前三个

# 1
lst1 = []
for i in range(3):
    lst1.append(L[i])
print(lst1)

# 2
q = L[:3]
print(q)