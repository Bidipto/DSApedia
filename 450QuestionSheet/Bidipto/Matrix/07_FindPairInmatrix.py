#if we select a number we can select another only from the lower right quadrant 
#thus we use the dp matrix to store the min value from the upper left quadrant
import math
def findMaxValue(mat, n):
    dp = [[ 0 for i in range(n)] for j in range(n)]
    dp[0][0] = mat[0][0]
    for i in range(1,n):
        dp[0][i] = min(mat[0][i],dp[0][i-1])
    for j in range(1,n):
        dp[j][0] = min(mat[j][0],dp[j-1][0])
    res = -math.inf
    for i in range(1,n):
        for j in range(1,n):
            res = max(res, mat[i][j] - dp[i-1][j-1])
            dp[i][j] = min(mat[i][j],dp[i-1][j],dp[i][j-1])
    return res  