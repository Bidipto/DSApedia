# 659. Split Array into Consecutive Subsequences

def isPossible(self, nums: List[int]) -> bool:
    seq = collections.Counter()
    freq = collections.Counter(nums)
    
    for num in nums:
        if not freq[num]: continue 
        freq[num] -= 1
        if seq[num-1]>0:
            seq[num-1] -= 1
            seq[num] += 1
        elif freq[num+1]>0 and freq[num+2]>0:
            freq[num+1] -= 1
            freq[num+2] -= 1
            seq[num+2] += 1
        else:
            return False 
        
    return True