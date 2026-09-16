from src.array.lc_026_remove_duplicates_from_sorted_array import Solution


def test_normal_case_1():
    assert Solution().removeDuplicates([1, 1, 2]) == 2


def test_normal_case_2():
    assert Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5


def test_empty_case():
    assert Solution().removeDuplicates([]) == 0


def test_compacted_prefix():
    for values, expected in [
        ([], []),
        ([1, 1, 2], [1, 2]),
        ([2, 2, 2], [2]),
        ([1, 2, 3], [1, 2, 3]),
    ]:
        k = Solution().removeDuplicates(values)
        assert k == len(expected)
        assert values[:k] == expected
