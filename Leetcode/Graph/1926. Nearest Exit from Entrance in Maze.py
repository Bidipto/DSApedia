# 1926. Nearest Exit from Entrance in Maze

def nearestExit(self, mat: List[List[str]], entrance: List[int]) -> int:
        #singlesource bfs
        M = len(mat)
        N = len(mat[0])
        
        seen = set()
        que = deque()
        que.append([entrance[0],entrance[1]])
        
        level = 0
        while que:
            # print(que,level)
            level += 1
            for i in range(len(que)):
                i,j = que.popleft()
                if (i,j) in seen:
                    continue
                seen.add((i,j))
                
                for m,n in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                    if 0<=m<M and 0<=n<N and (m,n) not in seen and mat[m][n] == ".":
                        if m==M-1 or m==0 or n==N-1 or n==0:
                            return level
                        que.append((m,n))
                        
        return -1