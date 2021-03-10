class Solution:

    def minDepth(self, root) -> int:

        if not root:
            return 0

        if root.left == None and root.right == None:
            return 1

        elif not root.left:
            return self.minDepth(root.right) + 1
        
        elif not root.right:
            return self.minDepth(root.left) + 1

        else:
            return min (self.minDepth(root.left), self.minDepth(root.right)) + 1