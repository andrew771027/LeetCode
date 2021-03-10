import pytest
from .TreeNodeModule import ConvertListToBinaryTree
from .Symmetric_Tree.symmetric_tree import Solution

@pytest.mark.parametrize(("param", "expected_result"),
                        [
                            (ConvertListToBinaryTree([1,2,2,3,4,4,3]), True),
                            (ConvertListToBinaryTree([[1,2,2,None,3,None,3]]), True)
                        ]
)
def test_symmetric_tree(param, expected_result):
    
    test = Solution()
    assert test.isSymmetric(param) == expected_result