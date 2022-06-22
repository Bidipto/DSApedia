# kafi hard hard question, wont be able to code it up during a interview or oa without hints or even with hints 
# 2127. Maximum Employees to Be Invited to a Meeting
def maximumInvitations(self, fav: List[int]) -> int:
        #there cound be to types ways to invite the max number of employees
        #one: a cycle 
        #two: all cycles of length 2 with longest chain attached to the,
        #we are supposed to return the max of both 
        
        #in 2nd case to find the longest chain we have to make a reversed adj list, and 
        #do a bfs on the nodes 
        
        #step1 : make the reversed adj list 
        #step2 : search for the cycles in the graph
        #step3 : if the len of the cycle is more then 2 its case 1
        #step4 : if the len of the cucle is equal to 2 its case 2, call the chain func
        #         return the longest chains on both the nodes 
        #step5 : return the max of both the cases
        
        N = len(fav)
        adj = {i:set() for i in range(N)}
        
        for person,f in enumerate(fav):
            adj[f].add(person)
        # print(adj) 
        #search for the chains, since its not necessary that all the 
        #node a join ie there might be more then one strongly connected componentes
        cycleLen = 0
        chainLen = 0
        for curr in range(N):
            # print(fav)
            if fav[curr] != -1:
                dic = {curr:0}
                while fav[curr] != -1:
                    nxt = fav[curr]
                    fav[curr] = -1
                    #cycle encounterd 
                    if nxt in dic:
                        lenOfChain = len(dic)-dic[nxt]
                        if lenOfChain == 2:
                            chainLen += 2 + self.bfs(curr,{curr,nxt},adj) + self.bfs(nxt,{curr,nxt},adj)
                        else:
                            cycleLen = max(cycleLen, lenOfChain)
                    dic[nxt]=len(dic)
                    curr = nxt
        # print(cycleLen, chainLen)
        return max(cycleLen, chainLen)
            
            
def bfs(self, start, seen, adj):
    maxx = 0
    que = deque([(start, 0)])
    
    while que:
        u,level = que.popleft()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                que.append([v, level + 1])
                maxx = max(maxx, level + 1)
    # print(start,maxx)
    return maxx