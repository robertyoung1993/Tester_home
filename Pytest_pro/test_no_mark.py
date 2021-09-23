"""
pytest_demo4
"""

# pytest的查找测试策略
# 默认情况下，pytest会递归查找当前目录下所有以test开始或者结尾的python脚本
# 并执行文件内所有以test开始或结束的函数方法

def test_func1():
    assert 1 == 1

def test_func2():
    assert 1 != 1

