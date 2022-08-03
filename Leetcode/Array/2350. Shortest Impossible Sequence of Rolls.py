def shortestSequence(self, rolls: List[int], k: int) -> int:
        #we calculate the number of subset that have all the elements 
        #the answer will be one more that
        s = set()
        res = 0
        for i in rolls:
            s.add(i)
            if len(s) == k:
                res += 1
                s = set()
        return res + 1 