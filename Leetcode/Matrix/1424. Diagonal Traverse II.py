# 1424. Diagonal Traverse II
# did a got solution but caused TLE 
# need to get a habit for looking into the conStraints 
def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        M = len(nums)
        N = max({len(arr) for arr in nums})
        
        temp = []
        res = []
        
        for i, arr in enumerate(nums):
            for j, ele in enumerate(arr):
                t = (i+j,-i,ele)
                temp.append(t)
                
        for summ, row, ele in sorted(temp):
            res.append(ele)
            
        return res