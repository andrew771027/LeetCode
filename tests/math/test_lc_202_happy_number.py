import pytest
from hypothesis import given
from hypothesis import strategies as st

from src.math.lc_202_happy_number import Solution


@pytest.mark.parametrize(
    "n, expected",
    [
        pytest.param(
            19,
            True,
            id="leetcode-example-happy",
        ),
        pytest.param(
            2,
            False,
            id="leetcode-example-unhappy",
        ),
        pytest.param(
            1,
            True,
            id="single-one",
        ),
        pytest.param(
            7,
            True,
            id="happy-seven",
        ),
        pytest.param(
            10,
            True,
            id="happy-ten",
        ),
        pytest.param(
            100,
            True,
            id="happy-hundred",
        ),
        pytest.param(
            4,
            False,
            id="unhappy-cycle-entry",
        ),
        pytest.param(
            20,
            False,
            id="unhappy-twenty",
        ),
        pytest.param(
            82,
            True,
            id="intermdeiate-happy-value",
        ),
        pytest.param(
            999,
            False,
            id="large-unhappy-number",
        ),
    ],
)
def test_is_happy(n: int, expected: bool) -> None:
    actual = Solution().isHappy(n)

    assert actual is expected


@given(
    n=st.integers(
        min_value=1,
        max_value=2**31 - 1,
    )
)
def test_is_happy_property(n: int) -> None:
    actual = Solution().isHappy(n)
    expected = Solution().is_happy_oracle(n)

    assert actual == expected
