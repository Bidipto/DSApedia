from collections import deque
import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        que = deque()
        s = collections.Counter()
        res = 0
        for i in s:
            print(i)
        for i in s:
            print(i)
            print(que,s)
            while que and s[i] != 0:
                    s[que.popleft()] -= 1
            que.append(i)
            s[i] += 1
            res=max(res,len(que))
        return res

s = Solution()
print(s.lengthOfLongestSubstring("abccb"))