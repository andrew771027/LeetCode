from src.array.lc_118_pascals_triangle import Solution


def test_zero_line_case():
    assert Solution().generate(0) == []


def test_one_line_case():
    assert Solution().generate(1) == [[1]]


def test_normal_case():
    assert Solution().generate(5) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
    ]
