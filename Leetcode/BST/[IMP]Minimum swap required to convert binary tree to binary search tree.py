# Given an array A[] which represents a Complete Binary Tree i.e, 
# if index i is the parent, index 2*i + 1 is the left child and index 2*i + 2 is the right child.
# The task is to find the minimum number of swaps required to convert it into a Binary Search Tree. 
class Solution:
    def minSwaps(self, n : int, A : List[int]) -> int:
        self.res = []

        def magic(i):
            if i >= len(A):
                return 
            magic((2*i)+1)
            self.res.append(A[i])
            magic((2*i)+2)
    
        magic(0)

        arr = [*enumerate(self.res)]
        arr.sort(key = lambda x: x[1])
        seen = set()
        N = len(A)
        res = 0
        for i in range(N):
            #  print(seen,arr[i])
            if i in seen or arr[i][0] == i:
                continue
            j = i
            cycle = 0
            while j not in seen:
                seen.add(j)
                j = arr[j][0]
                cycle += 1
            if cycle>1: res += cycle-1
        return res
        


