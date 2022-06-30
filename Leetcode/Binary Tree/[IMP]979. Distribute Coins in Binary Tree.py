# 979. Distribute Coins in Binary Tree

def distributeCoins(self, root: Optional[TreeNode]) -> int:
    self.magic = 0
    # for each ndoe we return a transaction 
    # if we need coins it will be negative 
    # if we give coins it will be positive
    def magic(root):
        if not root: return 0
    
        leftTransaction = magic(root.left)
        rightTransaction = magic(root.right)
        
        self.magic += abs(leftTransaction) + abs(rightTransaction)
        return leftTransaction + rightTransaction + root.val - 1 
    
    magic(root)
    return self.magic