# 2121. Intervals Between Identical Elements

def getDistances(self, arr: List[int]) -> List[int]:
    N = len(arr)
    dic = {}
    c = {}
    temp = Counter()
    for i,val in enumerate(arr):
        if val in dic:
            dic[val].append(dic[val][-1] + i)
            c[val] += 1
        else:
            dic[val] = [i]
            c[val] = 1

    res = []
    
    for i,val in enumerate(arr):
        first = (((temp[val]+1)*i) - dic[val][temp[val]])
        last =  (dic[val][-1]-dic[val][temp[val]])-((c[val]-(temp[val]+1))*i)
        # print(first,last)
        res.append(first + last)
        temp[val] += 1
    return res
        
        