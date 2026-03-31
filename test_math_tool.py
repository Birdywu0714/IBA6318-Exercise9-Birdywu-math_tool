# test_math_tool.py
from math_tool import add_numbers, multiply_numbers

def test_add():
    # 测试 10 + 5 是否等于 15
    assert add_numbers(10, 5) == 15

def test_multiply():
    # 测试 3 * 4 是否等于 12
    assert multiply_numbers(3, 4) == 12