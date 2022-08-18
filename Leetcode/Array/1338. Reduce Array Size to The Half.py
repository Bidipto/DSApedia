#bucket sort 

# 1338. Reduce Array Size to The Half

def minSetSize(self, arr: List[int]) -> int:
    N = len(arr)
    c = collections.Counter(arr)
    bucket = [0]*100001
    for key in c:
        bucket[c[key]] += 1
        
    res = 0
    count = 0
    for i in range(N,-1,-1):
        if bucket[i] == 0:
            continue 
        for j in range(bucket[i]):
            if count >= N//2:
                return res
            count += i
            res += 1
    return res