#look literally 2 ways to do this
#hell of a problem 
#dp[i][j] means how much would be the cost if we store words from from i to j(inclusive)

#now we know the cost of storing the words from i to j
# it becomes a problem of what if we store a word in a line or the next line
# here we start building the string 

def solveWordWrap(self, nums, k):
    n = len(nums)
    dp = [[math.inf] * n for i in range(n)]
    for i in range(n): 
        temp = k
        for j in range(i,n):
            temp -= nums[j]
            if temp<0:
                break
            elif j != n-1:
                dp[i][j] = temp * temp
            else:
                dp[i][j] = 0
            temp -= 1
    arr = [0 for i in range(n+1)]
    # [[9, 1, inf, inf], 
    #  [0, 16, 4, inf], 
    #  [0, 0, 16, inf], 
    #  [0, 0, 0, 0]]
    #[3,2,2,5]
    #[0,0,0,0,0]

    #we start buildin the string from the end 
    for i in range(n-1,-1,-1):
        temp = math.inf
        for j in range(i,n):
            if dp[i][j] == math.inf:
                break
            #we take the minimum of the possiblilities
            # dp[i][j] + arr[j+1] means we store i to j in a line plus the best we can do after that
            # follow up qustion could be to print the array 
            # we can do that by maintaining another list along with arr 
            temp = min(temp,dp[i][j] + arr[j+1])
        arr[i] = temp
    return arr[0]