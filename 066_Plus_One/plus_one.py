import pytest

class Solution:

    def plusOne(self, digits :list) -> list:
        
        num = 0
        result = []

        for index in range(len(digits)):

            num = num + digits[index] * 10 ** (len(digits) - (index + 1))
        
        num = num + 1

        for index in range(len(str(num))):

            result.append(int(str(num)[index]))

        return result


@pytest.mark.parametrize(("param", "expected_result") , [
    ([1, 2, 3], [1, 2, 4]),
    ([4, 3, 2, 1], [4, 3, 2, 2]),
    ([0], [1])
])
def test_plus_one(param, expected_result):

    test = Solution()
    assert test.plusOne(param) == expected_result
