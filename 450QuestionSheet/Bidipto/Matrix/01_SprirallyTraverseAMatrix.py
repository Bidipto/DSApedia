#using the direction variable to know the direction we need to traverse next
def spirallyTraverse(self,matrix, r, c): 
    top = 0
    bottom = r-1
    left = 0
    right = c-1
    
    direction = 1
    res = []
    while bottom >= top and right >= left:
        #we need to traverse the top ie from right to left of the current top row
        if direction == 1:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            direction = 2
        #we need to traverse the right ie from top to bottom of the current right column
        elif direction ==2:
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            direction = 3
        #we need to traverse the bottom ie from left to right of the current bottom row
        elif direction == 3:
            for i in range(right, left -1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            direction = 4
        #we need to traverse the left ie from bottom to top of the current left column
        else:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            direction = 1
    return res