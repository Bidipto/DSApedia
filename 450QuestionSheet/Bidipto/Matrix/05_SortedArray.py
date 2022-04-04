#better meathod to sort an matrix?
def sortedMatrix(self,N,mat):
    arr = []
    for i in mat:
        for j in i:
            arr.append(j)
    arr.sort(reverse = True)
    for i in range(N):
        for j in range(N):
            mat[i][j] = arr.pop()
    return mat