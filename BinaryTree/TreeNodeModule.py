import pytest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)

def ConvertListToBinaryTree(data_list: list) -> TreeNode:
    
    if not data_list:
        return None 
    
    index = 0
    root = TreeNode(data_list[index])
    return InsertLevelOrder(data_list=data_list,
                            root=root,
                            index=index)

def InsertLevelOrder(data_list, root, index) -> TreeNode:

    if index < len(data_list):

        if data_list[index]: 

            root = TreeNode(data_list[index]) 

            root.left = InsertLevelOrder(data_list=data_list, 
                                        root=root, 
                                        index=2 * index + 1
                                        )

            root.right = InsertLevelOrder(data_list=data_list,
                                        root=root,
                                        index=2 * index + 2
                                        )
            return root

def Inorder_Traverse(root: TreeNode):

    if root.val != None :
        
        Inorder_Traverse(root=root.left)
        print(f"Value: {root.val}")
        Inorder_Traverse(root.right)

    

@pytest.mark.parametrize(("param"),
                        [
                            ([3,9,20,None,None,15,7])
                        ])
def test_create_binary_tree(param):

    # arr = [1, 2, 3, 4, 5, 6, 6, 6, 6] 
    root = None
    root = ConvertListToBinaryTree(data_list=param)
    # Inorder_Traverse(root=root) 