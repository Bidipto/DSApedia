# 315. Count of Smaller Numbers After Self
# a modified version of the merge sort algorithm
# see the question reverse pairs
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        count = [0]*len(nums)
        
        def magic(arr):
            N = len(arr)
            
            if N == 1:
                return arr
            
            left = magic(arr[:N//2])
            right = magic(arr[N//2:])
            
            l, r = 0, 0
            R = len(right)
            L = len(left)
            # print(left,right)
            while l<L and r<=R:
                # print(l,r)
                index = left[l][1]
                if r == R:
                    count[index] += R
                    l += 1
                    
                elif left[l][0] > right[r][0]:
                    r += 1
                    
                else:
                    count[index] += r
                    l += 1
            # print(count)       
            return sorted(left+right)
        
        arr = []
        for i,val in enumerate(nums):
            arr.append((val,i))
        # print(arr)
        magic(arr)
        return count