#the idea is to use the concept of histogram by processing all the rows from top to bottom 
class Solution:
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        N = len(mat[0])
        heights = [0]*N
        res = 0
        for arr in mat:
            for i in range(N):
                if arr[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            # print(heights)
            res = max(self.magic(heights),res)
        return res
    def magic(self, heights: List[int]) -> int:
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