#Dp for trees, kafi easy to come up with with a patient mind, lel 
def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
    dp = {}
    dp[1] = [TreeNode(0)]
    
    if not n%2: return []
    
    def magic(i):
        if i in dp: 
            return dp[i]
        
        temp = []
        for j in range(1,i,2):
            left = magic(j)
            right = magic(i-j-1)
            
            for l,r in product(left,right):
                temp.append(TreeNode(0,l,r))
                
        dp[i] = temp
        return dp[i]
    
    return magic(n)
            