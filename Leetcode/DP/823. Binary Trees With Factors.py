# 823. Binary Trees With Factors
# made a factor list where all factor pairs of a number are stored 
# and then calculated the number of binary trees that can be formed with them 


def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = pow(10,9)+7
        N = len(arr)
        arr.sort(reverse = True)
        dic = collections.defaultdict(list)
        
        for i in range(N):
            val = arr[i]
            # dic[val] = []
            lo = i 
            hi = N - 1
            while lo<=hi:
                mul = arr[lo] * arr[hi]
                if mul == val:
                    dic[val].append([arr[lo],arr[hi]])
                    lo += 1
                    hi -= 1
                elif mul>val:
                    lo += 1
                else:
                    hi -= 1
        # print(dic)          
        res = 0
        
        @cache
        def magic(i):
            res = 1
            
            for f1,f2 in dic[i]:
                if f1 != f2:
                    res += (2*(magic(f1) * magic(f2)))%mod
                else:
                    res += ((magic(f1) * magic(f2))%mod)
                # print(res)
                
            return res
        
        for i in arr:
            res += (magic(i)%mod)
        
        return res%mod