# 1293. Shortest Path in a Grid with Obstacles Elimination

# bfs my friend

def shortestPath(self, grid: List[List[int]], K: int) -> int:
    M = len(grid)
    N = len(grid[0])
    
    seen = set()
    
    queue = collections.deque()
    queue.append([0,0,0])
    count = 0
    
    while queue:
        # print(count,queue)
        for q in range(len(queue)):
            x,y,k = queue.popleft()
            
            if x == M-1 and y == N-1:
                print(k)
                return count 
            
            if (x,y,k) in seen:
                continue
                
            seen.add((x,y,k))
            
            for m,n in (x+1,y),(x,y+1),(x-1,y),(x,y-1):
                if 0<=m<M and 0<=n<N:
                    if grid[m][n] == 1 and (m,n,k+1) not in seen and k<K :
                        queue.append((m,n,k+1))
                    elif grid[m][n] == 0 and (m,n,k) not in seen:
                        queue.append((m,n,k))
        count += 1
    return -1