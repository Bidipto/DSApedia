# 76. Minimum Window Substring
def minWindow(self, s: str, t: str) -> str:
    res = ""
    T = Counter(t)
    S = Counter(s[:len(t)-1])
    right = len(t) - 1
    left = 0
    res = ""
    temp = math.inf
    
    #and 111 reason why i love counter 
    while right<len(s):
        S[s[right]] += 1
        right += 1
        
        while not T - S:
            if right - left < temp:
                temp = right - left
                res = s[left:right]
            S[s[left]] -= 1
            left += 1
                
    return res