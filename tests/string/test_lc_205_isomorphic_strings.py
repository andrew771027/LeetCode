from src.string.lc_205_isomorphic_strings import Solution


def test_normal_case_1():
    assert Solution().isIsomorphic(s="egg", t="add")


def test_normal_case_2():
    assert not Solution().isIsomorphic(s="f11", t="b23")


def test_normal_case_3():
    assert Solution().isIsomorphic(s="paper", t="title")


def test_normal_case_4():
    assert not Solution().isIsomorphic(s="egg", t="title")
