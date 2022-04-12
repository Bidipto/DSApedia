#better solution is possible?
def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
    for q in range(k):
        for i in range(len(grid)):
            temp = grid[i][-1]
            for j in range(len(grid[0])-1, 0, -1):
                grid[i][j] = grid[i][j-1]
            grid[i][0] = temp
        temp = grid[-1][0]
        for i in range(len(grid)-1, 0, -1):
            grid[i][0] = grid[i-1][0]
        grid[0][0] = temp
    return grid