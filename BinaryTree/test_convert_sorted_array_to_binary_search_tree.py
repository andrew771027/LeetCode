import pytest
from .TreeNodeModule import TreeNode
from .Convert_Sorted_Array_To_Binary_Search_Tree.convert_sorted_array_to_binary_search_tree import Solution

@pytest.mark.parametrize(("param"),
                        [
                            ([3,9,20,None,None,15,7])
                        ])
def test_converted_sorted_array_to_binary_search_tree(param):
    test = Solution()
    test.sortedArrayToBST(param)