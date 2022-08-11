def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    def magic(node,val):
        if not node:
            return None 
        # print(node.val, val)
        if node.val == val:
            if not node.left and not node.right:
                return None
            #case 1 no left child (also tackels the case of no children)
            if not node.left:
                return node.right 
            #case 2 no right child 
            if not node.right:
                return node.left 
            
            #case 3 has both right and left child 
            #the replacement will be the left of node of the right subtree 
            #or similarly the right most child of the left subtree 
            if node.right and node.left:
                temp = node.right 

                while temp.left:
                    temp = temp.left

                node.val = temp.val 
                node.right = magic(node.right,node.val)

            
        elif node.val>val:
            node.left = magic(node.left,val)
        else:
            node.right = magic(node.right,val)
            
        return node
    
    return magic(root,key)