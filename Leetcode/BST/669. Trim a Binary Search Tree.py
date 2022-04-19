#kafi important concept and basics clear kore onek 

def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
    def magic(root):
        #base_case 
        if not root:
            return None
        
        #when the value of root node is less then low,we ignore the root 
        #and its left subtree
        if root.val<low:
            return magic(root.right)
        
        #and lly when its higher we ignore the right
        if root.val>high:
            return magic(root.left)
        
        #when its between the low and high we perform magic on right
        #and left Bsts of the root
        root.right = magic(root.right)
        root.left = magic(root.left)
        
        return root
    return magic(root)