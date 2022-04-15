# 113. Path Sum II
#return the list of paths from root to leaf with path sum equal to target
def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
    res = []
    def magic(root,target,curr):
        if not root:
            return
        #if its a leaf node and the target is equal to root value 
        #ie makes a path
        #then we append the current path to the list and return 
        elif not root.right and not root.left and target == root.val:
            res.append(curr + [root.val])
            return 
            # print(root.val,target)
        
        right = magic(root.right,target - root.val,curr + [root.val])
        left = magic(root.left,target - root.val,curr + [root.val])
        
    magic(root,target,[])
    return res