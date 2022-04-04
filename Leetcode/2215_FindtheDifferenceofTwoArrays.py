# 2215. Find the Difference of Two Arrays
def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    s1 = set(nums1)
    s2 = set(nums2)
    answer = [[] for i in range(2)]
    for i in s1:
        if i not in s2:
            answer[0].append(i)
    for i in s2:
        if i not in s1:
            answer[1].append(i)
    return answer