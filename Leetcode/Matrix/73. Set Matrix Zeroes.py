def setZeroes(self, matrix: List[List[int]]) -> None:
    #simple storing the row and column in the sets 
    #look up for optimizations
    N = len(matrix[0])
    M = len(matrix)
    
    row = set()
    column = set()

    for i,j in product(range(M),range(N)):
        if matrix[i][j] == 0:
            row.add(i)
            column.add(j)
    # print(row,column)  
    for j in range(N):
        for i in row:
            matrix[i][j] = 0
            
    for i in range(M):
        for j in column:
            matrix[i][j] = 0
            
    return matrix
                