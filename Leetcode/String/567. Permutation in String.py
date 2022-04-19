# 567. Permutation in String
def checkInclusion(self, p: str, s: str) -> bool:
    P = Counter(p)
    S = Counter(s[:len(p)])
    for i in range(len(p), len(s)):
        if S == P:
            return True
        ele = s[i]
        S[ele] += 1
        first = i -len(p)
        S[s[first]] -= 1
        
    return S == P