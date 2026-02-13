import pytest

from src.array.lc_001_two_sum import Solution


def test_normal_case_1():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_normal_case_2():
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]


def test_duplicate_numbers():
    assert Solution().twoSum([3, 3], 6) == [0, 1]


def test_negative_numbers():
    assert Solution().twoSum([-1, -2, -3, -4], -6) == [1, 3]


def test_no_solution():
    with pytest.raises(ValueError):
        Solution().twoSum([1, 2, 3], 10)
