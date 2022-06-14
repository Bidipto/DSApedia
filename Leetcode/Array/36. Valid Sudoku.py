# 36. Valid Sudoku
def isValidSudoku(self, board: List[List[str]]) -> bool:
    #we need to check for repetations in each row and each column and each mini 
    
    #check for rows 
    for row in board:
        if not self.magic(row):
            # print(row)
            return False
        
    #check for columns 
    for column in zip(*board):
        if not self.magic(column):
            # print(column)
            return False
    #check for minisquares
    for i in range(0,9,3):
        for j in range(0,9,3):
            arr = [board[m][n] for m in range(i,i+3) for n in range(j,j+3)]
            if not self.magic(arr):
                # print(arr)
                return False 
            
    return True
    
def magic(self,arr):
    nums = [int(i) for i in arr if i != "."]
    # print(nums,len(nums) != len(set(nums)))
    return len(nums) == len(set(nums))