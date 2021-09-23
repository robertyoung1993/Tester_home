"""
pytest_demo3
"""
import pytest


# 捕获异常，在测试过程中，经常需要测试是否如期抛出预期的异常，以确定异常处理模块生效。
# 在pytest中使用pytest.raise()捕获异常

def test_raises():
    with pytest.raises(TypeError) as e:
        abs('2')
    exec_msg = e.value.args[0]
    assert exec_msg == "bad operand type for abs(): 'str'"
