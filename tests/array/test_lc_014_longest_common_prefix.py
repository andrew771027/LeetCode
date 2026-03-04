from src.array.lc_014_longest_common_prefix import Solution


def test_normal_case():
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"


def test_invalid_case():
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
