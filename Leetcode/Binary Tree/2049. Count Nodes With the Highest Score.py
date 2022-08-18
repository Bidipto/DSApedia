def countHighestScoreNodes(self, parents: List[int]) -> int:
    N = len(parents)
    self.res = 0
    self.score = 0 
    
    adj = collections.defaultdict(list)
    
    for i,val in enumerate(parents):
        adj[val].append(i)
        
    # print(adj)
    
    def magic(node):
        if node not in adj:
            if self.score == N-1:
                self.res += 1
            elif self.score < N-1:
                self.score = N-1 
                self.res = 1
            # print(node,N-1)
            return 1
        
        if len(adj[node]) == 1:
            rightChild = magic(adj[node][0])
            score = rightChild*max(1,(N-rightChild-1))
            if self.score == score:
                self.res += 1
            elif self.score < score:
                self.score = score
                self.res = 1
            # print(node,score)
            return 1 + rightChild 
        
        else:
            rightChild = magic(adj[node][0])
            leftChild = magic(adj[node][1])
            score = rightChild*leftChild*max(1,(N-rightChild-leftChild-1))
            if self.score == score:
                self.res += 1
            elif self.score < score:
                self.score = score
                self.res = 1
            # print(node,score)
            return 1 + rightChild + leftChild 
        
    magic(0)
    # print(self.score)
    return self.res