class Solution:
    def isSymmetric(self, root) -> bool:
        
        return self.isMirror(root, root)

    def isMirror(self, root1, root2):

        if root1 is None and root2 is None:
            return True
        
        if root1 != None and root2 != None:
            
            if root1.val == root2.val:

                return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)
        
        return False


        

         

        