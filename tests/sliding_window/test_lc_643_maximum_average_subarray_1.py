import pytest

from src.sliding_window.lc_643_maximum_average_subarray_1 import Solution
from hypothesis import given, strategies as st

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
    #允許10^-5的浮點數誤差
    assert actual == pytest.approx(expected, abs=1e-5)


def find_max_average_oracle(
    nums: list[int],
    k: int,
) -> float:
    
    return max(
        sum(nums[i:i + k]) / k
        for i in range(len(nums) - k + 1)
        )

@st.composite
def valid_inputs(draw):
    nums = draw(
        st.lists(
            st.integers(min_value=-100, max_value=100),
            min_size=1,
            max_size=30,
        )
    )

    k = draw(
        st.integers(
            min_value=1,
            max_value=len(nums),
        )
    )

    return nums, k

@given(data=valid_inputs())
def test_find_max_average_property(data):
    nums, k = data

    actual = Solution().findMaxAverage(nums, k)
    expected = find_max_average_oracle(nums, k)

    assert actual == pytest.approx(expected, abs=1e-5)