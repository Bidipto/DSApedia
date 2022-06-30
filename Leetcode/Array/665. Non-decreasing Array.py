# 665. Non-decreasing Array

def checkPossibility(self, nums: List[int]) -> bool:
        #in case of a mismath we can either decrease the higher numbeer or 
        #lower the current number 
        flag = False
        prev = nums[0]
        
        for i in range(1,len(nums)):
            # print(prev,nums[i],flag)
            val = nums[i]
            if prev>val:
                if flag:
                    return False
                elif i-2>=0 and nums[i-2]>val:
                    # print(nums[i-2])
                    flag = True
                else:
                    flag = True
                    prev = val
            else:
                prev = val
        return True