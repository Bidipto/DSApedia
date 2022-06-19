# 105. Construct Binary Tree from Preorder and Inorder Traversal
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dummy = TreeNode(9999)
        
        def magic(preorder,inorder):
            # print(preorder,inorder)
            if not preorder:
                return 
            
            rootVal = preorder[0]
            index = inorder.index(rootVal)
            
            left = index
            right = len(inorder)-index-1
            
            node = TreeNode(rootVal)
            #inorder meh root ke right meh sab right tree ka roots ha aur left meh left ka
            #preorder meh root sabse pehle hota ha fir left nodes fir right nodes
            #threfore we take the root value from preorder and find the number of
            #nodes from the nodes that lie in left and right of root in inorder
            node.left = magic(preorder[1:1+left],inorder[:index])
            node.right = magic(preorder[1+left:],inorder[index+1:])
            
            return node
            
            
        
        dummy.right = magic(preorder, inorder)
        return dummy.right
# 106. Construct Binary Tree from Inorder and Postorder Traversal
def buildTreeIntoPost(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dummy = TreeNode(9999)
        
        def magic(preorder,inorder):
            # print(preorder,inorder)
            if not preorder:
                return 
            
            rootVal = preorder[-1]
            index = inorder.index(rootVal)
            
            left = index
            right = len(inorder)-index-1
            
            node = TreeNode(rootVal)
            #inorder meh root ke right meh sab right tree ka roots ha aur left meh left ka
            #preorder meh root sabse pehle hota ha fir left nodes fir right nodes
            #therefore we take the root value from preorder and find the number of
            #nodes from the nodes that lie in left and right of root in inorder
            node.left = magic(preorder[:left],inorder[:index])
            node.right = magic(preorder[left:len(inorder)-1],inorder[index+1:])
            
            return node
            
            
        
        dummy.right = magic(postorder, inorder)
        return dummy.right