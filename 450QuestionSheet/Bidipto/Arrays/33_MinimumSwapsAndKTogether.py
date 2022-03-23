#slidinggggg window and Two pointer
import math
from collections import deque
def minSwap (arr, n, k) : 
    num = 0
    for i in arr:
        if i<=k:
            num += 1
    curr = 0
    que = deque()
    for i in range(num):
        que.append(arr[i])
        if arr[i]>k:
            curr += 1
    res = curr
    for j in range(num, n):
        que.append(arr[j])
        if arr[j]>k:
            curr += 1
        if que.popleft()>k:
            curr -= 1
        res = min(res, curr)
    return res
    
