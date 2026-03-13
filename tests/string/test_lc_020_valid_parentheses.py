from src.string.lc_020_valid_parentheses import Solution


def test_normal_case_1():
    assert Solution().isValid("()") is True


def test_normal_case_2():
    assert Solution().isValid("()[]{}") is True


def test_normal_case_3():
    assert Solution().isValid("([])") is True


def test_failure_case_1():
    assert not Solution().isValid("(]")


def test_failure_case_2():
    assert not Solution().isValid("([)]")
