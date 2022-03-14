def minJumps(self, arr, n):
    # error with 138 case but works fine in the leetcode question
    # 45. jump game 2
    dp = [math.inf for i in range(n)]
    dp[0] = 0
    for i in range(n):
        val = arr[i]
        temp = dp[i] + 1
        for j in range(i + 1, i + val + 1):
            if j<n and temp<dp[j]:
                dp[j] = temp
    # print(dp)
    return -1 if dp[-1] == math.inf else dp[-1]