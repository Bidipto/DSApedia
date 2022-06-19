def isValidBST(self, root: Optional[TreeNode],minn = -math.inf, maxx = math.inf) -> bool:
    if not root:
        return True

    if root.val>=maxx or root.val<=minn:
        return False
    # in the left branch, root is the new ceiling; 
    #  contrarily root is the new floor in right branch
    return self.isValidBST(root.left,minn,root.val) and self.isValidBST(root.right,root.val,maxx)
