# 1944. Number of Visible People in a Queue

def canSeePersonsCount(self, arr: List[int]) -> List[int]:
    #we start from end and calculate the number of number of people 
    #that are shorter then the curr in the stack and one taller person given by MIN(1,len(Stack))
    N = len(arr)
    
    if N == 1:
        return [0]
    
    res = [0 for i in range(N)]
    stack = [arr[-1]]
    
    for i in range(N-2,-1,-1):
        val = arr[i]
        c = 0
        while stack and stack[-1]<val:
            stack.pop()
            c += 1
        res[i] = c + min(1,len(stack))
        stack.append(val)
    return res