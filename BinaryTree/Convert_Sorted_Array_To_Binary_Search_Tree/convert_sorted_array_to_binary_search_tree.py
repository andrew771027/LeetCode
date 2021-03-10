# from ..TreeNodeModule import TreeNode

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)

class Solution:

    def sortedArrayToBST(self, nums):

        if len(nums) == 0:
            return None
        
        left = 0
        right = len(nums)-1

        return self.dfs(nums, left, right)

    def dfs(self, nums, left, right):
        
        if left > right:
            return None

        middle = (left + right) // 2

        root = TreeNode(nums[middle])
        root.left = self.dfs(nums, left, middle-1)
        root.right = self.dfs(nums, middle+1, right)

        return root
