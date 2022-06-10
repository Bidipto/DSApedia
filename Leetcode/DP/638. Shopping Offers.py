# 638. Shopping Offers
# each offer made is a state for this dp approach 
def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        N = len(price)
        dic = {}
        
        def magic(curr):
            if tuple(curr) in dic:
                return dic[tuple(curr)]
            
            if max(curr) == 0:
                return 0
            
            val = sum([curr[i]*price[i] for i in range(N)])
            
            for spe in special:
                temp = [curr[i]-spe[i] for i in range(N)]
                if min(temp)<0:
                    continue
                val = min(val,magic(temp)+spe[-1])
            
            dic[tuple(curr)] = val
            return val
        
        return magic(needs)