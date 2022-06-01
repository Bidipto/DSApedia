# 663 · Walls and Gates
# https://leetcode.com/problems/walls-and-gates/
# we need to get the distance rooms to gate 
# bfs is the first and last thought
from collections import deque
class Solution:
    def walls_and_gates(self, rooms: List[List[int]]):
        M = len(rooms)
        N = len(rooms[0])
        visited = set()
        queue = deque()
        for i in range(M):
            for j in range(N):
                if rooms[i][j] == -1:
                    visited.add((i,j))
                elif rooms[i][j] == 0:
                    visited.add((i,j))
                    queue.append((i,j))

        counter = 0
        while queue:
            counter += 1
            for q in range(len(queue)):
                m,n = queue.popleft()
                for i,j in (m+1,n),(m,n+1),(m-1,n),(m,n-1):
                    if 0<=i<M and 0<=j<N and (i,j) not in visited:
                        rooms[i][j] = counter 
                        queue.append((i,j))
                        visited.add((i,j))