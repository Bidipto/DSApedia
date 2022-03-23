def majorityElement(self, nums: List[int]) -> List[int]:
    #naive approach is to use dictionary and counter to store the frequency of all the elements
    #and then check if the frequency is greater than n/3
    dic = Counter(nums)
    res = []
    # print(dic)
    for i in dic:
        if dic[i] > len(nums)//3:
            res.append(i)
    return res
#a better approach is to use Moore's Voting Algorithm
def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) // 3]