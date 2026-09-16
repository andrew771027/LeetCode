from src.array.lc_027_remove_element import Solution


def test_normal_case_1():
    assert Solution().removeElement([3, 2, 2, 3], 3) == 2


def test_normal_case_2():
    assert Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5


def test_retained_prefix():
    for values, val, expected in [
        ([], 3, []),
        ([3, 2, 2, 3], 3, [2, 2]),
        ([3, 3], 3, []),
        ([1, 2], 3, [1, 2]),
    ]:
        k = Solution().removeElement(values, val)
        assert k == len(expected)
        assert sorted(values[:k]) == sorted(expected)
