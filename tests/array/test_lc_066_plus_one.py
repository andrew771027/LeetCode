from src.array.lc_066_plus_one import Solution


def test_normal_case_1():
    assert Solution().plusOne([1, 2, 3]) == [1, 2, 4]


def test_normal_case_2():
    assert Solution().plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]


def test_normal_case_3():
    assert Solution().plusOne([9]) == [1, 0]


def test_normal_case_4():
    assert Solution().plusOne([9, 9]) == [1, 0, 0]
