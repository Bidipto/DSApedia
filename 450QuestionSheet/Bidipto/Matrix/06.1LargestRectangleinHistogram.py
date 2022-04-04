#the idea is to remeber the last index of the heights lower than then the present height seen
#when the height is decresing, anything above the decresed height becomes useless 
#so we can just pop the stack and update the res
#the idea of start is ki agar humne present se koi zada height wala tower dekha toh,
#the present height is contain in that too 
#
#    ^
#  ^ ^ ^
#  ^ ^ ^ ^
#  for the second tower(0 index) the start would be 0 cause height 2 starts from the zeroth tower
def largestRectangleArea(self, heights: List[int]) -> int:
    stack = [] #pair of values(index,height)
    res = 0
    for i,h in enumerate(heights):
        start = i
        while stack and stack[-1][1]>h:
            index,height = stack.pop()
            res = max(res,height*(i-index))
            start = index
        stack.append([start,h])
    L = len(heights)
    for i,h in stack:
        res = max(res,h*(L-i))
    return res

#TLE solution but i guesss insted of updating each time we could just store the start index
def largestRectangleArea(self, heights: List[int]) -> int:
    M = max(heights)
    curr = [0]*M
    res = 0
    for height in heights:
        for i in range(height):
            curr[i] += 1
            res = max(res,curr[i]*(i+1))
        for j in range(height,M):
            curr[j] = 0
    return res
                