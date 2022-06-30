# 240. Search a 2D Matrix II

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    N = len(matrix[0])
    M = len(matrix)
    
    m, n = M-1, 0
    
    #we start from left bottom and ther are two cases: actually 3
    
    #case1 : serach value is less
    #if search value is less so all the values in the the current row will be more,
    #so we eleminate the search for the current row and MOVE ONE ROW UP
    
    #case2 : serach value is more
    #if search value is more so all the values in the the current colum will be less,
    #so we eleminate the search for the current column and MOVE ONE COLUMN RIGHT
    
    #case3: if value is equal we return True
    
    #case4: we go out of bound cause the element is not present we break and return Flase
    
    
    while m>=0 and n<N:
        # print(m,n,matrix[m][n])
        val = matrix[m][n]
        if val == target: return True
        #if greater we eliminate current column
        elif val<target: n+= 1
        #if lesser we eleminate current row
        else: m -= 1
    return False