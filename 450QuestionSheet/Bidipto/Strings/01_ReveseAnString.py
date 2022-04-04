#inplace sorting using a loop and swapping
def reverseString(self, s: List[str]) -> None:
    for i in range(len(s)//2):
        s[i],s[-i-1] = s[-i-1],s[i]
#stack solution
def reverseString(self, s: List[str]) -> None:
    stack = []
    for i in s:
        stack.append(i)
    
    for i in range(len(s)):
        s[i] = stack.pop()
#recursive solution 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        self.magic(s,0)
    def magic(self,s,i):
        if len(s)//2>i:
            s[i],s[-i-1] = s[-i-1],s[i]
            self.magic(s,i+1)
        