from src.string.lc_028_find_the_index_of_the_first_occurance_in_a_string import Solution


def test_normal_case_1():
    assert Solution().strStr(haystack="sadbutsad", needle="sad") == 0


def test_normal_case_2():
    assert Solution().strStr(haystack="leetcode", needle="leeto") == -1
