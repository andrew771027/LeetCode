from src.array.lc_136_single_number import Solution


def test_normal_case_1():
    assert Solution().singleNumber([2, 2, 1]) == 1


def test_normal_case_2():
    assert Solution().singleNumber([4, 1, 2, 1, 2]) == 4


def test_normal_case_3():
    assert Solution().singleNumber([1]) == 1
