# 179. Largest Number
# again a custom comparator kinda koolll 
class Mod:
    def __init__(self, word):
        self.word = word
    def __gt__(self, other):
        return self.word+other.word > other.word+self.word 
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = [Mod(str(i)) for i in nums]
        res = ""
        for i in sorted(arr, reverse = True):
            res += i.word
        return str(int(res))