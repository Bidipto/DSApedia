#binary search after determining the the element in which the target lies
def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
    N = len(mat)
    M = len(mat[0])
    row = -1
    for i in range(0,N):
        if mat[i][0] <= target and mat[i][-1]>=target:
            row = i
            break
    if row == -1:
        return False
    lo = 0
    hi = M - 1
    while lo<=hi:
        mid = lo + (hi-lo)//2
        if mat[row][mid]<target:
            lo = mid + 1
        elif mat[row][mid]>target:
            hi = mid - 1
        else:
            return True
        # print(lo,hi)
    return False