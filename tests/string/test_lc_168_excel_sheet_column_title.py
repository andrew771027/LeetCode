from src.string.lc_168_excel_sheet_column_title import Solution


def test_normal_case_1():
    assert Solution().convertToTitle(columnNumber=1) == "A"


def test_nomral_case_2():
    assert Solution().convertToTitle(columnNumber=28) == "AB"


def test_normal_case_3():
    assert Solution().convertToTitle(columnNumber=701) == "ZY"
