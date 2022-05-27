# 847. Shortest Path Visiting All Nodes
# typical dp where we use a mask to maintain the visited nodes  
def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)
        cache = {}
        end = (1<<N)-1
        
        
        def magic(node, mask):
            state = (node, mask)
            #when all the nodes are visited ie only one 1 in mask
            #all simply mask is a power of 2
            #mask = 00100 mask-1 = 00011 
            #fore, mask & mask-1 = 0
            if mask & (mask-1) == 0:
                return 0
            #caching 
            if state in cache:
                return cache[state]
            
            #to avoid infinite loops we put a inf value to cache
            cache[state] = math.inf
            
            for neighbour in graph[node]:
                #checking if neighbour is visited
                #if there is a 0 in neighbour th  place 
                #it will give a zero, let nei = 3
                # 11110 & 00100 = 00100 (unvisited)
                # 11010 & 00100 = 0(visited)
                if mask & (1<<neighbour):
                    # 1 xor 1 = 0 and 0 xor 1 = 1
                    #here we need to convert 1 to 0 to make node visited
                    #therfore if node =3
                    #11000 xor 01000 = 10000
                    take = magic(neighbour,mask^(1<<node)) + 1
                    nottake = magic(neighbour,mask) + 1
                    cache[state] = min(cache[state],take,nottake)
                    
            return cache[state]
        
        
        res = math.inf
        for i in range(N):
            res = min(res, magic(i,end))
    
        return res