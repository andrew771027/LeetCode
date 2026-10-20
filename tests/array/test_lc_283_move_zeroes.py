import pytest

from src.array.lc_283_move_zeroes import Solution


@pytest.mark.parametrize(
    ("nums, expected"),
    [
        pytest.param(
            [0, 1, 0, 3, 12],
            [1, 3, 12, 0, 0],
            id="leetcode-example",
        ),
        pytest.param(
            [0],
            [0],
            id="single-zero",
        ),
        pytest.param(
            [1, 2, 3],
            [1, 2, 3],
            id="no-zero",
        ),
        pytest.param(
            [0, 0, 0],
            [0, 0, 0],
            id="all-zero",
        ),
        pytest.param(
            [0, 0, 1, 2],
            [1, 2, 0, 0],
            id="leading-zeros",
        ),
        pytest.param(
            [1, 2, 0, 0],
            [1, 2, 0, 0],
            id="trailing-zeros",
        ),
        pytest.param(
            [],
            [],
            id="empty-array",
        ),
        pytest.param(
            [0, -1, 0, -3, 2],
            [-1, -3, 2, 0, 0],
            id="negative-values",
        ),
    ],
)
def test_move_zeroes(
    nums: list[int],
    expected: list[int],
):
    original_id = id(nums)

    result = Solution().moveZeroes(nums)

    assert result is None
    assert nums == expected
    assert id(nums) == original_id
