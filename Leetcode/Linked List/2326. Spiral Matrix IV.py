# 2326. Spiral Matrix IV
#modification to spiral matrix
def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
    res = [[-1 for w in range(n)] for q in range(m)]
    print(res)
    #1: left to right
    #2: top to down 
    #3: right to left 
    #4: down to top 
    
    top = 0
    bottom = m - 1
    left = 0
    right = n - 1
    
    direction = 1
    while bottom >= top and right >= left and head:
        if direction == 1:
            for i in range(left, right + 1):
                res[top][i] = head.val
                head = head.next
                if not head:
                    break
            top += 1
            direction = 2
        elif direction ==2:
            for i in range(top, bottom + 1):
                res[i][right] = head.val
                head = head.next
                if not head:
                    break
            right -= 1
            direction = 3
        elif direction == 3:
            for i in range(right, left -1, -1):
                res[bottom][i] = head.val
                head = head.next
                if not head:
                    break
            bottom -= 1
            direction = 4
        else:
            for i in range(bottom, top - 1, -1):
                res[i][left] = head.val
                head = head.next
                if not head:
                    break
            left += 1
            direction = 1
    return res