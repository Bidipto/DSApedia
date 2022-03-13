#quite impressed by this one, could think of all the edge case and the logic smoothly, ahhaa
def nextPermutation(self, nums: List[int]) -> None:
    if len(nums) == 1:
        return
    if nums == sorted(nums):
        nums[-1],nums[-2] = nums[-2],nums[-1]
    elif nums == sorted(nums, reverse = True):
        nums.sort()
    else:
        #searching for the first peak(or maybe the first decline)
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i + 1]:
                peak = nums[i+1]
                peakpos = i+1
                peakprev = nums[i]
                break
            #if its the last element just swap the last to, optimization thought we can remove the first edge case
        if i + 2 == len(nums):
            nums[-1],nums[-2] = nums[-2],nums[-1]
            return 
        #traversing the right of peak
        #both the cases are handeled by including the peak in the loop
        for i in range(len(nums) - 1, peakpos - 1, -1):
            if nums[i]>peakprev:
                nums[i],nums[peakpos-1] = nums[peakpos - 1],nums[i]
                break
        #sorting after the swap, kafi important
        nums[peakpos:] = sorted(nums[peakpos:])
        