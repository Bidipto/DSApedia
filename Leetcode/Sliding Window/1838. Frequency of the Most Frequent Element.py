# 1838. Frequency of the Most Frequent Element

def maxFrequency(self, nums: List[int], k: int) -> int:
    nums.sort()
    res = 0
    summ = 0
    i = 0
    for j in range(len(nums)):
        # print(i,j,summ)
        summ += nums[j]
        while k<((j-i+1)*nums[j])-summ:
            summ -= nums[i]
            i += 1
        res = max(res,j-i+1)
    return res