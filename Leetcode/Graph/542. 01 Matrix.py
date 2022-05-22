# 542. 01 Matrix
def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #multisource bfs
        M = len(mat)
        N = len(mat[0])
        
        seen = set()
        que = deque()
        
        for i,j in product(range(M),range(N)):
            if mat[i][j] == 0:
                que.append((i,j))
        
        level = -1
        while que:
            level += 1
            for i in range(len(que)):
                i,j = que.popleft()
                if (i,j) in seen:
                    continue
                mat[i][j]=level
                seen.add((i,j))
                
                for m,n in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                    if 0<=m<M and 0<=n<N and (m,n) not in seen:
                        que.append((m,n))
                        
        return mat