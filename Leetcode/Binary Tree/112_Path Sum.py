# 112. Path Sum
def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
    #base case
    if not root:
        return False
    #if its a leaf node and target is equal to the value
    elif not root.right and not root.left and target == root.val:
        return True
    
    # print(root.val,target)
    right = self.hasPathSum(root.right,target - root.val)
    left = self.hasPathSum(root.left,target - root.val)
    
    #if there is a path through the root either right ot left will return true
    return right or left