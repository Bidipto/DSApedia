#a very very better approach
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

    
#my very naive approach where is check for the left and right subtree of a root node
def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
    dummy = TreeNode
    dummy.right = root
    dummy.left = None
    pre = dummy
    def magic(root):
        if root.right:
            right = root.right
            if right.val>high:
                if right.left:
                    root.right = right.left
                    magic(root)
                else:
                    root.right = None
            elif right.val<low:
                if right.right:
                    root.right = right.right
                    magic(root)
                else:
                    root.right = None
            magic(right)
        if root.left:
            left = root.left
            if left.val>high:
                if left.left:
                    root.left = left.left
                    magic(root)
                else:
                    root.left = None
            elif left.val<low:
                if left.right:
                    root.left = left.right
                    magic(root)
                else:
                    root.left = None
            magic(left)
    magic(pre)
    return dummy.right