import pytest

from src.array.lc_643_maximum_average_subarray_1 import Solution

@pytest.mark.parametrize(
    "nums, k, expected",
    [
        pytest.param(
            [1 ,12, -5 ,-6, 50 ,3], 
            4, 
            12.75000, 
            id="leetcode-example",
        ),
        pytest.param(   
            [5],
            1,
            5.0000,
            id="single-element",
        ),
        pytest.param(
            [1 ,2, 3, 4],
            4,
            2.5,
            id="window-equals-array",
        ),
        pytest.param(
            [10, 1, 1, 1, 10],
            2,
            5.5,
            id="multiple-max-windows",
        ),
        pytest.param(
            [1, 2, 3, 4, 5],
            1,
            5.0,
            id="window-size-one",
        ),
    ]
)
def test_find_max_average(nums: list[int], k: int, expected: float,) -> None:
    actual = Solution().findMaxAverage(nums, k)
    assert actual == expected