# 399. Evaluate Division
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.adj = defaultdict(list)
        #builfing a adj list of the graph with the given ratios and the opposite direction using the 
        #the inverse of the ratio
        for se,value in zip(equations, values):
            start = se[0]
            end = se[1]
            reverse = pow(value,-1)
            self.adj[start].append((end,value))
            self.adj[end].append((start,reverse))
            
        res = []
        
        for start, end in queries:
            self.end = end
            self.visited = set([start])
            res.append(self.magic(start,1.0))
        
        return res
    
    #we just have to return the path multiplication of the path
    def magic(self, start, prob):
        #if it doesnt exist we return a -1
        if start not in self.adj:
            return -1.0
        
        if start == self.end:
            return prob
        
        temp = -1.0
        for nxt, nxtprob in self.adj[start]:
             if nxt not in self.visited:
                self.visited.add(nxt)
                temp = max(self.magic(nxt, nxtprob*prob), temp)
        
        return temp
        