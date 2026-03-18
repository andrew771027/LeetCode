from src.string.lc_242_valid_anagram import Solution


def test_normal_case_1():
    assert Solution().isAnagram(s="anagram", t="nagaram")


def test_normal_case_2():
    assert not Solution().isAnagram(s="rat", t="car")


def test_normal_case_3():
    assert not Solution().isAnagram(s="anagram", t="car")
