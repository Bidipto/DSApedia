#classic backtracking problem silimlar to purmutaions in leetcode
def find_permutation(self, S):
    N = len(S)
    res = []
    def magic(s,curr):
        if not s:
            res.append(curr)
            return
        
        for i in range(len(s)):
            magic(s[:i] + s[i+1:],curr + s[i])
    
    magic(S,"")
    return sorted(res)