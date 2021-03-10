class Solution:

    def isBalanced(self, root) -> bool:

        if not root:
            return True

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        if abs(left - right) < 2:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

    def maxDepth(self, root) -> int:

        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left , right) + 1

