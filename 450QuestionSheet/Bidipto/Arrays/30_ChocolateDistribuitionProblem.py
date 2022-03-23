#SimpleTwopointersolution
import math
def findMinDiff(self, arr, N, M):
    arr.sort()
    res = math.inf
    # m is pointer at the smallest element in the current window and i at the largest element
    for i in range(M - 1, N):
        m = i - M + 1
        res = min(res, arr[i] - arr[m])
    return res
