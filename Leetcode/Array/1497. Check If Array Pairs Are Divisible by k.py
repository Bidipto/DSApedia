#make a dict with the count for the remainder obtain upon division with k
def canArrange(self, arr: List[int], k: int) -> bool:
    newArr = []
    for i in arr:
        newArr.append(i%k)
        
    count = collections.Counter(newArr)
    # print(count)
    for key in count:
        if key == 0:
            if count[key]%2:
                # print(key)
                return False
        else:
            if count[key] != count[k-key]:
                # print(key)
                return False 
    return True