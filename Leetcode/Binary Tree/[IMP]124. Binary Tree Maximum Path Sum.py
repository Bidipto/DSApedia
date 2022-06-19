# 124. Binary Tree Maximum Path Sum

#from every node we give the max path sum through that node
#note that we might have negatives to tackle with 

def maxPathSum(self, root: Optional[TreeNode]) -> int:
    res = [-math.inf]
    
    def magic(node):
        if not node:
            return 0
        #dealing with negative path sum 
        rightSum = max(0, magic(node.right))
        leftSum = max(0, magic(node.left))
        
        # print(rightSum, leftSum, node.val)
        
        res[0] = max(res[0],rightSum + node.val + leftSum)
        
        return max(rightSum, leftSum) + node.val
    
    magic(root)
    return res[0]