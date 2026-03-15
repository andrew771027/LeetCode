from src.string.lc_058_length_of_last_word import Solution


def test_normal_case_1():
    assert Solution().lengthOfLastWord(s="Hello World") == 5


def test_normal_case_2():
    assert Solution().lengthOfLastWord(s="   fly me   to   the moon  ") == 4


def test_normal_case_3():
    assert Solution().lengthOfLastWord(s="luffy is still joyboy") == 6


def test_normal_case_4():
    assert Solution().lengthOfLastWord(s="") == 0
