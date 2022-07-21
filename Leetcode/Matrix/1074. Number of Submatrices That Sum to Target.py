# 1074. Number of Submatrices That Sum to Target

def numSubmatrixSumTarget(self, mat: List[List[int]], target: int) -> int:
        #first we make a running sum of of all the rows 
        M = len(mat)
        N = len(mat[0])
        
        for i in range(1,N):
            for j in range(M):
                mat[j][i] += mat[j][i-1]
                
        res = 0
        
        #then from every range in colums we add the rows and check like the question 
        # subset sum equal to k
        for i in range(N):
            for j in range(i,N):
                d = Counter()
                d[0] = 1
                tempsum = 0
                
                for row in range(M):
                    if i == 0:
                        tempsum += mat[row][j]
                    else:
                        tempsum += mat[row][j] - mat[row][i-1]
                        
                    res += d[tempsum - target]
                    d[tempsum] += 1
                    
        return res