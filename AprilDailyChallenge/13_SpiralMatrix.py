def generateMatrix(self, n: int) -> List[List[int]]:
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1
    
    matrix = [[0] * n for i in range(n)]
    val = 1
    
    direction = 1
    while bottom >= top and right >= left:
        if direction == 1:
            for i in range(left, right + 1):
                matrix[top][i] = val
                val += 1
            top += 1
            direction = 2
        elif direction ==2:
            for i in range(top, bottom + 1):
                matrix[i][right] = val
                val += 1
            right -= 1
            direction = 3
        elif direction == 3:
            for i in range(right, left -1, -1):
                matrix[bottom][i] = val
                val += 1
            bottom -= 1
            direction = 4
        else:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = val
                val += 1
            left += 1
            direction = 1
    return matrix