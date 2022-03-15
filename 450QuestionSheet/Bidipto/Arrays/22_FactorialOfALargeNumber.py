def subArrayExists(self,arr,n):
    res = 0
    s = set()
    s.add(0)
    for i in arr:
        res += i
        if res in s: return True
        s.add(res)
    return False