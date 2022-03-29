#simply traversing the array column wise
def rowWithMax1s(self,arr, n, m):
    M = len(arr)
    N = len(arr[0])
    for i in range(N):
        for j in range(M):
            if arr[j][i] == 1:
                return j
    return -1
