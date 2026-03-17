from src.string.lc_125_valid_palindrome import Solution


def test_normal_case_1():
    assert Solution().isPalindrome(s="A man, a plan, a canal: Panama")


def test_normal_case_2():
    assert not Solution().isPalindrome(s="race a car")


def test_nomral_case_3():
    assert Solution().isPalindrome(s=" ")
