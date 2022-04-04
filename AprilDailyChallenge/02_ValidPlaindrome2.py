class Solution:
    def validPalindrome(self, s: str) -> bool:
        flag = False
        lo = 0
        hi = len(s) -1
        while hi>lo:
            if s[lo] == s[hi]:
                lo += 1
                hi -= 1
            else:
                return self.valid(s,lo+1,hi) or self.valid(s,lo,hi-1)
        return True
    
    def valid(self,s,lo,hi):
        while hi>lo:
            if s[lo] == s[hi]:
                lo += 1
                hi -= 1
            else:
                return False
        return True