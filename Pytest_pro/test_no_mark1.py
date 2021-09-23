"""
pytest_demo5
"""

import pytest
#
# 1、标记测试函数
#     由于某种原因（test_func2）的功能尚未开发完成，我们只想执行指定的测试函数，以下有几种方法可以解决

def test_func1():
    assert 1 == 1

def test_func2():
    assert 1 != 1
# 1、显式指定函数名，通过::标记
# 只想执行函数test_func1     pytest test_no_mark1.py::test_func1

# 2、使用模糊匹配，使用 -k选项标识
# pytest -k func1 test_no_mark1.py

# 以上两种方法，第一种一次只能指定一个测试函数，当要进行批量测试时无能为力；
# 第二种方法可以批量操作，但需要所有测试的函数名包含相同的模式，也不方便。

# 3、使用 pytest.mark 在函数上进行标记
# 标记的测试函数如：pytest -m finished test_no_mark1.py

@pytest.mark.finished
def test_func3():
    assert 1 == 1

@pytest.mark.unfinished
def test_func4():
    assert 1 != 1