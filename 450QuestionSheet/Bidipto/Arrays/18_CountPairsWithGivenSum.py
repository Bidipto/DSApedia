#similar to leetcode problem 2sum
def getPairsCount(self, arr, n, k):
    dic = {}
    count = 0
    for i in arr:
        if i<=k:
            if i in dic:
                # print(i, k-i, dic[i])
                count += dic[i]
            dic[k-i] = dic.get(k-i, 0) + 1
    return count