# 437. Path Sum III
#better solutions with cacheing 
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = [0]
        def magic(root):
            if not root:
                return 
            
            minimagic(root,targetSum)
            magic(root.left)
            magic(root.right)
            
        
        def minimagic(root,target):
            if not root:
                return 
            elif target == root.val:
                res[0] += 1
            
            minimagic(root.right,target - root.val)
            minimagic(root.left,target - root.val)
            
        magic(root)
        return res[0]