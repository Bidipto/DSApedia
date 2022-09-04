def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return None
    if root == p or root == q:
        return root
    
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    
    if right and left:
        return root
    elif left:
        return left
    elif right:
        return right

def lca(self,root, n1, n2):
    self.res = None 
    
    def magic(root):
        if not root:
            return False 
        
        left = magic(root.left)
        right = magic(root.right)
        
        # print(left,right,root.data)
        
        if root.data == n1 or root.data == n2:
            if left or right:
                self.res = root
            return True
                
        if left and right:
            self.res = root 
            return True
                
        if left or right:
            return True
        
        return False 
        
    magic(root)
    return self.res