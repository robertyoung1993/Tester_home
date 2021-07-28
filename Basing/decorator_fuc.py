"""
装饰器
"""
# def now():
#     print('Today!')
#
# f = now
# f()

# 拿到函数的名字
# print(now.__name__)

# def log(func):
#     def wrapper(*args, **kwargs):
#         print('call %s():' % func.__name__)
#         return func(*args, **kwargs)
#     return wrapper
#
# @log
# def now():
#     print("Today!!!")
#
# now()

# now = log(now)

# 如果装饰器本身需要传入参数，那就需要编写一个返回装饰器的高阶函数
def log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log('execute')
def now():
    print("Tormorow!!!")

now()

# now = log('execute')(now)

























