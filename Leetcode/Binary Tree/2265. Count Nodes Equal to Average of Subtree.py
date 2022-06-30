# 2265. Count Nodes Equal to Average of Subtree

def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
    self.count = 0
    
    def magic(root):
        if not root: return 0,0
        
        leftTotal, leftNode = magic(root.left)
        rightTotal, rightNode = magic(root.right)
        
        Total = leftTotal + rightTotal + root.val
        Node =  leftNode + rightNode + 1
        
        if math.floor(Total/Node) == root.val:
            self.count += 1
        # print(Total, Node, root.val, self.count)
        return Total, Node
    
    magic(root)
    return self.count