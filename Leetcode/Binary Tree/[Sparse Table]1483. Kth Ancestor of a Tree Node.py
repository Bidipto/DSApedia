#used next level debugger in me lol 
#wanted to give up but didn't
#great question tbh 
class TreeAncestor:

    def __init__(self, N: int, parent: List[int]):
        #we use the size as 16 as 2 power 16 is 65,536 which is closest to the constraints
        size = 16
        #sparce table or binary lifting 
        #st[m][n]
        #m -> 2^m th ancestor of the node 
        #n -> node
        st = [[-1]*N for i in range(size+1)]
        # print(st)
        for i in range(N):
            st[0][i] = parent[i]
            
        for m in range(1,size+1):
            for n in range(N):
                #2^m-1th parent
                #binaary lifting and implementation of vanilla sparse tree
                par = st[m-1][n]
                if par != -1:
                    st[m][n] = st[m-1][par]
        
        self.st = st 
        self.size = size 
        self.power = {}
        for i in range(size + 1):
            self.power[i] = pow(2,i)
            
        # print(self.st)
    def getKthAncestor(self, node: int, n: int) -> int:
        par = node
        # for m in range(self.size+1):
        #     print(self.st[m][49736],self.st[m][node],m)
        for i in range(self.size, -1, -1):
            # print(self.power[i])
            if n>=self.power[i]:
                n-=self.power[i]
                node = self.st[i][node]
                if node == -1:
                    return -1
            # print(node,n,i)
        # print(node)
        return node

