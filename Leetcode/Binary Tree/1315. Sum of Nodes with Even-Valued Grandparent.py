def sumEvenGrandparent(self, root: TreeNode) -> int:
    # we pass the parents and grandparents as a state, and for every node with even grandparent 
    # we add the value of the node to the sum
    self.magic = 0
    def magic(node,parent,grandparent):
        if not node: return 
        
        if not grandparent%2:
            self.magic += node.val
            
        magic(node.right,node.val,parent)
        magic(node.left,node.val,parent)
    
    magic(root,-1,-1)
    return self.magic