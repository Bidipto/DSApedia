class Solution:
    def longestPalin(self, s):
        def magic(lo,hi):
            # print(lo)
            while lo>=0 and hi<len(s) and s[lo] == s[hi]:
                # print(s[lo:hi+1])
                if self.res<len(s[lo:hi+1]):
                    self.res = len(s[lo:hi+1])
                    self.ans = s[lo:hi+1]
                lo -= 1
                hi += 1
                # print(lo,hi,s[lo],s[hi])    
        self.res = 0
        self.ans = ""
        for i in range(len(s)):
            #odd palindrome
            lo = i
            hi = i
            magic(lo,hi)
            
            #even palindrome
            lo=i
            hi = i +1
            magic(lo,hi)
            
        return self.ans