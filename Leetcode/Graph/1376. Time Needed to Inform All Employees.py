# 1376. Time Needed to Inform All Employees
from collections import defaultdict,deque
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        #adj list with with manager -> employee
        adj = defaultdict(list)
        for i,val in enumerate(manager):
            adj[val].append(i)
            
        # print(adj)
        que = deque([(headID,0)])
        res = 0
        
        #simple bfs with track of maximum time
        while que:
            for q in range(len(que)):
                head,time = que.popleft()
                res = max(res,time)
                
                for employee in adj[head]:
                    que.append((employee,time+informTime[head]))
        
        return res