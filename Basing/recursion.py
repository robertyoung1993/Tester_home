"""
递归：一个函数可以在内部调用自身本身，这个函数就是递归函数
优点：定义简单，逻辑清晰
缺点：需要注意防止栈溢出
函数调用通过栈这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈，函数返回就会减一层栈
解决办法：通过尾递归优化
尾递归是指在函数返回的时候就调用自身本身，并且return语句不能包含表达式
"""

# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)

# print(fact(5))

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, prod):
    if num == 1:
        return prod
    return fact_iter(num-1, num * prod)

print(fact(5))




