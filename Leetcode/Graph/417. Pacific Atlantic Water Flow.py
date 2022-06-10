#need to figure out a better solution 
class Solution:
    def pacificAtlantic(self, arr: List[List[int]]) -> List[List[int]]:
        M = len(arr)
        N = len(arr[0])
        ans = []

        dpp = [[-1 for i in range(N)] for j in range(M)]
        dpa = [[-1 for i in range(N)] for j in range(M)]

        pathp = set()
        patha = set()

        def pacific(m, n, dpp):
            if m == 0 or n == 0:
                dpp[m][n] = 1
                return 1

            if dpp[m][n] == 1:
                return dpp[m][n]

            res = 0
            pathp.add((m,n))
            for i,j in [[0,1],[1,0],[-1,0],[0,-1]]:
                if m+i >= 0 and n+j >= 0 and m+i < M and n+j < N: 
                    if arr[m][n]>=arr[m+i][n+j]:
                        if (m+i,n+j) not in pathp:
                            res = max(res,pacific(m+i,n+j,dpp))
            pathp.remove((m,n))
            dpp[m][n] = res
            return dpp[m][n]

        def atlantic(m, n, dpa):
            if m == M -1 or n == N-1:
                dpa[m][n] = 1
                return 1

            if dpa[m][n] == 1:
                return dpa[m][n]

            res = 0
            patha.add((m,n))
            for i,j in [[0,1],[1,0],[-1,0],[0,-1]]:
                if 0 <= m+i < M and 0 <= n+j < N : 
                    if arr[m][n]>=arr[m+i][n+j]:
                        if (m+i,n+j) not in patha:
                            res = max(res,atlantic(m+i,n+j,dpa))
            patha.remove((m,n))
            dpa[m][n] = res
            return dpa[m][n]

        for i in range(M):
            for j in range(N):
                if atlantic(i,j,dpa) == 1 and pacific(i,j,dpp) == 1:
                    ans.append([i,j]) 

        #print(pathp, patha)
        #print(dpp, dpa)
        return ans