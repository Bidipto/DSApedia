# 95. Unique Binary Search Trees II

def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
    dp = {}
    def magic(start, end):
        #base_case for return
        if start>end:
            return [None]
        
        if (start, end) in dp:
            return dp[(start,end)]
        
        res = []
        #making every val in the range [start, end] a root 
        for i in range(start, end + 1):
            #the leftbst of the root will be given by the values less than the 
            #current value of the root
            leftbst = magic(start,i-1)
            #lly the right by values greater
            rightbst = magic(i+1,end)
            for l in leftbst:
                for r in rightbst:
                    root = TreeNode(i,l,r)
        
                    res.append(root)
            # print(leftbst, rightbst, res, start, end, i)
        dp[(start, end)] = res
        return dp[(start, end)]
    return magic(1,n)