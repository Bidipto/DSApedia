#two pointer approach O(n)

def maxArea(self, height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    width = len(height) - 1
    res = 0
    for w in range(width,0,-1):
        # print(res,w,height[left],height[right])
        if height[right]<height[left]:
            res = max(res,height[right]*w)
            right -= 1
        else:
            res = max(res,height[left]*w)
            left += 1
    return res