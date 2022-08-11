# 2359. Find Closest Node to Given Two Nodes
# moral: question acche se padho yarrrrrrrrrrrrrrrrrrrrrrrrrrrrr

class Solution:
    def closestMeetingNode(self, adj: List[int], node1: int, node2: int) -> int:
        def magic(node):
            queue = collections.deque()
            queue.append(node)
            dis = 0
            
            while queue:
                for q in range(len(queue)):
                    node = queue.popleft()

                    if node in seen:
                        return 
                    
                    seen[node] = dis
                    
                    if adj[node] != -1:
                        queue.append(adj[node])

                    dis += 1
                    
        def magic2(node):
            queue = collections.deque()
            queue.append(node)
            dis = 0
            
            while queue:
                for q in range(len(queue)):
                    node = queue.popleft()

                    if node in seen2:
                        return 
                    
                    seen2[node] = dis
                    
                    if adj[node] != -1:
                        queue.append(adj[node])

                    dis += 1
        
        seen = {}
        
        magic(node1)
        
        seen2 = {}
        
        magic2(node2)
        
        dis = math.inf 
        res = -1
        
        # print(seen)
        # print(seen2)
        
        for i in range(len(adj)):
            if i in seen and i in seen2:
                if max(seen[i],seen2[i])<dis:
                    dis = max(seen[i],seen2[i])
                    res = i
                    
        return res
        