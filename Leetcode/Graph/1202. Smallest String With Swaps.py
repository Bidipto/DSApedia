# 1202. Smallest String With Swaps
#after a lot of thinking and time speant getting to the perfect solution 
# lesson = goblal variable is better then return a list in dfs
from collections import defaultdict
class Solution:
    
    def dfs(self,i):
        self.visited[i] = True
        self.component.append(i)
        self.char.append(self.s[i])
        for j in self.adj[i]:
            if not self.visited[j]:
                self.dfs(j)
    
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.s = s
        N = len(s)
        self.adj = [[] for i in range(N)]
        
        #adj list 
        for i,j in pairs:
            self.adj[i].append(j)
            self.adj[j].append(i)


        self.visited = [False] * len(s)
        s = list(s)
        
        
        #dfs for connected components and also sorting
        #iniatially made different looops for dfs and sorting but than that was expensive and gave tle
        for i in range(N): 
            if not self.visited[i]:
                #also using global variable to store the connected components 
                # and the characters in the connected components, initailly returned but wad very expensive
                self.char = []
                self.component = []
                self.dfs(i)
                #sorting the idices and the characters
                self.component.sort()
                self.char.sort()
                # placing at the right place
                for k in range(len(self.component)):
                    s[self.component[k]] = self.char[k]
        
        return ''.join(s)