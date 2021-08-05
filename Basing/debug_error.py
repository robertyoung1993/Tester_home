"""
错误、调试和测试
"""

# try

# try:
#     print('try...')
#     # r = 10 / 0
#     r = 10 / 5
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END!')


# 捕获多种错误，发生不同类型的错误，应该由不同的except语句块处理
# try:
#     print('try...')
#     r = 10 / int('2')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:     # 没有错误的发生，可以在except语句快后加一个else，当没有错误发生时，会自动执行else语句
#     print('no error')
# finally:
#     print('finally...')
# print('END!')

# python的错误其实也是class,所有的错误类型都继承自BaseException,所以在使用except时需要注意的是，
# 他不但要捕获该类型的错误，还要把其子类也一网打尽

# def foo():
#     pass
#
#
# # 第二个except永远也捕获不到UnicodeError,因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了
# try:
#     foo()
# except ValueError as e:
#     print('ValueError')
# except UnicodeError as e:
#     print('UnicodeError')

# 使用try...except捕获错误还有一个好处，就是可以跨越多层调用，比喻函数main()调用bar(),bar()调用foo().，结果foo()出错了，
# 这时只要main()捕获到了，就可以处理

def fop(s):
    return 10 / int(s)

def bar(s):
    return fop(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

main()








































