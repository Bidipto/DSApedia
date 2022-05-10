# 456. 132 Pattern
import this
def find132pattern(self, nums: List[int]) -> bool:
    stack  = []
    minn = -math.inf
    #minn is the number is smaller then teh top of the stack
    #we maintain a decending stack and minn storing
    for i in nums[::-1]:
        if i < minn:
            return True
        
        while stack and stack[-1]<i:
            minn = stack.pop()
        stack.append(i)     
    return False