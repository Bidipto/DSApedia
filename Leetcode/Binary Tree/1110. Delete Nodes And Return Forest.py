def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    delete = set(to_delete)
    res = []
    def magic(root, prev, side):
        if not root:
                return 
            
        if root.val in delete:
            if prev:
                if side:
                    prev.left = None 
                else:
                    prev.right = None 
            
            if root.left and root.left.val not in delete:
                res.append(root.left)
            if root.right and root.right.val not in delete:
                res.append(root.right)
            
        magic(root.left,root,True)
        magic(root.right,root,False)

        
    if root and root.val not in delete:
        res.append(root)
    
    magic(root,None,True)
    return res