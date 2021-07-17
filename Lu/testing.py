# def main():
#     scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
#     # 通过键可以获取字典中对应的值
#     print(scores['骆昊'])
#     print(scores['狄仁杰'])
#     # 对字典进行遍历(遍历的其实是键再通过键取对应的值)
#     for elem in scores:
#         #print(elem)
#         print('%s\t--->\t%d' % (elem, scores[elem]))
#     for key, value in scores.items():
#         print(key, value)
#     # 更新字典中的元素
#     scores['白元芳'] = 65
#     scores['诸葛王朗'] = 71
#     scores.update(冷面=67, 方启鹤=85)
#     print(scores)
#     if '武则天' in scores:
#         print(scores['武则天'])
#     print(scores.get('武则天'))
#     # get方法也是通过键获取对应的值但是可以设置默认值
#     print(scores.get('武则天', 60))
#     # 删除字典中的元素
#     print(scores.popitem())
#     print(scores.popitem())
#     print(scores.pop('骆昊', 100))
#     # 清空字典
#     scores.clear()
#     print(scores)
#
#
# if __name__ == '__main__':
#     main()

# def f(x, y):
#     return x * y
#
# func = lambda x,y:x * y
#
# print(f(2, 3), func(2, 3))
# import logging
#
# def use_logging(func):
#     def wrapper(*args, **kwargs):
#         logging.warning("%s is running" % func.__name__)
#         print("%s is running" % func.__name__)
#         return func(*args, **kwargs)
#     return wrapper

# def bar():
#     print('i am bar')
#
#
# bar = use_logging(bar)
# print(bar)
# bar()

# @use_logging
# def foo():
#     print('i am foo')
#
# @use_logging
# def bar():
#     print('i am bar')
#
#
# foo()
# bar()

class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

if __name__ == '__main__':
    b = B()

