def canCross(self, stones: List[int]) -> bool:
        #a very good dp problem
        #we use visited to not to go the the same stone agaun 
        visited = set()
        arr = set(stones)
        last = stones[-1]
        flag = [False] 
        # print(last)
        def magic(i,k):
            if flag[0]:
                return 
            # print(i,k,i==last)
            if i == last:
                flag[0] = True
                return 
            
            if (i,k) in visited:
                return 
            
            visited.add((i,k))
            
            for newJump in range (max(1,k-1),k+2):
                if i + newJump in arr:
                    # print(newJump)
                    magic(i+newJump,newJump)
                    
            
        if stones[1]-1 != stones[0]:
            return False 
        
        magic(stones[1],1)
        return flag[0]