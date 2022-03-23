#slideeeeing window
from collections import deque
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        que = deque()
        summ = 0
        res = math.inf
        for i in nums:
            que.append(i)
            summ += i
            while que and summ>=target:
                res = min(res,len(que))
                summ -= que.popleft()
        return res if res != math.inf else 0