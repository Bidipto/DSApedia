#one of the multiple meathods
def isPalindrome(self, S):
    for i in range(len(S)//2):
        if S[i] != S[-i-1]:
            return 0
    return 1