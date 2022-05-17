# 1641. Count Sorted Vowel Strings
def countVowelStrings(self, n: int) -> int:
        #tabulation with spacee optimization
        prev = [1]*5
          
        for m in range(1,n):
            dp = [0]*5
            summ = 0
            for n in range(5):
                #since we are only concenred about the sum we can just use a forward loop,
                #instead of a back loop 
                summ += prev[n]
                dp[n] = summ
            prev = dp
        return sum(prev)