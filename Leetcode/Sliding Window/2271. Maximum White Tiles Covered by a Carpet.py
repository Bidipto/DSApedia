from collections import deque
#we sort hr list given to us first and then keep then in a deque
#and try for laying the carpet from the end
#something i had a hard time understanding was that the in the range both i and j were inclusive
def maximumWhiteTiles(self, arr: List[List[int]], L: int) -> int:
        arr.sort()
        start = max(arr[0][0]-L,0)
        res = min(L,arr[0][1] - arr[0][0]+1)
        temp = res 
        que = deque([arr[0]])
        for s,e in arr[1:]:
            # print(que,res,temp)
            while que and que[0][1]<=start:
                i,j = que.popleft()
                temp -= (j-i+1)
                # print(que,temp)
            if que and que[0][0]<start:
                res = max(res,temp-(start-que[0][0]+1))
            else:
                res = max(res,temp)
            que.append((s,e))
            temp += (e-s+1)
            start = max(e-L,0)
            # print(que,start)
        #check last case 
        while que and que[0][1]<=start:
                # print(que[0][1],start)
                i,j = que.popleft()
                temp -= (j-i+1)
        if que and que[0][0]<start:
            # print(start,que[0][0],start-que[0][0]+1)
            res = max(res,temp-(start-que[0][0]+1))
        else:
            res = max(res,temp)

        return res