#more optimized solution chahiye
class Solution:
    def totalNQueens(self, n: int) -> int:
        grid = [[False for e in range(n)] for q in range(n)]
        res = [0]
        def magic(row,grid,lst):
            # print(row,grid,lst)
            if row == n:
                if len(lst) == n:
                    res[0] += 1
                return
            
            for i in range(n):
                if not grid[row][i]:
                    temp = copy.deepcopy(grid)
                    for j in range(n):
                        temp[row][j] = True
                        temp[j][i] = True
                    for j in range(1, min(n-i,n-row)):
                        temp[row+j][i+j] = True
                    
                    for j in range(1, min(i+1,n-row)):
                        temp[row+j][i-j] = True
                    # print(temp)
                    magic(row+1,temp,lst + [[row,i]])
        
        magic(0,grid,[])
        return res[0]