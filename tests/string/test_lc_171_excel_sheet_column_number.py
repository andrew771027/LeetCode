from src.string.lc_171_excel_sheet_column_number import Solution


def test_normal_case_1():
    assert Solution().titleToNumber(columnTitle="A") == 1


def test_normal_case_2():
    assert Solution().titleToNumber(columnTitle="AB") == 28


def test_normal_case_3():
    assert Solution().titleToNumber(columnTitle="ZY") == 701
