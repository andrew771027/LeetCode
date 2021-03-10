import pytest
from .TreeNodeModule import ConvertListToBinaryTree
from .Maximum_Depth_Of_Binary_Tree.maximum_depth_of_binary_tree import Solution

@pytest.mark.parametrize(("param" ,"expected_result"),
                        [
                            (ConvertListToBinaryTree([3,9,20,None,None,15,7]), 3)
                        ])
def test_maximum_depth_binary_tree(param, expected_result):

    test = Solution()
    assert test.maxDepth(root=param) == expected_result