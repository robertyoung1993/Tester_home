"""
pytest_demo1
"""

# 第一个测试函数
# 测试成功
def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


# 命令行运行 pytest test1.py

# pytest使用.标识测试成功(passed)
# 小的技巧
# 使用-v选项，显示测试的详细信息
# 使用pytest -h 查看pytest的所有选项

