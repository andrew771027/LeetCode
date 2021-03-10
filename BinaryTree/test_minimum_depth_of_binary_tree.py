import pytest
from .TreeNodeModule import ConvertListToBinaryTree
from .Minumum_Depth_Of_Binary_Tree.minimum_depth_of_binary_tree import Solution

@pytest.mark.parametrize(("param", "expected_result"),
                        [
                            (ConvertListToBinaryTree([3,9,20,None,None,15,7]), 2)
                        ]
)
def test_minimum_depth_binary_tree(param, expected_result):
    
    test = Solution()
    assert test.minDepth(param) == expected_result