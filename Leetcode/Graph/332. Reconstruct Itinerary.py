# 332. Reconstruct Itinerary

def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #simple backtracking on graph with some brainstroming
        tickets.sort()
        
        adj = collections.defaultdict(list)
        
        for u,v in tickets:
            adj[u].append(v)
            
        res = ["JFK"]
        
        edgesLen = len(tickets)
        
        def magic(node):#
            #when we have all nodes visited we know we have the answer 
            if len(res)-1 == edgesLen:
                return True
            #we reach a end before visiting all the paths 
            if node not in adj:
                return False 
            
            tempList = adj[node]
            
            for i,child in enumerate(tempList):
                adj[node].pop(i)
                res.append(child)
                
                if magic(child): return True
                
                adj[node].insert(i,child)
                res.pop()
                
            return False
        
        magic("JFK")
        
        return res