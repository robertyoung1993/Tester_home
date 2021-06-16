"""
============================
Author: Allen
Time:2021/06/13
============================
"""

# 序列的操作

# 不可变型
# 数字、字符串、元组
# 类型特定的方法
S = "Spam"
S.find('pa')   # 1
S.replace('pa', 'XYZ')   # SXYZm

# 通过分隔符将字符串拆分为子字符串，大小写变换，测试字符串的内容，去掉字符串前后空格
line = 'aaa,bbb,ccccc,dd'
line.split(',')      # ['aaa', 'bbb', 'ccccc', 'dd']

print(dir(S))
# dir将会返一个列袭，其中包含了对象的所有属性
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
# '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize',
# 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map',
# 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
# 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
# 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
# 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


