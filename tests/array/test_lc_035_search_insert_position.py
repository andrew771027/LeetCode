from src.array.lc_035_search_insert_position import Solution


def test_normal_case():
    assert Solution().searchInsert([1, 3, 5, 6], 5) == 2


def test_invalid_case_1():
    assert Solution().searchInsert([1, 3, 5, 6], 2) == 1


def test_invalid_case_2():
    assert Solution().searchInsert([1, 3, 5, 6], 7) == 4
