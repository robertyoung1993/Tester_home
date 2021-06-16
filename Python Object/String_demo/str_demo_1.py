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

