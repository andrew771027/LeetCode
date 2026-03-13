from hypothesis import given
from hypothesis import strategies as st

from src.string.lc_013_roman_to_integer import Solution


def int_to_roman(num: int) -> str:
    val = [1000, 500, 100, 50, 10, 5, 1]
    syms = ["M", "D", "C", "L", "X", "V", "I"]

    roman = ""
    i = 0

    while num > 0:
        for _ in range(num // val[i]):
            roman += syms[i]
            num -= val[i]
        i += 1

    return roman


def test_normal_case_1():
    assert Solution().romanToInt("III") == 3


def test_normal_case_2():
    assert Solution().romanToInt("LVIII") == 58


def test_normal_case_3():
    assert Solution().romanToInt("MCMXCIV") == 1994


@given(st.integers(min_value=1, max_value=1999))
def test_hypothesis_case(number):
    """
    用hypohesis產生隨機的測試案例
    """
    roman = int_to_roman(number)
    assert Solution().romanToInt(roman) == number
