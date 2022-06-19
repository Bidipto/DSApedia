# 131. Palindrome Partitioning
# we build palindrome with the remaining length of the sting 
# and pass the left over stack to the next recursive call 
# and we add that partitioning to the res array when s is exhausted
def partition(self, s: str) -> List[List[str]]:
    res = []
    
    def magic(s,curr):
        if not s:
            res.append(curr)
            return
            
        for i in range(1, len(s)+1):
            temp = s[:i]
            if temp == temp[::-1]:
                magic(s[i:], curr + [temp])
    
    magic(s,[])
    return res
        