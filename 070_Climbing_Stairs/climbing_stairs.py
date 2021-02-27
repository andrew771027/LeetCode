import pytest

class Solution:

    def climbStairs_recursive(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        elif n == 2:
            return 2
        
        else:
            return self.climbStairs_recursive(n-2) + self.climbStairs_recursive(n-1)

    def climbStairs_interative(self, n: int) -> int:

        if n == 1:
            return 1

        if n == 2:
            return 2
        
        result = 0
        prev = 1
        current = 2

        for index in range(2, n):

            result = prev + current
            prev = current
            current = result
        
        return result



@pytest.mark.parametrize(("parma", "expected_result"),
                         [
                             (1 ,1),
                             (2, 2),
                             (3, 3),
                             (4, 5),
                             (5, 8),
                             (6, 13)
                         ]
)
def test_climbStairs_recursive(parma, expected_result):

    test = Solution()
    assert test.climbStairs_recursive(parma) == expected_result



@pytest.mark.parametrize(("parma", "expected_result"),
                         [
                             (1 ,1),
                             (2, 2),
                             (3, 3),
                             (4, 5),
                             (5, 8),
                             (6, 13)
                         ]
)
def test_climbStairs_interative(parma, expected_result):

    test = Solution()
    assert test.climbStairs_interative(parma) == expected_result