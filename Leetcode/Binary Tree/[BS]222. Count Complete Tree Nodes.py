#in a complete binary tree the nodes are always added in the highest depth from left to right 
#we need to find the branch at which there is a difference between the right height and the left height  
def countNodes(self, root: Optional[TreeNode]) -> int:
    self.count = 0
    
    def magic(root):
        if not root: return 0
        
        leftDepth = depth(root.left)
        rightDepth = depth(root.right)
        
        if leftDepth == rightDepth:
            return pow(2,leftDepth) + magic(root.right)
        else:
            return pow(2,rightDepth) + magic(root.left)
    
    def depth(node):
        if not node: return 0
        return 1 + depth(node.left)
    return magic(root)