import pytest

from itertools import combinations
from hypothesis import given, strategies as st
from src.array.lc_594_longest_harmonious_subsequence import Solution



@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param(
            [1, 3, 3, 2, 5, 2, 3, 7],
            5,
            id="leetcode-example",
        ),
        pytest.param(
            [1, 2, 3, 4],
            2,
            id="consecutive-values",
        ),
        pytest.param(
            [1, 1, 1, 1],
            0,
            id="all-identical",
        ),
        pytest.param(
            [1, 3, 5, 7],
            0,
            id="no-harmonious-pair",
        ),
        pytest.param(
            [1, 2, 2, 1],
            4,
            id="all-elements-valid",
        ),
        pytest.param(
            [-2, -1, -1, 0],
            3,
            id="negative-values",
        ),
        pytest.param(
            [5],
            0,
            id="single-element",
        ),
        pytest.param(
            [],
            0,
            id="empty-array",
        ),

    ]
)
def test_find_lhs(
    nums: list[int],
    expected: int,
) -> None:

    actual = Solution().findLHS(nums)
    assert actual == expected

def find_lhs_oracle(nums: list[int]) -> int:
    best = 0

    for size in range(2, len(nums) + 1):
        for subsequence in combinations(nums, size):
            if max(subsequence) - min(subsequence) == 1:
                best = max(best, size)

    return best

@given(
    nums=st.lists(
        st.integers(min_value=-10, max_value=10),
        min_size=0,
        max_size=10,
    )
)
def test_find_lhs_property(nums: list[int]) -> None:
    actual = Solution().findLHS(nums)
    expected = find_lhs_oracle(nums)

    assert actual == expected