# 493. Reverse Pairs
class Solution:
    def __init__(self):
        self.count = 0
    def reversePairs(self, nums: List[int]) -> int:
        #a modified merge sort 
        def magic(arr):
            N = len(arr)
            
            if N == 1:
                return arr
            
            left = magic(arr[:N//2])
            right = magic(arr[N//2:])
            
            l, r= 0, 0
            
            while r<len(right) and l<len(left):
                if left[l]<=(right[r]*2):
                    l += 1
                else:
                    # the all the numbers in left after left[l] will be greater
                    # anf hence satisity the condition
                    self.count += len(left)-l
                    r += 1
                    
            return sorted(left+right)
        
        magic(nums)
        return self.count