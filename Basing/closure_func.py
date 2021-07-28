"""
闭包：
1、内部函数可以引用外部函数的参数和局部变量
2、返回一个函数
3、嵌套一个函数
"""
def count():
    fs = []
    for i in range(1, 5):
        def f():
            return i * i
        fs.append(f)
    return fs

for func in count():
    print(func())
