#similar to jump game 3 but we just  have to decide the maximum range upto which we can jump
#and its based on the largest value of the forbidden arr
#and not with the x
#and also some modifications to the visited array to prevent any infinite loops
class Solution:
    def minimumJumps(self, f: List[int], a: int, b: int, x: int) -> int:
        if x==0:
            return 0
        
        N = (a + b + max(x,max(f)))
        
        visited = set([(0,True)])
        f = set(f)
        
        que = deque([(0,True)])
        
        jump = 0
        
        while que:
            jump += 1
            # print(jump,que)
            for q in range(len(que)):
                node,flag = que.popleft()
                state = (node,flag)
                front = node + a
                back = node - b

                if 0<=front<=N and front not in f and (front,True) not in visited:
                    if front == x:
                        return jump
                    visited.add((front,True))
                    que.append([front,True])                
                if 0<=back<=N and back not in f and (back,False) not in visited  and flag:
                    if back == x:
                        return jump
                    visited.add((back,False))
                    que.append([back,False])
        
        return -1