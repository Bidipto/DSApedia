# 667. Beautiful Arrangement II
def constructArray(self, n: int, k: int) -> List[int]:
        #using the property of wiggle/zigzag
        res = list()
        
        lo = 1
        hi = k + 1
        
        while lo<=hi:
            res.append(hi)
            hi -= 1
            #for odd cases
            if hi!=lo-1:
                res.append(lo)
                lo += 1
        res.reverse()
        res += [int(i) for i in range(k+2,n+1)]
        return res