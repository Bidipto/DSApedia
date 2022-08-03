# 1504. Count Submatrices With All Ones

def numSubmat(self, mat: List[List[int]]) -> int:
        #can be further optimization 
        M = len(mat)
        N = len(mat[0])
        arr = [[0 for i in range(N)] for j in range(M)]
        
        for m in range(M):
            for n in range(N):
                if mat[m][n] == 1:
                    if m == 0:
                        arr[m][n] = 1
                    else:
                        arr[m][n] = arr[m-1][n] + 1
                else:
                    arr[m][n] = 0
        
        res = 0
        
        for m in range(M):
            # print(m)
            for j in range(1,N+1):
                for i in range(j):
                    # print(arr[m][i:j])
                    res += min(arr[m][i:j])
        
        return res
                