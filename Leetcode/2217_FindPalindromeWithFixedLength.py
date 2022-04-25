# 2217. Find Palindrome With Fixed Length
#good observation
#need to works on thinking about edge cases
#just calculated the ith number of half of the length of the req palindrome
#baki last meh bass copy kar diya ha
def kthPalindrome(self, queries: List[int], L: int) -> List[int]:
    half = L//2 + L%2
    base = pow(10,half-1) - 1
    limit = pow(10,half)
    res = []
    for i in queries:
        if base + i >=limit:
            res.append(-1)
            continue
        halfpal = base + i
        temp = halfpal
        
        #odd
        if L%2:
            temp = temp//10
        while temp:
            halfpal = (halfpal *10) + temp%10
            temp = temp//10
        
        res.append(halfpal)
            
    return res