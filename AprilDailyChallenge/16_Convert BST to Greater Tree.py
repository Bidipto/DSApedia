# 538. Convert BST to Greater Tree
#using a global variable
def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    self.pathsum = 0
    def magic(root):
        if not root: return
        
        magic(root.right)
        self.pathsum += root.val
        root.val = self.pathsum
        magic(root.left)
        
    magic(root)
    return root