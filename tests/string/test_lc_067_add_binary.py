from src.string.lc_067_add_binary import Solution


def test_normal_case_1():
    assert Solution().addBinary(a="11", b="1") == "100"


def test_normal_case_2():
    assert Solution().addBinary(a="1010", b="1011") == "10101"
