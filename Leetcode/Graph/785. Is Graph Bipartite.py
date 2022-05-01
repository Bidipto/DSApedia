#colouring the graph
def isBipartite(self, graph: List[List[int]]) -> bool:
    colours = {}
    def magic(root):
        for i in graph[root]:
            if i in colours:
                #if two adjacent nodes are of same colour it cant be bipartite 
                if colours[i] == colours[root]:
                    return False
            else:
                #assign opposite colours to adjecent nodes 
                colours[i] = -colours[root]
                if not magic(i):
                    return False
        return True
                
    for i in range(len(graph)):
        if i not in colours:
            colours[i] = 1
            if not magic(i):
                return False
            
    return True