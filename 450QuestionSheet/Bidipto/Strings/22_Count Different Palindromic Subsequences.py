# 730. Count Different Palindromic Subsequences

#a lot easier than i thought lol 
#we just search for leftmost and rightmost index of a common letter and then recursively call the functions
#inside the leftmost and rightmost index
def countPalindromicSubsequences(self, S: str) -> int:
    mod = pow(10,9) + 7
    dp = {}
    def magic(start, end):
        if start == end + 1:
            return 1
        if start >= end:
            return 0
        
        #caching 
        if (start, end) in dp:
            return dp[(start, end)]
        
        count = 0
        for i in "abcd":
            #i is the letter we are looking for 
            left = S.find(i, start, end)
            right = S.rfind(i, start, end)
            
            #incase therer are no i letter i the S[start:end]
            if left == -1 or right == -1:
                continue
            
            #if there is only one i letter in S[start:end]
            if left == right:
                count += 1
            #recursile call to search for more palindromic subsequences
            #ps its not right-1 cause right here is the index and in the call end is exclusive
            else:
                count += 2 + magic(left+1,right)
                
        dp[(start, end)] = count % mod
        return dp[(start, end)]
    
    return magic(0, len(S))