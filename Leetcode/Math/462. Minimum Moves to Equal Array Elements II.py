# 462. Minimum Moves to Equal Array Elements II
# mistook the question to use average of number then relaized its median and not average
# this kinda intuition is hard to come up with kafi

def minMoves2(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        if N%2:
            median = nums[N//2]
        else:
            median = round((nums[N//2] + nums[(N//2)-1])/2)
        # print(median)
        res = 0
        for i in nums:
            res += abs(i-median)
            
        return res