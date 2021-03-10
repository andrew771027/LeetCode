import pytest
from .TreeNodeModule import ConvertListToBinaryTree
from .Balanced_Binary_Tree.balanced_binary_tree import Solution

@pytest.mark.parametrize(("param" ,"expected_result"),
                        [
                            (ConvertListToBinaryTree([3,9,20,None,None,15,7]), True)
                        ])
def test_balanced_binary_tree(param, expected_result):

    test = Solution()
    assert test.isBalanced(root=param) == expected_result