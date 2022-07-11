def maxProduct(self, root: Optional[TreeNode]) -> int:
    mod = pow(10,9) + 7
    self.sum = 0
    def summ(node):
        if not node: return 
        
        # self.sum %= mod
        self.sum += node.val
        
        summ(node.left)
        summ(node.right)
        
    summ(root)
    # print(self.sum)
    self.max = 0

    def magic(node):
        if not node: return 0
        
        left = magic(node.left)
        
        right = magic(node.right)
        
        # print(left, right, node.val)
        self.max = max(self.max,(left * (self.sum - left)),(right * (self.sum - right)))
        
        return (left + right + node.val)

    magic(root)
    return self.max%mod